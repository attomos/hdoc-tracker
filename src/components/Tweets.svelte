<script lang="ts">
  import { topLevelTweets } from "../lib/stores";
  import TweetBox from "./TweetBox.svelte";
</script>

<div
  class="mx-auto mt-4 flex max-w-[600px] flex-grow flex-col rounded-md py-2 outline-none"
  tabindex="0"
>
  <h2 class="my-4 px-4 text-lg font-bold">{$topLevelTweets.length} tweets</h2>
  <div class="flex-grow pb-40">
    <ul class=" mx-auto w-full p-2 outline-none" role="listbox" id="tweet-list">
      {#each $topLevelTweets as tweet}
        <TweetBox {tweet} />
      {/each}
    </ul>
  </div>
</div>
