<script lang="ts">
  import { onMount } from "svelte";

  import { searchTerm } from "../lib/stores";
  import BurgerMenu from "./BurgerMenu.svelte";
  import CloseIcon from "./CloseIcon.svelte";
  import ListBox from "./ListBox.svelte";
  import SearchIcon from "./SearchIcon.svelte";
  import ThemeToggle from "./ThemeToggle.svelte";

  let timer: ReturnType<typeof setTimeout>;

  let showSmallSearchInput = false;

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

  function handleClick() {
    const navRail = document.querySelector(".nav-rail");
    navRail.classList.remove("hidden");
    navRail.classList.add("flex", "flex-col");

    const backdrop = document.querySelector("#backdrop");
    backdrop.classList.toggle("bg-opacity-0");
    backdrop.classList.toggle("bg-opacity-75");

    const main = document.querySelector("main");
    main.classList.add("pointer-events-none", "overflow-hidden");
  }

  function toggleSmallSearchInput() {
    showSmallSearchInput = !showSmallSearchInput;
  }

  onMount(() => {
    const mql = window.matchMedia("(min-width: 850px)");
    mql.addEventListener("change", () => {
      showSmallSearchInput = false;

      const navRail = document.querySelector(".nav-rail");
      navRail.classList.add("hidden", "xs:block");
      const backdrop = document.querySelector("#backdrop");
      backdrop.classList.remove("bg-opacity-75");
      backdrop.classList.remove("bg-opacity-0");
      backdrop.classList.add("bg-opacity-0");

      const main = document.querySelector("main");
      main.classList.remove("pointer-events-none", "overflow-hidden");
    });
  });
</script>

<nav
  class="nav-bar xs:grid-cols-4 grid min-h-[57px] {showSmallSearchInput
    ? 'grid-cols-1'
    : 'grid-cols-3'} items-center justify-between border-b border-b-gray-300 p-2 px-8 dark:border-b-gray-700"
>
  <div class={showSmallSearchInput ? "hidden" : "flex"}>
    <button on:click={handleClick} class="select-none">
      <BurgerMenu
        className="xs:hidden cursor-pointer pointer-events-auto dark:stroke-white"
      />
    </button>

    <span class="xs:block hidden dark:text-white">hdoc-tracker</span>
  </div>

  <span
    class="justify-self-center dark:text-white {showSmallSearchInput
      ? 'hidden'
      : 'xs:hidden block'} ">hdoc-tracker</span
  >

  <div
    class=" col-span-2  justify-center {showSmallSearchInput
      ? 'xs:flex flex'
      : 'xs:flex hidden'}"
  >
    <div class="relative {showSmallSearchInput ? 'w-full' : 'w-3/5 pl-4'}">
      <span
        class="pointer-events-none absolute inset-y-0 left-6 flex items-center pl-2"
        class:hidden={showSmallSearchInput}
      >
        <SearchIcon />
      </span>
      <span
        class=" absolute inset-y-0  flex cursor-pointer items-center pl-2 {showSmallSearchInput
          ? 'left-2'
          : 'left-6'}"
        class:hidden={!showSmallSearchInput}
        class:block={showSmallSearchInput}
        on:click={toggleSmallSearchInput}
      >
        <CloseIcon />
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

  <span
    class="xs:hidden block cursor-pointer justify-self-end"
    class:hidden={showSmallSearchInput}
    tabindex="0"
    on:click={toggleSmallSearchInput}
    ><SearchIcon className="dark:stroke-white" /></span
  >

  <div class="xs:flex hidden items-center justify-end gap-5">
    <ThemeToggle />
    <ListBox />
  </div>
</nav>
