<script lang="ts">
  import { Link } from "svelte-navigator";
  export let to: string;
</script>

<Link
  class="group xs:flex-col xs:gap-0 flex items-center gap-3 rounded-sm p-3 text-sm hover:cursor-pointer hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-0 focus-visible:outline-purple-400 dark:hover:bg-gray-800 dark:focus-visible:outline-violet-600"
  on:click
  {to}
>
  <slot />
</Link>
