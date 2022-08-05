<script lang="ts">
  import { browser } from "$app/env";
  import { base } from "$app/paths";
  import { onMount, onDestroy, tick } from "svelte";
  import Fa from "svelte-fa";
  import {
    faCheckCircle,
    faSync,
    faSkullCrossbones,
    faQuestionCircle,
    faTimesCircle,
  } from "@fortawesome/free-solid-svg-icons";
  import Dropzone from "svelte-file-dropzone";
  import { data, DEFAULT } from "$lib/stores";
  const BASE = "http://127.0.0.1:5000/api/runner";

  let files = {
    accepted: [],
    rejected: [],
  };

  async function updateData() {
    $data.runner = await (await fetch(`${BASE}/file`)).json();
    processing = (await (await fetch(`${BASE}/run`)).json()).status;
  }

  async function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail;
    files.accepted = [...files.accepted, ...acceptedFiles];
    files.rejected = [...files.rejected, ...fileRejections];
    var form = new FormData();
    form.append("file", files.accepted.at(-1));
    await fetch(`${BASE}/file`, {
      method: "POST",
      body: form,
    });
    clearInterval(interval);
    interval = setInterval(async () => {
      await updateData();
      await tick();
    }, 1000);
  }

  async function handleClearClick(e) {
    $data.runner = DEFAULT.runner;
    processing = false;
    clearInterval(interval);
  }

  async function handleEditSaveChanges(e) {
    const r = await fetch(`${BASE}/file/edit`, {
      method: "PUT",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(current_federate),
    });
    console.log(r);
  }

  async function handleDelete(federate) {
    const r = await fetch(`${BASE}/file/edit`, {
      method: "DELETE",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(federate),
    });
    console.log(r);
  }

  async function handleAdd(e) {
    const r = await fetch(`${BASE}/file/edit`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(current_federate),
    });
    console.log(r);
  }

  async function handleRun(e) {
    const r = await fetch(`${BASE}/run`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
    });
    console.log(r);
  }

  async function handleCancel(e) {
    const r = await fetch(`${BASE}/run`, {
      method: "DELETE",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
    });
    console.log(r);
  }

  async function handleLoad(e) {
    const r = await fetch(`${BASE}/file/path`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ path: $data.runner_path }),
    });
    console.log(r);
    clearInterval(interval);
    interval = setInterval(async () => {
      await updateData();
      await tick();
    }, 1000);
  }

  async function handleLog(e) {
    const r = await (
      await fetch(`${BASE}/log/${current_federate.name}`, {
        method: "GET",
        mode: "cors",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
      })
    ).json();
    current_federate.log = r.log;
  }

  let interval = null;
  onMount(async () => {
    clearInterval(interval);
    interval = setInterval(async () => {
      await updateData();
      await tick();
    }, 1000);
  });

  onDestroy(() => {
    clearInterval(interval);
  });

  let current_federate = { name: null, directory: null, exec: null };
  let processing = false;
</script>

<div class="flex w-7/8 flex-col mt-6 mx-8">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      {#if Object.keys($data.runner).length == 0}
        <Dropzone on:drop={handleFilesSelect} multiple="false">
          <p>Drag 'n' drop a "runner.json" file here, or click to select a "runner.json" file</p>
        </Dropzone>
      {:else}
        <div class="grid grid-cols-1 gap-2">
          <div class="flex justify-between py-4">
            <h3 class="font-medium leading-tight text-2xl pt-4 mb-2 text-blue-600">Runner</h3>
            <div class="flex space-x-2 w-9/12 justify-end">
              {#if processing}
                <div
                  class="spinner-border animate-spin inline-block px-3 py-2.5 w-8 h-8 border-4 rounded-full text-blue-600"
                  role="status"
                >
                  <span class="visually-hidden">Loading...</span>
                </div>
              {/if}
              <input
                type="text"
                class="form-control block w-9/12 px-3 py-1.5 text-base font-normal text-gray-700 bg-gray-100 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="input"
                bind:value={$data.runner.path}
                aria-label="path to runner file"
                readonly
              />
              {#if !processing}
                <button
                  class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                  data-bs-toggle="modal"
                  data-bs-target="#edit-path-model">Edit</button
                >
                <button
                  class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                  data-bs-toggle="modal"
                  data-bs-target="#add-model">Add</button
                >
                <button
                  class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                  on:click={handleRun}>Run</button
                >
              {:else}
                <button
                  class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                  on:click={handleCancel}>Cancel</button
                >
              {/if}
              <button
                type="button"
                class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                on:click={handleClearClick}>Clear</button
              >
            </div>
          </div>

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
                      {federate.directory}
                    </code>
                  </p>
                </div>
                <div class="flex flex-col px-4 py-2 space-y-2 justify-center items-center">
                  {#if federate.status == "running"}
                    <div class="inline-block w-8 h-8 text-blue-600" role="status">
                      <Fa icon={faSync} spin="true" />
                      <span class="visually-hidden">Loading...</span>
                    </div>
                  {/if}
                  {#if federate.status == "success"}
                    <div class="inline-block w-8 h-8 text-blue-600" role="status">
                      <Fa icon={faCheckCircle} />
                    </div>
                    <button
                      class="inline-block px-6 py-2.5 w-48 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={async () => {
                        current_federate = federate;
                        await handleLog();
                      }}
                      data-bs-toggle="modal"
                      data-bs-target="#show-log-model">Show Log</button
                    >
                  {/if}
                  {#if federate.status == "failed"}
                    <div class="inline-block w-8 h-8 text-blue-600" role="status">
                      <Fa icon={faTimesCircle} />
                    </div>
                    <button
                      class="inline-block px-6 py-2.5 w-48 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={async () => {
                        current_federate = federate;
                        await handleLog();
                      }}
                      data-bs-toggle="modal"
                      data-bs-target="#show-log-model">Show Log</button
                    >
                  {/if}
                  {#if federate.status == "terminated"}
                    <div class="inline-block w-8 h-8 text-blue-600" role="status">
                      <Fa icon={faSkullCrossbones} />
                    </div>
                    <button
                      class="inline-block px-6 py-2.5 w-48 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={async () => {
                        current_federate = federate;
                        await handleLog();
                      }}
                      data-bs-toggle="modal"
                      data-bs-target="#show-log-model">Show Log</button
                    >
                  {/if}
                  {#if federate.status == "unknown"}
                    <div class="inline-block w-8 h-8 text-blue-600" role="status">
                      <Fa icon={faQuestionCircle} />
                    </div>
                  {/if}
                  {#if !processing}
                    <button
                      class="inline-block px-6 py-2.5 w-24 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={() => handleDelete(federate)}>Delete</button
                    >
                    <button
                      class="inline-block px-6 py-2.5 w-24 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={() => (current_federate = federate)}
                      data-bs-toggle="modal"
                      data-bs-target="#edit-model">Edit</button
                    >
                    <button
                      class="inline-block px-6 py-2.5 w-24 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      on:click={async () => {
                        current_federate = federate;
                        await handleLog();
                      }}
                      data-bs-toggle="modal"
                      data-bs-target="#show-log-model">Logs</button
                    >
                  {/if}
                </div>
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  </div>
</div>

<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="edit-model"
  tabindex="-1"
  aria-labelledby="edit-model-title"
  aria-modal="true"
  role="dialog"
>
  <div class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none">
    <div
      class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
    >
      <div
        class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
      >
        <h5 class="text-xl font-medium leading-normal text-gray-800" id="edit-model-label">
          Edit Job
        </h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <div class="modal-body relative p-4">
        <h5
          class="text-xl font-medium mb-2 text-blue-600 hover:text-blue-700 transition duration-300 ease-in-out"
        >
          <label>Federate Name</label>
          <input
            type="text"
            class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
            bind:value={current_federate.name}
            placeholder="Federate Name"
          />
        </h5>
        <p>
          <label>exec:</label>
          <code class="text-gray-700">
            <input
              type="text"
              class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
              bind:value={current_federate.exec}
              placeholder="Federate executable"
            />
          </code>
        </p>
        <p>
          <label>dir:</label>
          <span class="text-gray-700">
            <input
              type="text"
              class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
              bind:value={current_federate.directory}
              placeholder="Federate dir"
            />
          </span>
        </p>
      </div>
      <div
        class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"
      >
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
          data-bs-dismiss="modal"
        >
          Close
        </button>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
          data-bs-dismiss="modal"
          on:click={handleEditSaveChanges}
        >
          Save changes
        </button>
      </div>
    </div>
  </div>
</div>

<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="edit-path-model"
  tabindex="-1"
  aria-labelledby="edit-path-model-title"
  aria-modal="true"
  role="dialog"
>
  <div class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none">
    <div
      class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
    >
      <div
        class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
      >
        <h5 class="text-xl font-medium leading-normal text-gray-800" id="edit-path-model-label">
          Edit Runner Path
        </h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <div class="modal-body relative p-4">
        <p>
          <label>runner.json:</label>
          <span class="text-gray-700">
            <input
              type="text"
              class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
              bind:value={$data.runner_path}
              placeholder={$data.runner.path}
            />
          </span>
        </p>
      </div>
      <div
        class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"
      >
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
          data-bs-dismiss="modal"
        >
          Close
        </button>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
          data-bs-dismiss="modal"
          on:click={handleLoad}
        >
          Save changes
        </button>
      </div>
    </div>
  </div>
</div>

<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="add-model"
  tabindex="-1"
  aria-labelledby="add-model-title"
  aria-modal="true"
  role="dialog"
>
  <div class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none">
    <div
      class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
    >
      <div
        class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
      >
        <h5 class="text-xl font-medium leading-normal text-gray-800" id="add-model-label">
          Add Job
        </h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <div class="modal-body relative p-4">
        <h5
          class="text-xl font-medium mb-2 text-blue-600 hover:text-blue-700 transition duration-300 ease-in-out"
        >
          <label>Federate Name</label>
          <input
            type="text"
            class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
            bind:value={current_federate.name}
            placeholder="Federate Name"
          />
        </h5>
        <p>
          <label>exec:</label>
          <code class="text-gray-700">
            <input
              type="text"
              class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
              bind:value={current_federate.exec}
              placeholder="Federate executable"
            />
          </code>
        </p>
        <p>
          <label>dir:</label>
          <span class="text-gray-700">
            <input
              type="text"
              class="
              form-control
              block
              w-full
              px-3
              py-1.5
              text-base
              font-normal
              text-gray-700
              bg-white bg-clip-padding
              border border-solid border-gray-300
              rounded
              transition
              ease-in-out
              m-0
              focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
            "
              bind:value={current_federate.directory}
              placeholder="Federate dir"
            />
          </span>
        </p>
      </div>
      <div
        class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"
      >
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
          data-bs-dismiss="modal"
        >
          Close
        </button>
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
          data-bs-dismiss="modal"
          on:click={handleAdd}
        >
          Save changes
        </button>
      </div>
    </div>
  </div>
</div>

<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="show-log-model"
  tabindex="-1"
  aria-labelledby="show-log-model-title"
  aria-modal="true"
  role="dialog"
>
  <div class="modal-dialog modal-xl modal-dialog-scrollable relative w-auto pointer-events-none">
    <div
      class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
    >
      <div
        class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
      >
        <h5 class="text-xl font-medium leading-normal text-gray-800" id="show-log-model-label">
          {current_federate.name}.log
        </h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <pre class="overflow-scroll">
        <code class="text-gray-700 block whitespace-pre-wrap">
          {current_federate.log}
        </code>
      </pre>
    </div>
  </div>
</div>
