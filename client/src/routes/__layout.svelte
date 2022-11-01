<script>
  import '../app.css'
  import { browser } from '$app/env'
  import { onMount } from 'svelte'
  import Navbar from '$lib/Navbar.svelte'
  onMount(async () => {
    if (browser) {
      await import('tw-elements')
    }
  })
</script>

<svelte:head>
  <title>HELICS Web Interface</title>
</svelte:head>

<div class="h-screen w-screen grid">
  <Navbar />
  <main class="container mx-auto">
    <slot />
  </main>
</div>

<style>
  div {
    grid-template-rows: auto 1fr;
  }
</style>
