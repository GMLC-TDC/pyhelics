<script lang="ts">
  import { data } from '$lib/stores'
  import ProfilePlot from '$lib/ProfilePlot.svelte'
  import DataFlowGraph from '$lib/DataFlowGraph.svelte'
  import { onMount } from 'svelte'

  import { LayerCake } from 'layercake'
  import Dropzone from 'svelte-file-dropzone'
  const BASE = 'http://127.0.0.1:5000/api'

  let files = {
    accepted: [],
    rejected: [],
  }

  async function updateData() {
    $data.profile = await (await fetch(`${BASE}/profile`)).json()
  }

  async function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail
    files.accepted = [...files.accepted, ...acceptedFiles]
    files.rejected = [...files.rejected, ...fileRejections]
    var form = new FormData()
    form.append('file', files.accepted[0])
    await fetch(`${BASE}/profile`, {
      method: 'POST',
      body: form,
    })
    await updateData()
  }
</script>

<div class="container flex w-7/8 flex-col mt-6 mx-8">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block w-full sm:px-6 lg:px-8">
      <Dropzone on:drop={handleFilesSelect} multiple="false" />
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
