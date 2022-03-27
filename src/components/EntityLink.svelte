<script lang="ts">
  import type { ExpandedEntity } from "../lib/types";

  export let expandedEntity: ExpandedEntity;
</script>

<a
  class={expandedEntity.href
    ? "text-violet-800 outline-none hover:underline focus-visible:underline dark:text-violet-300"
    : "text-gray-400"}
  href={expandedEntity.href || null}
  target="_blank"
>
  {#if expandedEntity.fixed}
    <slot /><span class="hover:cursor-help" title="Fixed URL">*</span>
  {:else}
    <slot />
  {/if}
</a>
