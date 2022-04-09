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
  let burgerMenuTabindex = -1;

  const DEBOUNCE_DURATION = 100;

  const debounce = (e: KeyboardEvent) => {
    const target = e.target as HTMLInputElement;
    if (e.key === "Escape") {
      target.blur();
      searchTerm.update((t) => target.value);
      return;
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      searchTerm.update((t) => target.value);
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
    burgerMenuTabindex = mql.matches ? -1 : 0;
    mql.addEventListener("change", (e) => {
      burgerMenuTabindex = e.matches ? -1 : 0;
      console.log(burgerMenuTabindex);
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
  class="nav-bar grid min-h-[57px] xs:grid-cols-4 {showSmallSearchInput
    ? 'grid-cols-1'
    : 'grid-cols-3'} items-center justify-between border-b border-b-gray-300 p-2 px-8 dark:border-b-gray-700"
>
  <div class={showSmallSearchInput ? "hidden" : "flex"}>
    <button
      on:click={handleClick}
      class="select-none rounded-md outline-none focus-visible:ring-2 focus-visible:ring-purple-400 dark:focus-visible:ring-violet-600"
      tabindex={burgerMenuTabindex}
    >
      <BurgerMenu
        className="xs:hidden cursor-pointer pointer-events-auto dark:stroke-white"
      />
    </button>

    <span class="hidden dark:text-white xs:block">
      <a class="decoration-slate-300 hover:underline" href="/">hdoc-tracker</a>
    </span>
    <span class="hidden dark:text-white xs:block">
      &nbsp;by <a
        class="decoration-slate-300 hover:underline"
        href="https://twitter.com/attomos"
        target="_blank">@attomos</a
      >
    </span>
  </div>

  <span
    class="justify-self-center dark:text-white {showSmallSearchInput
      ? 'hidden'
      : 'block xs:hidden'} ">hdoc-tracker</span
  >

  <div
    class=" col-span-2  justify-center {showSmallSearchInput
      ? 'flex xs:flex'
      : 'hidden xs:flex'}"
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
        class="w-full rounded-lg border-none px-4 pl-12 text-gray-500 outline-none ring-2 ring-gray-200 focus:ring-2 focus:ring-purple-400 dark:bg-black dark:text-white dark:caret-white dark:ring-gray-700 dark:placeholder:text-gray-400 dark:focus:ring-violet-600"
        type="text"
        placeholder="Quick search..."
        on:keyup={debounce}
      />
      <span
        class="absolute inset-y-0 right-6 my-2 flex items-center rounded-md bg-slate-200 p-2 text-purple-700 dark:bg-slate-700 dark:text-violet-200"
        >/</span
      >
    </div>
  </div>

  <button
    class="block cursor-pointer justify-self-end rounded-md outline-none focus-visible:ring-2 focus-visible:ring-purple-400 dark:focus-visible:ring-violet-600 xs:hidden"
    class:hidden={showSmallSearchInput}
    on:click={toggleSmallSearchInput}
    ><SearchIcon className="dark:stroke-white" /></button
  >

  <div class="hidden items-center justify-end gap-5 xs:flex">
    <ThemeToggle />
    <ListBox />
  </div>
</nav>
