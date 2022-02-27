<script lang="ts">
  import "./app.css";
  import Tweets from "./components/Tweets.svelte";
  import ActivityGraph from "./components/ActivityGraph.svelte";
  import NavigationRail from "./components/NavigationRail.svelte";
  import NavigationBar from "./components/NavigationBar.svelte";
</script>

<div class="app-layout">
  <NavigationBar />
  <NavigationRail />
  <main class="mx-auto flex w-1/2 flex-col">
    <ActivityGraph />
    <Tweets />
  </main>
</div>
