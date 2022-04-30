<script lang="ts">
  export let href: string;
  export let target = "_blank";
</script>

<a
  class="font-semibold text-violet-800 underline dark:text-violet-400"
  {href}
  {target}
>
  <slot />
</a>
