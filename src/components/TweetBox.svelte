<script lang="ts">
  import type { Tweet } from "src/lib/types";
  import { handleTweetBoxClick } from "../components/Layout.svelte";

  export let tweet: Tweet;

  let tweetHtmlText = tweet.text;
  if (tweet.entities.days?.length) {
    const { start, end } = tweet.entities.days[0];
    tweetHtmlText =
      `<mark class="bg-teal-300 p-1 rounded-sm">${tweetHtmlText.substring(
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
