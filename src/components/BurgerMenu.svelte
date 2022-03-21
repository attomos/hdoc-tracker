<script lang="ts">
  export let className: string;
</script>

<svg
  xmlns="http://www.w3.org/2000/svg"
  class="h-6 w-6 rounded-md {className}"
  fill="none"
  viewBox="0 0 24 24"
  stroke="currentColor"
  stroke-width="2"
  on:click
>
  <path
    stroke-linecap="round"
    stroke-linejoin="round"
    d="M4 6h16M4 12h16M4 18h16"
  />
</svg>
