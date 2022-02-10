<script lang="ts">
  import type { Tweet } from "src/lib/types";

  export let tweet: Tweet;
  const tweetHtmlText = tweet.text.replaceAll("\n", "<br>");

  let active = false;

  function handleFocus() {
    active = true;
  }

  function handleMouseOver() {
    active = true;
  }

  function handleMouseOut() {
    active = false;
  }
</script>

<!-- {@debug tweet} -->

<li
  role="option"
  aria-selected={active}
  on:focus={handleFocus}
  on:mouseover={handleMouseOver}
  on:mouseout={handleMouseOut}
  on:blur={handleMouseOut}
>
  {#if tweet.conversation_id === tweet.id}
    <a class="tweet-box" href="#content">
      {@html tweetHtmlText}
    </a>
  {:else}
    <a class="tweet-box tweet-box-child" href="#content">
      {@html tweetHtmlText}
    </a>
  {/if}
</li>
