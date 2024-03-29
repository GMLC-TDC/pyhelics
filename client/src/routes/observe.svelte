<script lang="ts">
  import { browser } from "$app/env";
  import { base } from "$app/paths";
  import { onMount } from "svelte";
  import Fa from "svelte-fa";
  import Table from "$lib/Table.svelte";
  import Dropzone from "svelte-file-dropzone";
  import { data, DEFAULT } from "$lib/stores";
  import Topology from "$lib/Topology.svelte";
  const BASE = "http://127.0.0.1:5000/api/observer";

  function isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }

  function getCoreName(id) {
    for (const core of $data.cores) {
      if (core.id == id) {
        return core.name;
      }
    }
  }

  function getFederateName(id) {
    for (const federate of $data.federates) {
      if (federate.id == id) {
        return federate.name;
      }
    }
  }

  function getSubscriptionName(source, target) {
    for (const publication of $data.publications) {
      if (source == publication.source && target == publication.target) {
        return publication.name;
      }
    }
  }

  async function updateData() {
    $data.systeminfo = await (await fetch(`${BASE}/systeminfo`)).json();

    $data.cores = await (await fetch(`${BASE}/cores`)).json();

    $data.federates = await (await fetch(`${BASE}/federates`)).json();
    $data.federates.map((f) => (f.core_name = getCoreName(f.parent)));
    $data.federates = $data.federates;

    $data.graphs = await (await fetch(`${BASE}/graphs`)).json();

    $data.publications = await (await fetch(`${BASE}/publications`)).json();
    $data.publications.map((p) => {
      p.source_name = getFederateName(p.source);
      p.target_name = getFederateName(p.target);
    });
    $data.publications = $data.publications;

    $data.inputs = await (await fetch(`${BASE}/inputs`)).json();
    $data.inputs.map((i) => {
      i.source_name = getFederateName(i.source);
      i.target_name = getFederateName(i.target);
    });
    $data.inputs = $data.inputs;

    function getDataTitle(k) {
      if (k == "id") {
        return "ID";
      } else if (k == "simulation_time") {
        return "Simulation Time";
      } else {
        return k;
      }
    }

    $data.table = await (await fetch(`${BASE}/data`)).json();
    const table_columns = [];
    for (const k of Object.keys($data.table[0])) {
      if (k != "updated_at") {
        table_columns.push({
          field: k,
          sortName: k,
          title: getDataTitle(k),
          show: true,
          sort: "ascending",
          sortColor: "#fff",
          sortActive: true,
          text_center: false,
        });
      }
    }
    $data.table_columns = table_columns;
  }

  let files = {
    accepted: [],
    rejected: [],
  };

  async function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail;
    files.accepted = [...files.accepted, ...acceptedFiles];
    files.rejected = [...files.rejected, ...fileRejections];
    var data = new FormData();
    data.append("file", files.accepted.at(-1));
    await fetch(`${BASE}/database`, {
      method: "POST",
      body: data,
    });
    await updateData();
  }

  async function handleClearClick(e) {
    const profile = $data.profile;
    $data = DEFAULT;
    $data.profile = profile;
  }
</script>

<div class="flex w-7/8 flex-col mt-6 mx-8">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      <div class="flex space-x-4">
        <Dropzone on:drop={handleFilesSelect} multiple="false">
          <p>
            Drag 'n' drop a observer generated "helics-cli.sqlite" file here, or click to select a
            "helics-cli.sqlite" file
          </p>
        </Dropzone>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          on:click={handleClearClick}>Clear</button
        >
      </div>

      {#if Object.keys($data.systeminfo).length != 0}
        <div class="my-4">
          HELICS Version: {$data.systeminfo.version.string}
        </div>
      {/if}

      {#if $data.table.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Topology</h3>
        <Topology />
      {/if}

      {#if $data.cores.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Cores</h3>
        <Table data={$data.cores} columns={$data.cores_columns} />
      {/if}

      {#if $data.federates.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Federates</h3>
        <Table data={$data.federates} columns={$data.federates_columns} />
      {/if}

      {#if $data.publications.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Publications</h3>
        <Table data={$data.publications} columns={$data.publications_columns} />
      {/if}

      {#if $data.inputs.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Inputs</h3>
        <Table data={$data.inputs} columns={$data.inputs_columns} />
      {/if}

      {#if $data.table.length != 0}
        <h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">data</h3>
        <Table data={$data.table} columns={$data.table_columns} />
      {/if}
    </div>
  </div>
</div>
