<script lang="ts">
  import "./app.css";
  import Tweets from "./lib/Tweets.svelte";
  import ActivityGraph from "./lib/ActivityGraph.svelte";
</script>

<main class="bg-teal-100">
  <div class="flex h-screen">
    <div class="mx-auto">
      <Tweets />
      <ActivityGraph />
    </div>
  </div>
</main>
