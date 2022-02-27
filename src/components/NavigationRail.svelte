<script lang="ts">
  import { Home, DataFile } from "@icon-park/svg";

  const homeSvg = Home({ theme: "filled", size: "1.5em" });
  const dataFileSvg = DataFile({ theme: "outline", size: "1.5em" });
</script>

<div class="nav-rail">
  <a
    class="flex flex-col items-center px-4 py-2 text-sm hover:cursor-pointer"
    href="/"
  >
    <div>{@html homeSvg}</div>
    <span class="mt-2">Home</span>
  </a>
  <a
    class="flex flex-col items-center px-4 py-2 text-sm hover:cursor-pointer"
    href="/tweets"
  >
    <div>{@html dataFileSvg}</div>
    <span class="mt-2">Tweets</span>
  </a>
</div>
