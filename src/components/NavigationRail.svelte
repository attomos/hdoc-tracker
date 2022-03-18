<script lang="ts">
  import { useLocation } from "svelte-navigator";
  import HomeIcon from "./HomeIcon.svelte";
  import NavigationRailLink from "./NavigationRailLink.svelte";
  import SettingsIcon from "./SettingsIcon.svelte";

  const location = useLocation();
  $: homeActive = $location.pathname === "/";
  $: settingsActive = $location.pathname === "/settings";
</script>

<div class="nav-rail">
  <NavigationRailLink to="/">
    <HomeIcon active={homeActive} />
    <span class:active-rail-item={homeActive} class="rail-item">Home</span>
  </NavigationRailLink>
  <NavigationRailLink to="settings">
    <SettingsIcon active={settingsActive} />
    <span class:active-rail-item={settingsActive} class="rail-item">
      Settings
    </span>
  </NavigationRailLink>
</div>
