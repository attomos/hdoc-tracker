<script lang="ts">
  import { tweets } from "../lib/stores";
  import TweetBox from "./TweetBox.svelte";
</script>

<div class="mt-4 flex flex-grow flex-col overflow-auto">
  <h2 class="my-4 text-lg font-bold">List of tweets go here...</h2>
  <div class="flex-grow overflow-scroll pb-40">
    <ul class="mx-8 py-2" role="listbox" id="tweet-list">
      {#each Object.keys($tweets) as conversationId}
        {#each $tweets[conversationId] as tweet}
          <TweetBox {tweet} />
        {/each}
      {/each}
    </ul>
  </div>
</div>
