<script lang="ts">
  import { spring, tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { afterUpdate, beforeUpdate, getContext, onMount } from "svelte";
  import { get, writable } from "svelte/store";
  import { Svg } from "layercake";

  import * as d3 from "d3";

  const { data, width, height } = getContext("LayerCake");

  const SCALING = 1e9;
</script>

<Svg>
  {#each $data as profile}
    <rect />
  {/each}
</Svg>
