<script lang="ts">
  import { Link, useLocation } from "svelte-navigator";
  import HomeIcon from "./HomeIcon.svelte";
  import SettingsIcon from "./SettingsIcon.svelte";

  const location = useLocation();
</script>

<div class="nav-rail">
  <Link class="nav-rail-item" to="/">
    <HomeIcon active={$location.pathname === "/"} />
    <span class={$location.pathname === "/" ? "active-rail-item" : "rail-item"}
      >Home</span
    >
  </Link>
  <Link class="nav-rail-item" to="settings">
    <SettingsIcon active={$location.pathname === "/settings"} />
    <span
      class={$location.pathname === "/settings"
        ? "active-rail-item"
        : "rail-item"}>Settings</span
    >
  </Link>
</div>
