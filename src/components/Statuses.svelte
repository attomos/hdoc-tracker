<script lang="ts">
  import { topLevelStatuses } from "../lib/stores";
  import StatusBox from "./StatusBox.svelte";
</script>

<div
  class="mx-auto mt-4 flex w-full max-w-[600px] flex-grow flex-col rounded-md py-2 outline-none sm:min-w-[600px]"
  tabindex="0"
>
  <h2 class="my-4 px-4 text-lg font-bold">{$topLevelStatuses.length} tweets</h2>
  <div class="flex-grow pb-40">
    <ul class=" mx-auto w-full p-2 outline-none" role="listbox" id="status-list">
      {#each $topLevelStatuses as [status, replies]}
        <StatusBox {status} {replies} />
      {/each}
    </ul>
  </div>
</div>
