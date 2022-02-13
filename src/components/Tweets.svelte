<script lang="ts">
  import { tweets } from "../lib/stores";
  import TweetBox from "./TweetBox.svelte";
</script>

<div class="mt-4 flex flex-col flex-grow overflow-auto">
  <h2 class="text-lg font-bold my-4">List of tweets go here...</h2>
  <div class="flex-grow overflow-scroll pb-40">
    <ul class="mx-8 py-2" role="listbox" id="tweet-list">
      <!-- {#each $tweets.data.slice(0, 10) as tweet, idx}
        <TweetBox
          tweet={{ text: "something short", conversation_id: 1, id: 1, idx }}
        />
      {/each} -->
      {#each $tweets.data as tweet}
        <TweetBox {tweet} />
      {/each}
    </ul>
  </div>
</div>
