<script context="module" lang="ts">
  import Fa from 'svelte-fa/src/fa.svelte'
  import { faCaretDown, faCaretUp } from '@fortawesome/free-solid-svg-icons'
</script>

<script lang="ts">
  interface Column {
    field: string
    sortName: string
    title: string
    show: boolean
    sort: string
    sortColor: string
    sortActive: boolean
  }

  export let data = []
  export let columns: Column[] = []
  export let showAll = false
  export let N = 10

  function getPages(showAll: boolean) {
    const n = showAll ? data.length + 1 : N
    var pages = [{ number: 1, active: true }]
    for (const [index, _] of data.entries()) {
      if (index % n === 0 && index > 0) {
        pages = [...pages, { number: index / n + 1, active: false }]
      }
    }
    return pages
  }

  function selectPage(i: number) {
    for (var page of pages) {
      page.number === i ? (page.active = true) : (page.active = false)
    }
    pages = pages
  }

  $: numberElementsPerPage = showAll ? data.length + 1 : N
  $: pages = getPages(showAll)
  $: isFirstPageActive = pages.length === 1 ? true : pages[0].active
  $: isLastPageActive = pages.length === 1 ? true : pages.at(-1).active
  $: activePage = pages.findIndex((page) => page.active)

  function handleSort(column: Column) {
    for (let c of columns) {
      if (c.title == column.title) {
        if (c.sortActive) {
          c.sort = c.sort == 'ascending' ? 'descending' : 'ascending'
        }
        c.sortActive = true
      } else {
        c.sortActive = false
      }
    }
    columns = columns
    data = data
  }

  function sortData(data) {
    for (const c of columns) {
      if (c.sortActive) {
        if (c.sort == 'ascending') {
          data.sort((d1, d2) => {
            let a = d1[c.sortName]
            let b = d2[c.sortName]
            a = a == '-' ? 0 : a
            b = b == '-' ? 0 : b
            if (a < b) {
              return -1
            }
            if (a > b) {
              return 1
            }
            return 0
          })
        } else if (c.sort == 'descending') {
          data.sort((d1, d2) => {
            let a = d1[c.sortName]
            let b = d2[c.sortName]
            a = a == '-' ? 0 : a
            b = b == '-' ? 0 : b
            if (a > b) {
              return -1
            }
            if (a < b) {
              return 1
            }
            return 0
          })
        }
        break
      }
    }
    return data
  }
  $: sortData(data)
</script>

<div class="flex w-full flex-col my-2">
  <div class="flex w-full justify-between">
    <button
      on:click={(_) => (showAll = !showAll)}
      type="button"
      class="inline-block px-6 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"
    >
      {#if showAll}
        <Fa icon={faCaretUp} />
      {:else}
        <Fa icon={faCaretDown} />
      {/if}
    </button>
  </div>
</div>

<table class="table-auto w-full">
  <thead class="border-b bg-gray-800">
    <tr>
      {#each columns as column}
        <th scope="col" class="text-sm font-medium text-white px-6 py-4 text-left">
          <div class="flex">
            <span>{column.title}</span> &nbsp;
            {#if column.sort == 'ascending'}
              <button on:click={() => handleSort(column)}
                ><Fa
                  style="color: {column.sortActive ? column.sortColor : '#aaa'}"
                  icon={faCaretDown}
                /></button
              >
            {/if}
            {#if column.sort == 'descending'}
              <button on:click={() => handleSort(column)}
                ><Fa
                  style="color: {column.sortActive ? column.sortColor : '#aaa'}"
                  icon={faCaretUp}
                /></button
              >
            {/if}
          </div>
        </th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each data as row, index (row)}
      {#if index >= activePage * numberElementsPerPage && index < (activePage + 1) * numberElementsPerPage}
        <tr class="border-b hover:bg-gray-100">
          {#each columns as column}
            <td class="px-6 py-4 whitespace text-sm font-medium text-gray-900"
              >{row[column.field]}</td
            >
          {/each}
        </tr>
      {/if}
    {/each}
  </tbody>
</table>
<div class="flex w-full justify-between mb-12">
  <div class="flex justify-center">
    {#if !showAll}
      <span class="px-2 py-3"
        >Showing {N * activePage + 1} to {Math.min(N * (activePage + 1), data.length)} of
        {data.length} rows with
      </span>
      <div class="dropdown relative">
        <button
          class="
          dropdown-toggle
          px-2
          py-3
          bg-blue-600
          text-white
          font-medium
          text-xs
          leading-tight
          uppercase
          rounded
          shadow-md
          hover:bg-blue-700 hover:shadow-lg
          focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
          active:bg-blue-800 active:shadow-lg active:text-white
          transition
          duration-150
          ease-in-out
          flex
          items-center
          whitespace-nowrap
        "
          type="button"
          id="dropdownMenuButton1"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          {N} <span class="px-1" />
          <Fa icon={faCaretDown} />
        </button>
        <ul
          class="
          dropdown-menu
          min-w-max
          absolute
          bg-white
          text-base
          z-50
          float-left
          py-3
          list-none
          text-left
          rounded-lg
          shadow-lg
          mt-1
          hidden
          m-0
          bg-clip-padding
          border-none
        "
        >
          <li>
            <button
              on:click={() => (N = 10)}
              class="
              dropdown-item
              text-sm
              py-2.5
              px-6
              font-normal
              block
              w-full
              whitespace-nowrap
              bg-transparent
              text-gray-700
              hover:bg-gray-100
            ">10</button
            >
          </li>
          <li>
            <button
              on:click={() => (N = 25)}
              class="
              dropdown-item
              text-sm
              py-2.5
              px-6
              font-normal
              block
              w-full
              whitespace-nowrap
              bg-transparent
              text-gray-700
              hover:bg-gray-100
            ">25</button
            >
          </li>
        </ul>
      </div>
      <span class="px-2 py-3">rows per page.</span>
    {/if}
  </div>
  <nav aria-label="Page navigation example">
    {#if !showAll}
      <ul class="flex  list-style-none">
        <li class="page-item {isFirstPageActive ? 'disabled' : ''}">
          <button
            on:click={(_) => selectPage(1)}
            class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none text-gray-800 focus:shadow-none
            {isFirstPageActive ? 'pointer-events-none' : 'hover:text-gray-800 hover:bg-gray-200'}"
            aria-label="Previous"
          >
            <span aria-hidden="true">&laquo;</span>
          </button>
        </li>
        {#each pages as page (page)}
          <li class="page-item {page.active ? 'active' : ''}">
            <button
              on:click={(_) => selectPage(page.number)}
              class="page-link relative block py-1.5 px-3 border-0 outline-none rounded
                {page.active
                ? 'bg-blue-600 text-white hover:text-white hover:bg-blue-600 shadow-md focus:shadow-md'
                : 'bg-transparent text-gray-800 hover:text-gray-800 hover:bg-gray-200 focus:shadow-none'}
                  "
            >
              {page.number}
            </button>
          </li>
        {/each}
        <li class="page-item  {isLastPageActive ? 'disabled' : ''}">
          <button
            on:click={(_) => selectPage(pages.length)}
            class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none text-gray-800 focus:shadow-none
            {isLastPageActive ? 'pointer-events-none' : 'hover:text-gray-800 hover:bg-gray-200'}"
            aria-label="Next"
          >
            <span aria-hidden="true">&raquo;</span>
          </button>
        </li>
      </ul>
    {/if}
  </nav>
</div>
