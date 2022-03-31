<script lang="ts">
  import { tweets } from "../lib/stores";
  import { getExpandedEntities } from "../lib/tweetUtils";
  import type { ExpandedEntities, Tweet } from "../lib/types";
  import EntityLink from "./EntityLink.svelte";
  import TweetBox from "./TweetBox.svelte";

  export let tweet: Tweet;
  export let replies: Tweet[];

  let hideReply = true;

  let expandedEntities: ExpandedEntities;
  $: {
    expandedEntities = getExpandedEntities(tweet, $tweets);
  }

  function handleRepliesClick(e: MouseEvent) {
    hideReply = !hideReply;
    e.stopPropagation();
  }
</script>

<div class="border-t border-t-gray-200 pt-2 dark:border-t-gray-500">
  <div class="flex justify-between">
    <div class="flex gap-4">
      <div>
        <EntityLink expandedEntity={expandedEntities.demo}>demo</EntityLink>
      </div>
      <div>
        <EntityLink expandedEntity={expandedEntities.src}>source</EntityLink>
      </div>
    </div>
    {#if replies.length > 0}
      <div>
        <button
          class="text-purple-800 hover:underline"
          on:click={handleRepliesClick}
        >
          View reply ({replies.length})
        </button>
      </div>
    {/if}
  </div>
</div>

<div class:hidden={hideReply}>
  {#each replies as reply}
    <TweetBox tweet={reply} replies={[]} hideFooter={true} />
  {/each}
</div>
