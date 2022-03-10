<script lang="ts">
  import { getContext } from "svelte";
  const { data, width, height } = getContext("LayerCake");
  import { onMount } from "svelte";
  import { fade, draw, crossfade } from "svelte/transition";
  import { scaleLinear, scaleOrdinal } from "d3-scale";
  import { zoom, zoomIdentity } from "d3-zoom";
  import { schemeCategory10 } from "d3-scale-chromatic";
  import { select, selectAll } from "d3-selection";
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
    drag,
    forceSimulation,
    forceLink,
    forceManyBody,
    forceCenter,
    forceCollide,
  };
  let svg;
  let w = $width;
  let h = $height;
  const nodeRadius = 5;
  const padding = { top: 20, right: 40, bottom: 40, left: 25 };
  $: graph = $data.length == 0 ? { nodes: [], links: [] } : $data;
  $: links = graph.links.map((d) => Object.create(d));
  $: nodes = graph.nodes.map((d) => Object.create(d));
  const colourScale = d3.scaleOrdinal(d3.schemeCategory10);
  let transform = d3.zoomIdentity;
  $: simulation = d3
    .forceSimulation(nodes)
    .force(
      "link",
      d3
        .forceLink(links)
        .id((d) => d.name)
        .distance((link) => (link.ignore ? 300 : 30)),
    )
    .force(
      "collision",
      d3.forceCollide().radius((d) => 25),
    )
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter($width / 2, $height / 2))
    .on("tick", simulationUpdate);

  onMount(() => {
    d3.select(svg)
      .append("svg:defs")
      .selectAll("marker")
      .data(["end"]) // Different link/path types can be defined here
      .enter()
      .append("svg:marker") // This section adds in the arrows
      .attr("id", String)
      .attr("viewBox", "0 -5 10 10")
      .attr("refX", 15)
      .attr("refY", -1.5)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
      .append("svg:path")
      .attr("d", "M0,-5L10,0L0,5");
    d3.select(svg)
      .call(
        d3
          .drag()
          .container(svg)
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
  });

  function simulationUpdate() {
    nodes = [...nodes];
    links = [...links];
  }

  function zoomed(currentEvent) {
    transform = currentEvent.transform;
    simulationUpdate();
  }

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
</script>

<div class="flex flex-col">
  <div class="flex justify-center">
    <div class="form-check">
      <input type="checkbox" bind:checked={labels} />
      <label class="form-check-label inline-block text-gray-800" for="flexCheckChecked">
        Show labels
      </label>
    </div>
  </div>
  <svg class="grow" bind:this={svg} width={w} height={h / 1.15}>
    {#each links as link}
      <g stroke={link.ignore ? "" : "#999"} stroke-opacity="0.6">
        <line
          x1={link.source.x}
          y1={link.source.y}
          x2={link.target.x}
          y2={link.target.y}
          marker-end={link.ignore ? "" : "url(#end)"}
          transform="translate({transform.x} {transform.y}) scale({transform.k} {transform.k})"
        >
          <title>{link.source.id}</title>
        </line>
        <text
          class={link.ignore ? "hidden" : ""}
          transform="translate({transform.x} {transform.y}) scale({transform.k} {transform.k})"
          x={(link.source.x + link.target.x) / 2}
          y={(link.source.y + link.target.y) / 2}
          dx="12"
          dy="0.35em">{link.label}</text
        >
      </g>
    {/each}

    {#each nodes as point}
      <circle
        class="node"
        r={point.name == "__broker__" ? 0 : 5}
        fill={colourScale(point.group)}
        cx={point.x}
        cy={point.y}
        transform="translate({transform.x} {transform.y}) scale({transform.k} {transform.k})"
      >
        <title>{point.id}</title></circle
      >
      {#if labels}
        <text
          class="label {point.name == '__broker__' ? 'hidden' : ''}"
          transform="translate({transform.x} {transform.y}) scale({transform.k} {transform.k})"
          x={point.x}
          y={point.y}
          dx="12"
          dy=".35em">{point.federate} - {point.name}</text
        >
      {/if}
    {/each}
  </svg>
</div>

<style>
  svg {
    width: 100%;
    height: 100%;
    background-color: #f0f0f0;
  }
  circle {
    stroke: #fff;
    stroke-width: 1.5;
  }
</style>
