<script lang="ts">
  import { browser } from "$app/env";
  import { base } from "$app/paths";
  import { onMount } from "svelte";
  import Fa from "svelte-fa";
  import Table from "$lib/Table.svelte";
  import Dropzone from "svelte-file-dropzone";
  import { data, DEFAULT } from "$lib/stores";
  const BASE = "http://127.0.0.1:5000/api/runner";

  let files = {
    accepted: [],
    rejected: [],
  };

  async function updateData() {
    $data.runner = await (await fetch(`${BASE}/file`)).json();
  }

  async function handleFilesSelect(e) {
    console.log(e);
    const { acceptedFiles, fileRejections } = e.detail;
    files.accepted = [...files.accepted, ...acceptedFiles];
    files.rejected = [...files.rejected, ...fileRejections];
    var form = new FormData();
    form.append("file", files.accepted[0]);
    await fetch(`${BASE}/file`, {
      method: "POST",
      body: form,
    });
    await updateData();
  }

  async function handleClearClick(e) {
    $data.runner = {};
  }

  $: console.log($data.runner);
</script>

<div class="flex w-7/8 flex-col mt-6 mx-8">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      <div class="flex space-x-4">
        <Dropzone on:drop={handleFilesSelect} multiple="false">
          <p>Drag 'n' drop a "runner.json" file here, or click to select a "runner.json" file</p>
        </Dropzone>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          on:click={handleClearClick}>Clear</button
        >
      </div>
      {#if Object.keys($data.runner).length != 0}
        <div class="grid grid-cols-1 gap-2">
          <h3 class="font-medium leading-tight text-2xl pt-4 mb-2 text-blue-600">Runner</h3>
          {#each $data.runner.federates as federate}
            <div class="flex justify-center">
              <div
                class="flex flex-col md:flex-row w-full rounded-lg bg-white shadow-lg justify-between"
              >
                <div class="p-6 flex flex-col justify-start">
                  <h5
                    class="text-xl font-medium mb-2 text-blue-600 hover:text-blue-700 transition duration-300 ease-in-out"
                  >
                    {federate.name}
                  </h5>
                  <p>
                    <span class="text-slate-400">exec: </span>
                    <code class="text-gray-700">
                      {federate.exec}
                    </code>
                  </p>
                  <p>
                    <span class="text-slate-400">dir: </span>
                    <code class="text-gray-700">
                      "{federate.directory}"
                    </code>
                  </p>
                </div>
                <!-- <div class="flex flex-col p-6"> -->
                <!--   <button -->
                <!--     class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" -->
                <!--     >Tail Log File</button -->
                <!--   > -->
                <!-- </div> -->
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  </div>
</div>
