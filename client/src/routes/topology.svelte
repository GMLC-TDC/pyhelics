<script lang="ts">
  import { data } from "$lib/stores";
  import DataFlowGraph from "$lib/DataFlowGraph.svelte";
  import { onMount } from "svelte";

  import { LayerCake } from "layercake";

  function createGraph(f, d) {
    let nodes = [];
    let links = [];
    let keys = {};
    let i = 0;
    nodes.push({ name: "__broker__", group: 0 });
    for (const core of d.cores) {
      for (const federate of core.federates) {
        if (federate.publications === undefined) {
          federate.publications = [];
        }
        for (const publication of federate.publications) {
          nodes.push({
            name: `${publication.federate}-${publication.handle}`,
            federate: federate.attributes.name,
            group: 1,
          });

          if (publication.targets === undefined) {
            publication.targets = [];
          }
          keys[`${publication.federate}-${publication.handle}`] = publication.key;
          for (const target of publication.targets) {
            links.push({
              source: `${publication.federate}-${publication.handle}`,
              target: `${target.federate}-${target.handle}`,
              label: keys[`${publication.federate}-${publication.handle}`],
              ignore: false,
            });
            links.push({
              source: `${publication.federate}-${publication.handle}`,
              target: "__broker__",
              ignore: true,
            });
            links.push({
              source: `${target.federate}-${target.handle}`,
              target: "__broker__",
              ignore: true,
            });
          }
        }
      }
    }
    for (const core of d.cores) {
      for (const federate of core.federates) {
        if (federate.inputs === undefined) {
          federate.inputs = [];
        }
        for (const input of federate.inputs) {
          nodes.push({
            name: `${input.federate}-${input.handle}`,
            federate: federate.attributes.name,
            group: 2,
          });

          if (input.sources === undefined) {
            input.sources = [];
          }
          for (const source of input.sources) {
            links.push({
              source: `${source.federate}-${source.handle}`,
              target: `${input.federate}-${input.handle}`,
              label: keys[`${source.federate}-${source.handle}`],
              ignore: false,
            });
            links.push({
              source: `${input.federate}-${input.handle}`,
              target: "__broker__",
              ignore: true,
            });
            links.push({
              source: `${source.federate}-${source.handle}`,
              target: "__broker__",
              ignore: true,
            });
          }
        }
      }
    }
    nodes = Array.from(new Set(nodes.map(JSON.stringify))).map(JSON.parse);
    links = Array.from(new Set(links.map(JSON.stringify))).map(JSON.parse);
    return {
      nodes,
      links,
    };
  }

  let graph;

  onMount(() => {
    graph = createGraph($data.graphs.federate, $data.graphs.data);
  });
</script>

<div class="flex flex-col h-full">
  <div class="grow grid grid-areas-layout justify-items-stretch my-auto">
    <LayerCake data={graph}>
      <DataFlowGraph />
    </LayerCake>
  </div>
</div>
