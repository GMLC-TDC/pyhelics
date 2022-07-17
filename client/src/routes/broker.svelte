<script lang="ts">
  import Fa from "svelte-fa";
  import { faExclamationTriangle, faSync } from "@fortawesome/free-solid-svg-icons";

  import BrokerLayout from "$lib/BrokerLayout.svelte";
  import { data } from "$lib/stores";
  import { onMount, tick } from "svelte";

  let healthcheck = false;
  let brokers = [];
  let processingBrokerServer = true;
  let status = false;
  let interval = null;
  let broker_name = "Broker1";
  let broker_port = 23404;
  let broker_core_type = "zmq";
  let broker_log_level = "info";

  const PYSERVER_BASE = "http://127.0.0.1:5000/api";
  const HELICSSERVER_BASE = "http://127.0.0.1:8080";

  async function refresh() {
    await fetchHealthCheck();
    await fetchBrokerServerState();
    await fetchBrokers();
  }

  onMount(async () => {
    await refresh();
    await tick();

    processingBrokerServer = false;
    clearInterval(interval);

    interval = setInterval(async () => {
      await refresh();
      await tick();
    }, 5000);
  });

  async function fetchHealthCheck() {
    try {
      const response = await fetch(`${HELICSSERVER_BASE}/healthcheck`, {
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const r = await response.json();
      if (r) {
        healthcheck = r.success;
      }
      if (healthcheck) {
        console.log("Healthy server");
      }
    } catch {
      console.log("Unable to reach server");
      healthcheck = false;
    }
  }

  async function fetchBrokerServerState() {
    if (healthcheck) {
      const r = await (await fetch(`${PYSERVER_BASE}/broker-server`)).json();
      if (r.status) {
        status = true;
      } else {
        status = false;
      }
    } else {
      status = false;
    }
  }

  async function fetchBrokers() {
    if (healthcheck) {
      const response = await fetch(`${HELICSSERVER_BASE}/brokers`, {
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const r = await response.json();
      if (r) {
        brokers = r.brokers;
      }
    }
  }

  async function handleBrokerServerStartStopClick() {
    processingBrokerServer = true;
    const r = await (
      await fetch(`${PYSERVER_BASE}/broker-server`, {
        method: "POST",
        mode: "cors",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ status: !status }),
      })
    ).json();
    await refresh();
    processingBrokerServer = false;
  }

  async function handleBrokerServerCreateClick(broker, port, core_type, log_level) {
    if (healthcheck) {
      if (port === "" || port === null) {
        port = 23404;
      }
      var data;
      if (log_level === "info") {
        data = { broker, port, core_type };
      } else {
        data = { broker, port, log_level, core_type };
      }
      console.log(JSON.stringify({ broker, port, log_level, core_type }));
      processingBrokerServer = true;
      const r = await fetch(`${HELICSSERVER_BASE}/create`, {
        method: "POST",
        mode: "cors",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      console.log(r);
      await refresh();
      processingBrokerServer = false;
    }
  }
</script>

<div class="flex w-7/8 flex-col mt-6 mx-8">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      <div class="flex justify-between">
        <div class="flex space-x-4 items-center">
          <button
            type="button"
            data-mdb-ripple="true"
            data-mdb-ripple-color="light"
            class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            on:click={async () => await handleBrokerServerStartStopClick()}
            >{status ? "Stop" : "Start"} Broker Server</button
          >
          <Fa icon={faSync} spin={processingBrokerServer} />
        </div>
        {#if healthcheck}
          <button
            type="button"
            data-mdb-ripple="true"
            data-mdb-ripple-color="light"
            class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            data-bs-toggle="modal"
            data-bs-target="#create-broker-model">Create New Broker</button
          >
        {/if}
      </div>

      <div class="flex flex-col h-full">
        <div class="grow grid grid-areas-layout justify-items-stretch my-auto">
          {#if healthcheck}
            <div class="py-2">Server is up and running with http interface.</div>
          {/if}
        </div>

        {#if healthcheck}
          <div class="grow grid grid-areas-layout justify-items-stretch my-auto py-6">
            <div class="flex justify-center w-full">
              <ul class="bg-white rounded-lg border border-gray-200 w-full text-gray-900 py-4">
                <h4
                  class="px-6 py-2 font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600 border-b border-gray-200"
                >
                  Brokers
                </h4>
                {#each brokers as broker}
                  <li class="px-6 py-4 w-full">
                    <BrokerLayout {broker} callback={refresh} />
                  </li>
                {/each}
              </ul>
            </div>
          </div>
        {/if}
      </div>
    </div>
  </div>
</div>

<!-- create-broker-model -->
<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="create-broker-model"
  tabindex="-1"
  aria-labelledby="create-broker-model-title"
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
        <h5 class="text-xl font-medium leading-normal text-gray-800">Create Broker</h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <div class="modal-body relative p-4">
        <label for="broker-name-input" class="form-label inline-block mb-2 text-gray-700"
          >Broker Name:</label
        >
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
          id="broker-name-input"
          placeholder="broker-name"
          bind:value={broker_name}
        />
      </div>
      <div class="modal-body relative p-4">
        <label for="broker-port-input" class="form-label inline-block mb-2 text-gray-700"
          >Broker Port:</label
        >
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
          id="broker-port-input"
          placeholder="23404"
          bind:value={broker_port}
        />
      </div>
      <div class="modal-body relative p-4">
        <label for="broker-core-type-input" class="form-label inline-block mb-2 text-gray-700"
          >Broker Core Type:</label
        >
        <select
          bind:value={broker_core_type}
          id="broker-core-type-input"
          class="form-select appearance-none
            block
            w-full
            px-3
            py-1.5
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding bg-no-repeat
            border border-solid border-gray-300
            rounded
            transition
            ease-in-out
            m-0
            focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          aria-label="Core Type"
        >
          <option value="zmq">ZMQ</option>
          <option value="tcp">TCP</option>
          <option value="udp">UDP</option>
        </select>
      </div>
      <div class="modal-body relative p-4">
        <label for="broker-log-level-input" class="form-label inline-block mb-2 text-gray-700"
          >Broker Log Level:</label
        >
        <select
          bind:value={broker_log_level}
          id="broker-core-type-input"
          class="form-select appearance-none
            block
            w-full
            px-3
            py-1.5
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding bg-no-repeat
            border border-solid border-gray-300
            rounded
            transition
            ease-in-out
            m-0
            focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          aria-label="Log Level"
        >
          <option value="debug">debug</option>
          <option value="trace">trace</option>
          <option value="info">info</option>
          <option value="error">error</option>
          <option value="warning">warning</option>
          <option value="none">none</option>
          <option value="data">data</option>
          <option value="connections">connections</option>
          <option value="interfaces">interfaces</option>
          <option value="profiling">profiling</option>
          <option value="summary">summary</option>
          <option value="timing">timing</option>
        </select>
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
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md focus:outline-none focus:ring-0 transition duration-150 ease-in-out ml-1
          {broker_name !== ''
            ? 'hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 active:bg-blue-800 active:shadow-lg focus:shadow-lg'
            : 'pointer-events-none opacity-60'}"
          disabled={broker_name == ""}
          data-bs-dismiss="modal"
          on:click={async () =>
            await handleBrokerServerCreateClick(
              broker_name,
              broker_port,
              broker_core_type,
              broker_log_level,
            )}
        >
          Create
        </button>
      </div>
    </div>
  </div>
</div>
