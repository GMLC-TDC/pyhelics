<script lang="ts">
  type Broker = {
    address: string;
    isConnected: boolean;
    isOpen: boolean;
    isRoot: boolean;
    name: string;
  };
  export let broker: Broker = null;
  export let callback = async () => {};

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
    </p>
    <button
      type="button"
      class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
      on:click={handleBrokerDeleteClick}
    >
      Delete
    </button>
  </div>
</div>
