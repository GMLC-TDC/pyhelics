<script lang="ts">
    import Fa from "svelte-fa";
    import {faGithub} from "@fortawesome/free-brands-svg-icons";
</script>

<!-- Main navigation container -->
<nav
        class="relative flex w-full flex-nowrap items-center justify-between py-3 bg-gray-900 text-gray-200 shadow-lg hover:text-neutral-700 focus:text-neutral-700 dark:bg-neutral-600 lg:flex-wrap lg:justify-start lg:py-4"
        data-te-navbar-ref>
    <div class="flex w-full flex-wrap items-center justify-between px-3">
        <div class="ml-2 pr-3">
            <a class="text-2xl font-bold text-white dark:text-neutral-200" href="/"
            ><h2>HELICS</h2></a
            >
        </div>
        <!-- Collapsible navbar container -->
        <div
                class="!visible mt-2 flex-grow basis-[100%] items-center lg:mt-0 lg:!flex lg:basis-auto"
                id="navbarSupportedContent2"
                data-te-collapse-item>
            <!-- Left links -->
            <ul class="list-style-none mr-auto flex flex-col pl-0 lg:mt-1 lg:flex-row">
                <li class="my-4 pl-2 lg:my-0 lg:pl-2 lg:pr-2">
                    <a class="nav-link text-white" href="/">Dashboard</a>
                </li>
                <li class="my-4 pl-2 lg:my-0 lg:pl-2 lg:pr-2">
                    <a class="nav-link text-white" href="/run">Runner</a>
                </li>
                <li class="my-4 pl-2 lg:my-0 lg:pl-2 lg:pr-2">
                    <a class="nav-link text-white" href="/observe">Observer</a>
                </li>
                <li class="my-4 pl-2 lg:my-0 lg:pl-2 lg:pr-2">
                    <a class="nav-link text-white" href="/profile">Profiler</a>
                </li>
                <li class="my-4 pl-2 lg:my-0 lg:pl-2 lg:pr-2">
                    <a class="nav-link text-white" href="/broker">Broker</a>
                </li>
            </ul>

            <!-- Right elements -->
            <div class="flex space-x-2 my-4 pl-2 justify-left items-left lg:justify-center lg:items-center relative">
                <!-- Icon -->
                <a
                        class="text-white opacity-60 hover:opacity-80 focus:opacity-80"
                        target="_blank"
                        href="https://github.com/GMLC-TDC/HELICS"
                >
                    <Fa icon={faGithub}/>
                </a>
            </div>
            <!-- Right elements -->
        </div>
    </div>
</nav>
