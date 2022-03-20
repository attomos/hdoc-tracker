<script lang="ts">
  export let href: string;
  export let target = "_blank";
</script>

<a
  class="px-1 font-semibold text-violet-800 underline dark:text-violet-400"
  {href}
  {target}
>
  <slot />
</a>
