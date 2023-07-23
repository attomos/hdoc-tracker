<script lang="ts">
  import { todayDate } from "../lib/stores";
  import type { Status } from "../lib/types";
  import { formatTwitterDateToShortFormat } from "../lib/dateUtils";

  export let status: Status;

  let formattedDate: string;
  let authorUrl: string;
  let tweetUrl: string;

  // TODO: hard-coded for now, until I do Cloudflare Workers thing.
  // Also see globalObjects.json
  const name = "Atom Chaipreecha";
  const username = "@attomos";

  $: {
    formattedDate = formatTwitterDateToShortFormat(
      status.created_at,
      $todayDate
    );
    authorUrl = `https://twitter.com/attomos`;
    tweetUrl = `https://twitter.com/attomos/status/${status.id}`;
  }
</script>

<div class="flex">
  <div class="flex gap-2">
    <div class="font-bold">
      <a
        class="rounded-sm outline-none hover:underline focus-visible:underline"
        href={authorUrl}
        target="_blank">{name}</a
      >
    </div>
    <div>
      <a href={authorUrl} target="_blank" tabindex="-1">{username}</a>
    </div>
  </div>
  <div class="px-1 text-gray-500 dark:text-gray-300">·</div>
  <div title="long date here">
    <a
      class="rounded-sm outline-none hover:underline focus-visible:underline"
      href={tweetUrl}
      target="_blank"
      data-testid="timestamp"
    >
      {formattedDate}
    </a>
  </div>
</div>
