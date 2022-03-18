<script lang="ts">
  import { searchTerm } from "../lib/stores";
  import SearchIcon from "./SearchIcon.svelte";
  import ThemeToggle from "./ThemeToggle.svelte";

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
        <SearchIcon />
      </span>
      <input
        id="search-bar"
        class="w-full rounded-lg border-none px-4 pl-12 text-gray-500 outline-none ring-2 ring-gray-200 focus:ring-2 focus:ring-purple-400 dark:bg-[#15141a] dark:text-white dark:caret-white dark:ring-gray-700 dark:placeholder:text-gray-400 dark:focus:ring-violet-600"
        type="text"
        placeholder="Quick search..."
        on:keyup={debounce}
      />
      <span
        class="absolute inset-y-0 right-6 my-2 flex items-center rounded-md bg-slate-200 p-2 text-purple-500 dark:bg-slate-700 dark:text-violet-300"
        >/</span
      >
    </div>
  </div>

  <div class="flex items-center justify-end gap-5">
    <ThemeToggle />
    <select
      name="round"
      id="round"
      class="rounded-lg border-none border-gray-200 bg-gray-200 outline-none focus:outline-purple-400 focus:ring-white dark:bg-slate-700 dark:text-white dark:focus:outline-violet-600 dark:focus:ring-gray-700"
    >
      <option value="r1">Round 1</option>
    </select>
  </div>
</nav>
