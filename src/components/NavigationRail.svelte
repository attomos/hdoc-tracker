<script lang="ts">
  import { Link, useLocation } from "svelte-navigator";
  import { getIcon } from "../lib/iconUtils";

  const location = useLocation();
</script>

<div class="nav-rail">
  <Link class="nav-rail-item" to="/">
    <div>{@html getIcon("home", $location.pathname)}</div>
    <span class={$location.pathname === "/" ? "active-rail-item" : "rail-item"}
      >Home</span
    >
  </Link>
  <Link class="nav-rail-item" to="settings">
    <div>{@html getIcon("setting-two", $location.pathname)}</div>
    <span
      class={$location.pathname === "/settings"
        ? "active-rail-item"
        : "rail-item"}>Settings</span
    >
  </Link>
</div>
