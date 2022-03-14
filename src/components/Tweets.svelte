<script lang="ts">
  import { topLevelTweets } from "../lib/stores";
  import TweetBox from "./TweetBox.svelte";
</script>

<div class="mt-4 flex flex-grow flex-col overflow-auto">
  <h2 class="my-4 text-lg font-bold">{$topLevelTweets.length} tweets</h2>
  <div class="flex-grow overflow-auto pb-40">
    <ul class="mx-8 w-1/2 py-2 outline-none" role="listbox" id="tweet-list">
      {#each $topLevelTweets as tweet}
        <TweetBox {tweet} />
      {/each}
    </ul>
  </div>
</div>
