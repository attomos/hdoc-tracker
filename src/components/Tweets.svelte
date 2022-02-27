<script lang="ts">
  import { tweets } from "../lib/stores";
  import TweetBox from "./TweetBox.svelte";

  // TODO: refactor this ugly code please
  const topLevelTweets = Object.keys($tweets)
    .map((conversationId) => {
      return $tweets[conversationId].map((tweet) => {
        if (tweet.conversation_id === tweet.id) {
          return tweet;
        }
      });
    })
    .flat()
    .filter((tweet) => tweet !== undefined);
</script>

<!-- {@debug topLevelTweets} -->
<!-- {@debug $tweets} -->

<div class="mt-4 flex flex-grow flex-col overflow-auto">
  <h2 class="my-4 text-lg font-bold">List of tweets go here...</h2>
  <div class="flex-grow overflow-auto pb-40">
    <ul class="mx-8 w-1/2 py-2" role="listbox" id="tweet-list">
      {#each topLevelTweets as tweet}
        <TweetBox {tweet} />
      {/each}
      <!-- {#each Object.keys($tweets) as conversationId}
        {#each $tweets[conversationId] as tweet}
          <TweetBox {tweet} />
        {/each}
      {/each} -->
    </ul>
  </div>
</div>
