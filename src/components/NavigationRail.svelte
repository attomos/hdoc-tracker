<script lang="ts">
  import { Link, useLocation } from "svelte-navigator";
  import HomeIcon from "./HomeIcon.svelte";
  import SettingsIcon from "./SettingsIcon.svelte";

  const location = useLocation();
</script>

<div class="nav-rail">
  <Link
    class="group flex flex-col items-center rounded-sm p-3 text-sm hover:cursor-pointer hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-0 focus-visible:outline-purple-400 dark:hover:bg-gray-800 dark:focus-visible:outline-violet-600"
    to="/"
  >
    <HomeIcon active={$location.pathname === "/"} />
    <span class={$location.pathname === "/" ? "active-rail-item" : "rail-item"}
      >Home</span
    >
  </Link>
  <Link
    class="group flex flex-col items-center rounded-sm p-3 text-sm hover:cursor-pointer hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-0 focus-visible:outline-purple-400 dark:hover:bg-gray-800 dark:focus-visible:outline-violet-600"
    to="settings"
  >
    <SettingsIcon active={$location.pathname === "/settings"} />
    <span
      class={$location.pathname === "/settings"
        ? "active-rail-item"
        : "rail-item"}>Settings</span
    >
  </Link>
</div>
