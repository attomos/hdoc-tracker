<script lang="ts">
  import type { Tweet } from "src/lib/types";
  import { handleTweetBoxClick } from "../components/Layout.svelte";

  export let tweet: Tweet;

  $: tweetHtmlText = tweet.text;
  $: if (tweet.entities.day_list?.length) {
    const { start, end } = tweet.entities.day_list[0];
    tweetHtmlText =
      `<mark class="bg-violet-200 text-violet-700 dark:text-violet-700 dark:bg-violet-300  p-1 rounded-sm" data-testid="mark">${tweetHtmlText.substring(
        start,
        end
      )}</mark>` + tweetHtmlText.substring(end);
  }

  const extraClass =
    tweet.conversation_id === tweet.id ? "" : "tweet-box-child";
</script>

<li role="option" on:click={handleTweetBoxClick}>
  <div class="tweet-box {extraClass}">
    {@html tweetHtmlText}
  </div>
</li>
