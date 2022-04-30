<script lang="ts">
  import { useLocation } from "svelte-navigator";
  import { clickOutside } from "../lib/clickOutside";
  import AboutIcon from "./AboutIcon.svelte";
  import CloseIcon from "./CloseIcon.svelte";
  import HomeIcon from "./HomeIcon.svelte";
  import ListBox from "./ListBox.svelte";
  import NavigationRailLink from "./NavigationRailLink.svelte";
  import SettingsIcon from "./SettingsIcon.svelte";
  import ThemeToggle from "./ThemeToggle.svelte";

  const location = useLocation();
  $: homeActive = $location.pathname === "/";
  $: settingsActive = $location.pathname === "/settings";
  $: aboutActive = $location.pathname === "/about";

  function closeNavMenu() {
    const navRail = document.querySelector(".nav-rail");
    const backdrop = document.querySelector("#backdrop");
    const main = document.querySelector("main");

    if (backdrop.classList.contains("bg-opacity-75")) {
      navRail.classList.add("hidden", "xs:block");
      navRail.classList.remove("block");

      backdrop.classList.toggle("bg-opacity-0");
      backdrop.classList.toggle("bg-opacity-75");

      main.classList.remove("pointer-events-none", "overflow-hidden");
    }
  }
</script>

<div class="nav-rail " use:clickOutside on:clickOutside={closeNavMenu}>
  <div>
    <div
      class="h-[57px] border-b border-b-gray-300 pt-4 dark:border-b-gray-700 xs:hidden"
    >
      <button
        class="ml-8 mb-8 flex content-center rounded-md outline-none focus-visible:ring-2 focus-visible:ring-purple-400 dark:focus-visible:ring-violet-600 xs:mx-auto"
        on:click={closeNavMenu}
      >
        <CloseIcon />
      </button>
    </div>
    <NavigationRailLink to="/" on:click={closeNavMenu}>
      <HomeIcon className={homeActive ? "active-rail-icon" : "rail-icon"} />
      <div class:active-rail-item={homeActive} class="rail-item">Home</div>
    </NavigationRailLink>
    <NavigationRailLink to="about" on:click={closeNavMenu}>
      <AboutIcon className={aboutActive ? "active-rail-icon" : "rail-icon"} />
      <span class:active-rail-item={aboutActive} class="rail-item">
        About
      </span>
    </NavigationRailLink>
    <NavigationRailLink to="settings" on:click={closeNavMenu}>
      <SettingsIcon
        className={settingsActive ? "active-rail-icon" : "rail-icon"}
      />
      <span class:active-rail-item={settingsActive} class="rail-item">
        Settings
      </span>
    </NavigationRailLink>
  </div>

  <div class="h-1/3">
    <div class="flex flex-col gap-8 p-3 xs:hidden">
      <ThemeToggle />
      <ListBox />
    </div>
  </div>
</div>
