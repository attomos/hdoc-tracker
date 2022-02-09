<script lang="ts">
  import "./app.css";
  import Tweets from "./components/Tweets.svelte";
  import ActivityGraph from "./components/ActivityGraph.svelte";
</script>

<main class="bg-teal-100">
  <div class="mx-auto flex flex-col w-1/2 h-screen">
    <ActivityGraph />
    <Tweets />
  </div>
</main>
