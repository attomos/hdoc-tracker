<script lang="ts">
  import type { Status } from "../lib/types";
  import { handleStatusBoxClick } from "./Layout.svelte";
  import StatusBoxBody from "./StatusBoxBody.svelte";
  import StatusBoxHeader from "./StatusBoxHeader.svelte";
  import StatusBoxFooter from "./StatusBoxFooter.svelte";

  export let status: Status;
  export let replies: Status[];
  export let hideFooter = false;

  let hideReply = true;
  function handleRepliesClick(e: CustomEvent) {
    hideReply = !hideReply;
    e.stopPropagation();
  }

  const isRootStatus =
    status.in_reply_to_id === null || status.in_reply_to_id === status.id;

  const extraClass = isRootStatus ? "" : "status-box-child";
</script>

<li role="option" on:click={handleStatusBoxClick}>
  <div class="status-box {extraClass}" tabindex="0">
    <StatusBoxHeader {status} />
    <StatusBoxBody {status} />
    {#if !hideFooter}
      <StatusBoxFooter {status} {replies} on:openReply={handleRepliesClick} />
    {/if}
  </div>
</li>

<div class:hidden={hideReply} class="mt-4">
  {#each replies as reply}
    <svelte:self status={reply} replies={[]} hideFooter={true} />
  {/each}
</div>
