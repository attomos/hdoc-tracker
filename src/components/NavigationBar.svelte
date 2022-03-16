<script lang="ts">
  import { Search } from "@icon-park/svg";
  import { searchTerm } from "../lib/stores";
  const searchSvg = Search({ theme: "outline", size: "1em" });

  let timer: ReturnType<typeof setTimeout>;

  const DEBOUNCE_DURATION = 100;

  const debounce = (e) => {
    if (e.key === "Escape") {
      e.target.blur();
      searchTerm.update((t) => e.target.value);
      return;
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      searchTerm.update((t) => e.target.value);
    }, DEBOUNCE_DURATION);
  };
</script>

<nav class="nav-bar">
  <span class="dark:text-white">hdoc-tracker</span>

  <div class="col-span-2 flex justify-center">
    <div class="relative w-3/5 pl-4">
      <span
        class="pointer-events-none absolute inset-y-0 left-6 flex items-center pl-2"
      >
        {@html searchSvg}
      </span>
      <input
        id="search-bar"
        class="search-input"
        type="text"
        placeholder="Quick search..."
        on:keyup={debounce}
      />
      <span
        class="absolute inset-y-0 right-6 my-2 flex items-center rounded-md bg-slate-200 p-2 text-purple-500"
        >/</span
      >
    </div>
  </div>

  <div class="flex justify-end">
    <select name="round" id="round" class="rounded-lg">
      <option value="r1">Round 1</option>
    </select>
  </div>
</nav>
