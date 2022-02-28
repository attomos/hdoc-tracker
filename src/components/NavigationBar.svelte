<script lang="ts">
  import { Search } from "@icon-park/svg";
  const searchSvg = Search({ theme: "outline", size: "1em" });
</script>

<nav class="nav-bar">
  <span>hdoc-tracker</span>

  <div class="col-span-2 flex justify-center">
    <div class="relative w-3/5 pl-4">
      <span
        class="pointer-events-none absolute inset-y-0 left-6 flex items-center pl-2"
      >
        {@html searchSvg}
      </span>
      <input
        class="w-full rounded-lg border border-gray-400 px-4 pl-10"
        type="text"
        placeholder="Quick search..."
      />
    </div>
  </div>

  <div class="flex justify-end">
    <select name="round" id="round" class="rounded-lg">
      <option value="r1">Round 1</option>
    </select>
  </div>
</nav>
