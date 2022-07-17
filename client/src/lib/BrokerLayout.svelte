<script lang="ts">
  type Broker = {
    address: string;
    isConnected: boolean;
    isOpen: boolean;
    isRoot: boolean;
    name: string;
  };
  export let broker: Broker = {};
  export let callback = async () => {};
  export let broker_barrier_time = null;
  let is_broker_barrier_time_set = false;

  const PYSERVER_BASE = "http://127.0.0.1:5000/api";
  const HELICSSERVER_BASE = "http://127.0.0.1:8080";

  async function handleBrokerDeleteClick() {
    if (broker) {
      const r = await fetch(`${HELICSSERVER_BASE}/${broker.name}`, {
        method: "DELETE",
        mode: "cors",
      });
    }
    await callback();
  }

  async function handleBrokerBarrierSet(time) {
    const r = await fetch(`${HELICSSERVER_BASE}/${broker.name}/barrier`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ time }),
    });
    await callback();
    if (r.status == 200) {
      is_broker_barrier_time_set = true;
    } else {
      console.log(r);
    }
  }

  async function handleBrokerBarrierClear() {
    const r = await fetch(`${HELICSSERVER_BASE}/${broker.name}/barrier`, {
      method: "DELETE",
      mode: "cors",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
    });
    await callback();
    if (r.status == 200) {
      is_broker_barrier_time_set = false;
    } else {
      console.log(r);
    }
  }
</script>

<div class="flex justify-center">
  <div class="block p-6 border border-gray-200 bg-white w-full">
    <h5 class="text-gray-900 text-xl leading-tight font-medium mb-2">Name: {broker.name}</h5>
    <p class="text-gray-700 text-base mb-4">
      Address: {broker.address}
      <br />
      Is Connected: {broker.isConnected}
      <br />
      Is Open: {broker.isOpen}
      <br />
      Is Root: {broker.isRoot}
      <br />
      {#if is_broker_barrier_time_set && broker_barrier_time != null && broker_barrier_time != undefined}
        Barrier Time: {broker_barrier_time}
      {/if}
    </p>
    <div class="flex space-x-2">
      <button
        type="button"
        class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
        on:click={handleBrokerDeleteClick}
      >
        Delete
      </button>
      {#if is_broker_barrier_time_set}
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          on:click={handleBrokerBarrierClear}
        >
          Clear Barrier
        </button>
      {:else}
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          data-bs-toggle="modal"
          data-bs-target="#broker-set-barrier-model"
        >
          Set Barrier
        </button>
      {/if}
    </div>
  </div>
</div>

<div
  class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
  id="broker-set-barrier-model"
  tabindex="-1"
  aria-labelledby="broker-set-barrier-model-title"
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
        <h5
          class="text-xl font-medium leading-normal text-gray-800"
          id="broker-set-barrier-model-label"
        >
          Modal title
        </h5>
        <button
          type="button"
          class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
          data-bs-dismiss="modal"
          aria-label="Close"
        />
      </div>
      <div class="modal-body relative p-4">
        <label for="broker-barrier-time-input" class="form-label inline-block mb-2 text-gray-700"
          >Broker Barrier Time:</label
        >
        <input
          type="number"
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
          id="broker-barrier-time-input"
          placeholder="0"
          bind:value={broker_barrier_time}
        />
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
          {broker_barrier_time != null
            ? 'hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 active:bg-blue-800 active:shadow-lg focus:shadow-lg'
            : 'pointer-events-none opacity-60'}"
          data-bs-dismiss="modal"
          disabled={broker_barrier_time == null}
          on:click={() => handleBrokerBarrierSet(broker_barrier_time)}
        >
          Set Barrier
        </button>
      </div>
    </div>
  </div>
</div>
