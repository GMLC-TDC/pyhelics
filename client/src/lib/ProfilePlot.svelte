<script lang="ts">
  import { spring, tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { afterUpdate, beforeUpdate, getContext, onMount } from "svelte";
  import { get, writable } from "svelte/store";
  import { Svg } from "layercake";
  import { data as store_data } from "$lib/stores";

  import * as d3 from "d3";

  const { data, width, height } = getContext("LayerCake");

  $: start_index = $store_data.profile_toggle_value == "real_time" ? "r_enter" : "s_enter";
  $: end_index = $store_data.profile_toggle_value == "real_time" ? "r_end" : "s_end";

  function minmaxData(data) {
    var min = Infinity;
    var max = -Infinity;
    for (const [k, v] of Object.entries(data)) {
      for (const e of v) {
        if (e[start_index] < min) {
          min = e[start_index];
        }
        if (e[end_index] > max) {
          max = e[end_index];
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
        if (e[end_index] - e[start_index] < min) {
          min = e[end_index] - e[start_index];
        }
        if (e[end_index] - e[start_index] > max) {
          max = e[end_index] - e[start_index];
        }
      }
    }
    return [min, max];
  }

  function legend({
    color,
    title,
    tickSize = 6,
    width = 320,
    height = 44 + tickSize,
    marginTop = 18,
    marginRight = 0,
    marginBottom = 16 + tickSize,
    marginLeft = 0,
    ticks = width / 64,
    tickFormat,
    tickValues,
  } = {}) {
    d3.select(color_legend_svg).selectAll("*").remove();

    const svg = d3
      .select(color_legend_svg)
      .attr("width", width)
      .attr("height", height)
      .attr("viewBox", [0, 0, width, height])
      .style("overflow", "visible")
      .style("display", "block");

    let tickAdjust = (g) => g.selectAll(".tick line").attr("y1", marginTop + marginBottom - height);
    let x;

    // Continuous
    if (color.interpolate) {
      const n = Math.min(color.domain().length, color.range().length);

      x = color.copy().rangeRound(d3.quantize(d3.interpolate(marginLeft, width - marginRight), n));

      svg
        .append("image")
        .attr("x", marginLeft)
        .attr("y", marginTop)
        .attr("width", width - marginLeft - marginRight)
        .attr("height", height - marginTop - marginBottom)
        .attr("preserveAspectRatio", "none")
        .attr(
          "xlink:href",
          ramp(color.copy().domain(d3.quantize(d3.interpolate(0, 1), n))).toDataURL(),
        );
    }

    // Sequential
    else if (color.interpolator) {
      x = Object.assign(
        color.copy().interpolator(d3.interpolateRound(marginLeft, width - marginRight)),
        {
          range() {
            return [marginLeft, width - marginRight];
          },
        },
      );

      svg
        .append("image")
        .attr("x", marginLeft)
        .attr("y", marginTop)
        .attr("width", width - marginLeft - marginRight)
        .attr("height", height - marginTop - marginBottom)
        .attr("preserveAspectRatio", "none")
        .attr("xlink:href", ramp(color.interpolator()).toDataURL());

      // scaleSequentialQuantile doesn’t implement ticks or tickFormat.
      if (!x.ticks) {
        if (tickValues === undefined) {
          const n = Math.round(ticks + 1);
          tickValues = d3.range(n).map((i) => d3.quantile(color.domain(), i / (n - 1)));
        }
        if (typeof tickFormat !== "function") {
          tickFormat = d3.format(tickFormat === undefined ? ",f" : tickFormat);
        }
      }
    }

    // Threshold
    else if (color.invertExtent) {
      const thresholds = color.thresholds
        ? color.thresholds() // scaleQuantize
        : color.quantiles
        ? color.quantiles() // scaleQuantile
        : color.domain(); // scaleThreshold

      const thresholdFormat =
        tickFormat === undefined
          ? (d) => d
          : typeof tickFormat === "string"
          ? d3.format(tickFormat)
          : tickFormat;

      x = d3
        .scaleLinear()
        .domain([-1, color.range().length - 1])
        .rangeRound([marginLeft, width - marginRight]);

      svg
        .append("g")
        .selectAll("rect")
        .data(color.range())
        .join("rect")
        .attr("x", (d, i) => x(i - 1))
        .attr("y", marginTop)
        .attr("width", (d, i) => x(i) - x(i - 1))
        .attr("height", height - marginTop - marginBottom)
        .attr("fill", (d) => d);

      tickValues = d3.range(thresholds.length);
      tickFormat = (i) => thresholdFormat(thresholds[i], i);
    }

    // Ordinal
    else {
      x = d3
        .scaleBand()
        .domain(color.domain())
        .rangeRound([marginLeft, width - marginRight]);

      svg
        .append("g")
        .selectAll("rect")
        .data(color.domain())
        .join("rect")
        .attr("x", x)
        .attr("y", marginTop)
        .attr("width", Math.max(0, x.bandwidth() - 1))
        .attr("height", height - marginTop - marginBottom)
        .attr("fill", color);

      tickAdjust = () => {};
    }

    svg
      .append("g")
      .attr("transform", `translate(0,${height - marginBottom})`)
      .call(
        d3
          .axisBottom(x)
          .ticks(ticks, typeof tickFormat === "string" ? tickFormat : undefined)
          .tickFormat(typeof tickFormat === "function" ? tickFormat : undefined)
          .tickSize(tickSize)
          .tickValues(tickValues),
      )
      .call(tickAdjust)
      .call((g) => g.select(".domain").remove())
      .call((g) =>
        g
          .append("text")
          .attr("x", marginLeft)
          .attr("y", marginTop + marginBottom - height - 6)
          .attr("fill", "currentColor")
          .attr("text-anchor", "start")
          .attr("font-weight", "bold")
          .text(title),
      );

    return svg.node();
  }

  function ramp(color, n = 256) {
    var canvas = document.createElement("canvas");
    canvas.width = n;
    canvas.height = 1;
    const context = canvas.getContext("2d");
    for (let i = 0; i < n; ++i) {
      context.fillStyle = color(i / (n - 1));
      context.fillRect(i, 0, 1, 1);
    }
    return canvas;
  }

  let color_legend_svg = null;

  $: {
    legend({
      color: d3.scaleSequential(lowhighData($data).reverse(), d3.interpolateRdYlBu),
      title: "Simulation Time (s)",
      width: $width,
      start_index,
      end_index,
    });
  }

  $: names = Object.keys($data);
  $: yScale = d3.scaleBand().domain(names).range([$height, 0]);
  $: [xMin, xMax] = minmaxData($data, start_index, end_index);
  $: xScale = d3
    .scaleLinear()
    .domain([xMin, xMax])
    .range([75, $width - 100]);
  $: colorScale = (c) =>
    d3.interpolateRdYlBu(d3.scaleLinear().domain(lowhighData($data)).range([1, 0])(c));

  $: SCALING = $store_data.profile_toggle_value == "real_time" ? 1e9 : 1;
</script>

<div class="container">
  <svg bind:this={color_legend_svg} />
</div>

<div class="container py-10">
  <Svg viewBox="0 0 {$width} {$height}">
    {#each Object.entries($data) as [k, v]}
      <g>
        {#each v as e}
          <rect
            x={100 + xScale(e[start_index])}
            y={yScale(e.name) + 75}
            width={xScale(e[end_index]) - xScale(e[start_index])}
            height={($height / names.length) * 0.9}
            style="fill:{colorScale(
              e[end_index] - e[start_index],
            )};stroke-width:0.25;stroke:rgb(0,0,0)"
          >
            <title
              >{k} (time = {e.s_enter}): elapsed = {(e[end_index] - e[start_index]).toFixed(
                2,
              )}s</title
            >
          </rect>
        {/each}
        <text x="0" y={yScale(k) + 100}>{k}</text>
      </g>
    {/each}
  </Svg>
</div>
