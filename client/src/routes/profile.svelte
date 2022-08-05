<script lang="ts">
  import { data } from "$lib/stores";
  import ProfilePlot from "$lib/ProfilePlot.svelte";
  import DataFlowGraph from "$lib/DataFlowGraph.svelte";
  import { onMount } from "svelte";

  import { LayerCake } from "layercake";
  import Switch from "$lib/Switch.svelte";
  import Dropzone from "svelte-file-dropzone";
  const BASE = "http://127.0.0.1:5000/api";

  let files = {
    accepted: [],
    rejected: [],
  };

  async function updateData() {
    $data.profile = await (await fetch(`${BASE}/profiler`)).json();
  }

  async function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail;
    files.accepted = [...files.accepted, ...acceptedFiles];
    files.rejected = [...files.rejected, ...fileRejections];
    var form = new FormData();
    form.append("file", files.accepted.at(-1));
    const r = await fetch(`${BASE}/profiler`, {
      method: "POST",
      body: form,
    });
    console.log(await r.json());
    await updateData();
  }

  async function handleClearClick(e) {
    $data.profile = [];
  }
</script>

<div class="container flex w-7/8 flex-col mt-6">
  <div class="overflow-x-auto">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      <div class="flex space-x-4">
        <Dropzone on:drop={handleFilesSelect} multiple="false">
          <p>Drag 'n' drop a "profile.txt" file here, or click to select a "profile.txt" file</p>
        </Dropzone>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          on:click={handleClearClick}>Clear</button
        >
      </div>
      <Switch
        bind:value={$data.profile_toggle_value}
        label="Choose a theme"
        design="multi"
        options={["real_time", "simulation_time"]}
        fontSize={12}
      />
    </div>
  </div>

  <div class="flex flex-grow my-4 w-full place-items-center">
    <LayerCake bind:data={$data.profile}>
      <ProfilePlot />
    </LayerCake>
  </div>
</div>

<style>
  .container {
    height: 75vh;
  }
</style>
