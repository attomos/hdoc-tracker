<script lang="ts">
  import type { Tweet } from "src/lib/types";

  export let tweet: Tweet;
  $: tweetHtmlText = tweet.text;
  $: if (tweet.entities.day_list?.length) {
    const { start, end } = tweet.entities.day_list[0];

    tweetHtmlText =
      `<mark class="pointer-events-none rounded-sm bg-violet-200 p-1 text-violet-900 dark:bg-violet-200 dark:text-violet-900" data-testid="mark">${tweetHtmlText.substring(
        start,
        end
      )}</mark> ` + tweetHtmlText.substring(end);
  }
</script>

<div class="whitespace-pre-wrap py-2">
  {@html tweetHtmlText}
</div>
