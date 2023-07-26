<script context="module" lang="ts">
  import { onMount } from "svelte";

  let dialogRef;

  function focusItem(element, shouldScroll = true) {
    if (!element.getAttribute("role")) {
      return focusItem(element.parentElement, false);
    }
    element.setAttribute("aria-selected", "true");
    element.focus();
    element.classList.add("selected");
    if (shouldScroll) {
      const rect = element.getBoundingClientRect();
      const ul = document.querySelector("#status-list");
      const main = document.querySelector("main");
      const ulParent = ul.parentElement;
      const ulParentRect = main.getBoundingClientRect();
      const ulPaddingTop = window
        .getComputedStyle(ulParent, null)
        .getPropertyValue("padding-top");
      const contextHeight = element.previousElementSibling
        ? element.previousElementSibling.clientHeight
        : 0;

      const yToScroll =
        rect.y - ulParentRect.y - parseFloat(ulPaddingTop) - contextHeight - 24;
      main.scrollBy(0, yToScroll);
    }
  }

  function findNextOption(currentOption: HTMLLIElement): HTMLLIElement {
    const ul = document.querySelector("#status-list");
    const listItems = Array.from(ul.querySelectorAll("li"));
    const currentIndex = listItems.indexOf(currentOption);
    const nextItem =
      currentIndex + 1 < listItems.length
        ? listItems[currentIndex + 1]
        : listItems[0];
    return nextItem;
  }

  function findPrevOption(currentOption: HTMLLIElement): HTMLLIElement {
    const ul = document.querySelector("#status-list");
    const listItems = Array.from(ul.querySelectorAll("li"));
    const currentIndex = listItems.indexOf(currentOption);
    const nextItem =
      currentIndex > 0
        ? listItems[currentIndex - 1]
        : listItems[listItems.length - 1];
    return nextItem;
  }

  function deselectCurrentItem(currentItem: HTMLLIElement) {
    currentItem.setAttribute("aria-selected", "false");
    currentItem.classList.remove("selected");
  }

  function handleKeyDown(e) {
    if (e.target.matches("input")) {
      return;
    }

    const currentItem = getSelectedItemOrFirstChild();

    if (e.key === "/") {
      document.getElementById("search-bar").focus();

      if (currentItem) {
        deselectCurrentItem(currentItem);
      }
      e.preventDefault();
      return;
    }

    if (e.key === "?") {
      if (dialogRef.open) {
        dialogRef.close();
      } else {
        dialogRef.showModal();
      }
      e.preventDefault();
      return;
    }

    if (dialogRef.open) {
      return;
    }

    if (!currentItem) return;

    const shouldPreventDefault = e.key === "j" || e.key === "k";

    if (shouldPreventDefault) {
      e.preventDefault();
    }

    const selectedItem = document.querySelector(
      "#status-list li[role='option'][aria-selected='true']"
    );

    let itemToFocus: HTMLLIElement;
    if (e.key === "j" && !selectedItem) {
      focusItem(currentItem);
      return;
    } else if (e.key === "j") {
      itemToFocus = findNextOption(currentItem);
    } else if (e.key === "k") {
      itemToFocus = findPrevOption(currentItem);
    }
    if (itemToFocus) {
      deselectCurrentItem(currentItem);
      focusItem(itemToFocus);
    }
  }

  function handleStatusBoxClick(e: MouseEvent) {
    if (!(e.target instanceof Element)) return;
    if (e.target.matches("a")) {
      return;
    }
    const currentItem = getSelectedItemOrFirstChild();
    currentItem.setAttribute("aria-selected", "false");
    currentItem.classList.remove("selected");
    const listItem = e.target.closest("li");
    focusItem(listItem, false);
  }

  function handleClickAtLayout(e: MouseEvent) {
    if (e.target instanceof Element && !e.target.closest(".status-box")) {
      const currentItem = getSelectedItemOrFirstChild();
      if (!currentItem) return;
      deselectCurrentItem(currentItem);
    }
  }

  function getSelectedItemOrFirstChild(): HTMLLIElement {
    return (
      document.querySelector("#status-list li[aria-selected='true']") ||
      document.querySelector("#status-list li:first-child")
    );
  }

  export { handleStatusBoxClick };
</script>

<script lang="ts">
  import "../app.css";
  import NavigationBar from "./NavigationBar.svelte";
  import NavigationRail from "./NavigationRail.svelte";
  import StyledKbd from "./StyledKbd.svelte";

  onMount(() => {
    document.addEventListener("click", handleClickAtLayout);
    document.addEventListener("keydown", handleKeyDown);
    const dialog: any = document.querySelector("dialog"); // use any for now, until this is fixed https://github.com/microsoft/TypeScript/issues/48267

    dialog.addEventListener("click", function onClick(e: MouseEvent) {
      if (e.target === dialog) {
        dialog.DOCUMENT_FRAGMENT_NODE;
        dialog.close();
      }
    });
  });
</script>

<div class="app-layout">
  <div
    id="backdrop"
    class="pointer-events-none fixed inset-0 z-20 bg-gray-500 bg-opacity-0 transition-opacity"
    aria-hidden="true"
  />
  <NavigationBar />
  <NavigationRail />
  <main class="flex flex-col overflow-y-scroll">
    <slot />
  </main>

  <div
    class="xs:grid fixed bottom-8 right-16 hidden h-8 w-8 cursor-pointer select-none place-content-center rounded-full bg-white text-2xl ring ring-gray-200 drop-shadow-md hover:ring-purple-400 dark:bg-black dark:text-white dark:ring-gray-700 dark:hover:ring-violet-600"
    on:click={dialogRef.showModal()}
  >
    ?
  </div>
</div>

<dialog
  class="rounded-lg ring ring-purple-400 dark:bg-black dark:text-white dark:ring-violet-600"
  bind:this={dialogRef}
>
  <div class="px-8 py-2">
    <h2
      class="mb-8 border-b-2 border-b-purple-400 pb-4 text-4xl dark:border-b-violet-600"
    >
      Keyboard shortcuts
    </h2>
    <div class="flex flex-col gap-3">
      <div>
        <StyledKbd>j</StyledKbd>
        <span>Select next status</span>
      </div>
      <div>
        <StyledKbd>k</StyledKbd>
        <span>Select previous status</span>
      </div>
      <div>
        <StyledKbd>/</StyledKbd>
        <span>Focus searchbar</span>
      </div>
      <div>
        <StyledKbd>?</StyledKbd>
        <span>Toggle keyboard shortcuts dialog</span>
      </div>
    </div>
  </div>
</dialog>
