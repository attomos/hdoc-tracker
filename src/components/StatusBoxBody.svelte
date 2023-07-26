<script lang="ts">
  import type { Status } from "src/lib/types";

  export let status: Status;
  $: statusHtmlText = status.parsed_content;
  $: if (status.entities.day_list?.length) {
    const { start, end } = status.entities.day_list[0];

    statusHtmlText =
      `<mark class="pointer-events-none rounded-sm bg-violet-200 p-1 text-violet-900 dark:bg-violet-200 dark:text-violet-900" data-testid="mark">${statusHtmlText.substring(
        start,
        end
      )}</mark> ` + statusHtmlText.substring(end);
  }
</script>

<div class="whitespace-pre-wrap py-2">
  {@html statusHtmlText}
</div>
