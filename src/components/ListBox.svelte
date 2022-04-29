<script lang="ts">
  import { currentRound } from "../lib/stores";
  import type { ListBoxItem } from "src/lib/types";

  export let data: ListBoxItem[] = [];
</script>

<select
  name="round"
  class="rounded-lg border-none border-gray-200 bg-gray-200 outline-none focus:outline-purple-400 focus:ring-white dark:bg-slate-700 dark:text-white dark:focus:outline-violet-600 dark:focus:ring-gray-700"
  bind:value={$currentRound}
>
  {#each data as item}
    <option value={item.value}>{item.text}</option>
  {/each}
</select>
