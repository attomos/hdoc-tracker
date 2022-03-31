<script lang="ts">
  import type { Tweet } from "../lib/types";
  import { handleTweetBoxClick } from "../components/Layout.svelte";
  import TweetBoxBody from "./TweetBoxBody.svelte";
  import TweetBoxHeader from "./TweetBoxHeader.svelte";
  import TweetBoxFooter from "./TweetBoxFooter.svelte";

  export let tweet: Tweet;
  export let replies: Tweet[];
  export let hideFooter = false;

  let hideReply = true;
  function handleRepliesClick(e: CustomEvent) {
    hideReply = !hideReply;
    e.stopPropagation();
  }

  const extraClass =
    tweet.conversation_id === tweet.id ? "" : "tweet-box-child";
</script>

<li role="option" on:click={handleTweetBoxClick}>
  <div class="tweet-box {extraClass}" tabindex="0">
    <TweetBoxHeader {tweet} />
    <TweetBoxBody {tweet} />
    {#if !hideFooter}
      <TweetBoxFooter {tweet} {replies} />
    {/if}
  </div>
</li>
