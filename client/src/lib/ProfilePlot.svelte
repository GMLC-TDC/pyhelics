<script lang="ts">
  import { spring, tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { afterUpdate, beforeUpdate, getContext, onMount } from "svelte";
  import { get, writable } from "svelte/store";
  import { Svg } from "layercake";

  import * as d3 from "d3";

  const { data, width, height } = getContext("LayerCake");

  function minmaxData(data) {
    var min = Infinity;
    var max = -Infinity;
    for (const [k, v] of Object.entries(data)) {
      for (const e of v) {
        if (e.r_enter < min) {
          min = e.r_enter;
        }
        if (e.r_end > max) {
          max = e.r_end;
        }
      }
    }
    return [min, max];
  }

  function lowhighData(data) {
    var min = Infinity;
    var max = -Infinity;
    for (const [k, v] of Object.entries(data)) {
      for (const e of v) {
        if (e.r_end - e.r_enter < min) {
          min = e.r_end - e.r_enter;
        }
        if (e.r_end - e.r_enter > max) {
          max = e.r_end - e.r_enter;
        }
      }
    }
    return [min, max];
  }

  $: names = Object.keys($data);
  $: yScale = d3.scaleBand().domain(names).range([$height, 0]);
  $: [xMin, xMax] = minmaxData($data);
  $: xScale = d3
    .scaleLinear()
    .domain([xMin, xMax])
    .range([75, $width - 100]);
  $: colorScale = (c) =>
    d3.interpolateRdYlBu(d3.scaleLinear().domain(lowhighData($data)).range([1, 0])(c));

  const SCALING = 1e9;
</script>

<Svg viewBox="0 0 {$width} {$height}">
  {#each Object.entries($data) as [k, v]}
    <g>
      {#each v as e}
        <rect
          x={100 + xScale(e.r_enter)}
          y={yScale(e.name)}
          width={xScale(e.r_end) - xScale(e.r_enter)}
          height={($height / names.length) * 0.9}
          style="fill:{colorScale(e.r_end - e.r_enter)};stroke-width:0.25;stroke:rgb(0,0,0)"
        >
          <title>{k} (t = {e.s_enter})</title>
        </rect>
      {/each}
      <text x="0" y={yScale(k) + 25}>{k}</text>
    </g>
  {/each}
</Svg>
