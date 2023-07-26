<script lang="ts">
  import { loading } from "../lib/stores";

  import ActivityGraph from "../components/ActivityGraph.svelte";
  import Tweets from "../components/Statuses.svelte";
  import Loading from "../components/Loading.svelte";
</script>

{#if $loading}
  <Loading />
{:else}
  <ActivityGraph />
  <Tweets />
{/if}
