<script lang="ts">
  import { createEventDispatcher } from "svelte";

  import { statuses } from "../lib/stores";
  import { getExpandedEntities } from "../lib/statusUtils";
  import type { ExpandedEntities, Status } from "../lib/types";
  import EntityLink from "./EntityLink.svelte";

  export let status: Status;
  export let replies: Status[];

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("openReply");
  }

  let expandedEntities: ExpandedEntities;
  $: {
    expandedEntities = getExpandedEntities(status, $statuses);
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
          class="text-purple-800 outline-none hover:underline focus-visible:underline dark:text-violet-300"
          on:click={handleClick}
        >
          View reply ({replies.length})
        </button>
      </div>
    {/if}
  </div>
</div>
