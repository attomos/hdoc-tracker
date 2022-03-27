<script lang="ts">
  import { getExpandedEntities } from "../lib/tweetUtils";
  import type { ExpandedEntities, Tweet } from "../lib/types";
  import EntityLink from "./EntityLink.svelte";
  import { tweets } from "../lib/stores";

  export let tweet: Tweet;

  let expandedEntities: ExpandedEntities;
  $: {
    expandedEntities = getExpandedEntities(tweet, $tweets);
  }
</script>

<div class="border-t-[0.1px] border-t-gray-200 pt-2">
  <div class="flex justify-start gap-4">
    <div>
      <EntityLink href={expandedEntities.expandedDemoUrl}>demo</EntityLink>
    </div>
    <div>
      <EntityLink href={expandedEntities.expandedSrcUrl}>source</EntityLink>
    </div>
    <!-- <div>
      <a class="text-purple-800 hover:underline" href="replies">replies</a>
    </div> -->
  </div>
</div>
