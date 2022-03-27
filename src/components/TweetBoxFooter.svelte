<script lang="ts">
  import { tweets } from "../lib/stores";
  import { getExpandedEntities } from "../lib/tweetUtils";
  import type { ExpandedEntities, Tweet } from "../lib/types";
  import EntityLink from "./EntityLink.svelte";

  export let tweet: Tweet;

  let expandedEntities: ExpandedEntities;
  $: {
    expandedEntities = getExpandedEntities(tweet, $tweets);
  }
</script>

<div class="border-t border-t-gray-200 pt-2 dark:border-t-gray-500">
  <div class="flex justify-start gap-4">
    <div>
      <EntityLink expandedEntity={expandedEntities.demo}>demo</EntityLink>
    </div>
    <div>
      <EntityLink expandedEntity={expandedEntities.src}>source</EntityLink>
    </div>
    <!-- <div>
      <a class="text-purple-800 hover:underline" href="replies">replies</a>
    </div> -->
  </div>
</div>
