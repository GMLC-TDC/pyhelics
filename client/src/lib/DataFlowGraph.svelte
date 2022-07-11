<script lang="ts">
  import { getContext } from "svelte";
  const { data, width, height } = getContext("LayerCake");
  import { onMount, onDestroy, tick } from "svelte";
  import { fade, draw, crossfade } from "svelte/transition";
  import { scaleLinear, scaleOrdinal } from "d3-scale";
  import { zoom, zoomIdentity } from "d3-zoom";
  import { schemeCategory10 } from "d3-scale-chromatic";
  import { select, selectAll, pointer } from "d3-selection";
  import { drag } from "d3-drag";
  import { forceSimulation, forceLink, forceManyBody, forceCenter, forceCollide } from "d3-force";

  let labels = true;
  let d3 = {
    zoom,
    zoomIdentity,
    scaleLinear,
    scaleOrdinal,
    schemeCategory10,
    select,
    selectAll,
    pointer,
    drag,
    forceSimulation,
    forceLink,
    forceManyBody,
    forceCenter,
    forceCollide,
  };
  let canvas;
  let w = $width;
  let h = $height;
  const nodeRadius = 5;
  const padding = { top: 20, right: 40, bottom: 40, left: 25 };
  $: graph = $data.length == 0 ? { nodes: [], links: [] } : $data;
  const groupColour = d3.scaleOrdinal(d3.schemeCategory10);
  let transform = d3.zoomIdentity;
  let simulation, context;

  const unsubscribe = data.subscribe(async ($data) => {
    // Have to use tick so links and nodes can catch up
    await tick();
    render();
  });
  onDestroy(() => {
    unsubscribe();
  });

  function render() {
    console.log({ graph });
    if (simulation) {
      simulation.nodes([]).force("link", d3.forceLink([]));
      simulation = undefined;
    }
    context = canvas.getContext("2d");
    resize();

    simulation = d3
      .forceSimulation(graph.nodes)
      .force(
        "link",
        d3.forceLink(graph.links).id((d) => d.name),
      )
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter($width / 2, $height / 2))
      .on("tick", simulationUpdate);
    // title
    d3.select(context.canvas).on("mousemove", (event) => {
      const mouse = d3.pointer(event);
      const d = simulation.find(
        transform.invertX(mouse[0]),
        transform.invertY(mouse[1]),
        nodeRadius,
      );

      if (d) context.canvas.title = d.index;
      else context.canvas.title = "";
    });
    d3.select(canvas)
      .call(
        d3
          .drag()
          .container(canvas)
          .subject(dragsubject)
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended),
      )
      .call(
        d3
          .zoom()
          .scaleExtent([1 / 10, 8])
          .on("zoom", zoomed),
      );
  }
  function simulationUpdate() {
    context.save();
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
    context.translate(transform.x, transform.y);
    context.scale(transform.k, transform.k);
    graph.links.forEach((d) => {
      if (d.source.name == "__broker__" || d.target.name == "__broker__") {
        return;
      }
      context.beginPath();
      var dx = d.target.x - d.source.x;
      var dy = d.target.y - d.source.y;
      var angle = Math.atan2(dy, dx);
      var head = nodeRadius;
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(
        d.target.x - Math.cos(angle) * nodeRadius * 1.2,
        d.target.y - Math.sin(angle) * nodeRadius * 1.2,
      );
      context.lineTo(
        d.target.x - Math.cos(angle) * nodeRadius * 1.2 - head * Math.cos(angle - Math.PI / 6),
        d.target.y - Math.sin(angle) * nodeRadius * 1.2 - head * Math.sin(angle - Math.PI / 6),
      );
      context.moveTo(
        d.target.x - Math.cos(angle) * nodeRadius * 1.2,
        d.target.y - Math.sin(angle) * nodeRadius * 1.2,
      );
      context.lineTo(
        d.target.x - Math.cos(angle) * nodeRadius * 1.2 - head * Math.cos(angle + Math.PI / 6),
        d.target.y - Math.sin(angle) * nodeRadius * 1.2 - head * Math.sin(angle + Math.PI / 6),
      );
      context.globalAlpha = 0.6;
      context.strokeStyle = "#999";
      context.lineWidth = Math.sqrt(d.value);
      context.stroke();
      context.globalAlpha = 1;
    });

    graph.nodes.forEach((d, i) => {
      if (d.name == "__broker__") {
        return;
      }
      context.beginPath();
      context.arc(d.x, d.y, nodeRadius, 0, 2 * Math.PI);
      context.strokeStyle = "#fff";
      context.lineWidth = 1.5;
      context.stroke();
      context.fillStyle = groupColour(d.group);
      context.fill();
      context.fillText(d.name, d.x + 10, d.y + 3);
    });
    context.restore();
  }
  function zoomed(currentEvent) {
    transform = currentEvent.transform;
    simulationUpdate();
  }
  // Use the d3-force simulation to locate the node
  function dragsubject(currentEvent) {
    const node = simulation.find(
      transform.invertX(currentEvent.x),
      transform.invertY(currentEvent.y),
      nodeRadius,
    );
    if (node) {
      node.x = transform.applyX(node.x);
      node.y = transform.applyY(node.y);
    }
    return node;
  }
  function dragstarted(currentEvent) {
    if (!currentEvent.active) simulation.alphaTarget(0.3).restart();
    currentEvent.subject.fx = transform.invertX(currentEvent.subject.x);
    currentEvent.subject.fy = transform.invertY(currentEvent.subject.y);
  }
  function dragged(currentEvent) {
    currentEvent.subject.fx = transform.invertX(currentEvent.x);
    currentEvent.subject.fy = transform.invertY(currentEvent.y);
  }
  function dragended(currentEvent) {
    if (!currentEvent.active) simulation.alphaTarget(0);
    currentEvent.subject.fx = null;
    currentEvent.subject.fy = null;
  }
  function resize() {
    ({ w, h } = canvas);
  }
</script>

<svelte:window on:resize={resize} />

<div class="container">
  <canvas bind:this={canvas} width={$width} height={$height} />
</div>

<style>
  canvas {
    float: left;
  }
</style>
