<script lang="ts">
  export let href: string;
</script>

<a
  class={href
    ? "text-violet-800 outline-none hover:underline focus-visible:underline dark:text-violet-300"
    : "text-gray-500"}
  href={href || null}
  target="_blank"><slot /></a
>
