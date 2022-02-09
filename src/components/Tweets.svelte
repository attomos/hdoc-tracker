<script lang="ts">
  import { tweets } from "../lib/stores";
</script>

<div class="mt-4 flex flex-col flex-grow overflow-scroll">
  <h2 class="text-lg font-bold my-4">List of tweets go here...</h2>
  <div class="flex-grow overflow-scroll pb-40">
    <ul class="list-disc ml-6 ">
      {#each $tweets.data as tweet}
        <li class="">{tweet.text}</li>
      {/each}
    </ul>
  </div>
</div>
