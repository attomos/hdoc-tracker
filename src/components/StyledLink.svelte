<script lang="ts">
  export let href: string;
  export let target = "_blank";
</script>

<a
  class="font-semibold text-purple-400 underline dark:text-violet-500"
  {href}
  {target}
>
  <slot />
</a>
