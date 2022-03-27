<script lang="ts">
  import type { Tweet } from "../lib/types";
  import { handleTweetBoxClick } from "../components/Layout.svelte";
  import TweetBoxBody from "./TweetBoxBody.svelte";
  import TweetBoxHeader from "./TweetBoxHeader.svelte";
  import TweetBoxFooter from "./TweetBoxFooter.svelte";

  export let tweet: Tweet;

  const extraClass =
    tweet.conversation_id === tweet.id ? "" : "tweet-box-child";
</script>

<li role="option" on:click={handleTweetBoxClick}>
  <div class="tweet-box {extraClass}" tabindex="0">
    <TweetBoxHeader {tweet} />
    <TweetBoxBody {tweet} />
    <TweetBoxFooter {tweet} />
  </div>
</li>
