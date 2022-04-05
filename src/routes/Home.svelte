<script lang="ts">
  import { loading } from "../lib/stores";

  import ActivityGraph from "../components/ActivityGraph.svelte";
  import Tweets from "../components/Tweets.svelte";
</script>

{#if $loading}
  <div class="loading">loading...</div>
{:else}
  <ActivityGraph />
  <Tweets />
{/if}
