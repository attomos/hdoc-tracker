<script lang="ts">
  import "../app.css";
  import NavigationBar from "./NavigationBar.svelte";
  import NavigationRail from "./NavigationRail.svelte";
</script>

<div class="app-layout">
  <NavigationBar />
  <NavigationRail />
  <main class="mx-auto flex w-1/2 flex-col">
    <slot />
  </main>
</div>
