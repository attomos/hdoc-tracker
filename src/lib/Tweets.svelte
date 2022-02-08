<script lang="ts">
  import { tweets } from "./stores";
</script>

<div class="my-4 flex flex-col w-4/5 flex-grow h-full">
  <h2 class="text-lg font-bold">List of tweets go here...</h2>
  <div class="overflow-scroll flex-grow">
    <ul class="list-disc ml-6 ">
      {#each $tweets.data.slice(0, 40) as tweet}
        <li class="">{tweet.text}</li>
      {/each}
    </ul>
  </div>
</div>
