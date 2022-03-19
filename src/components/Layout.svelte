<script context="module">
  import { onMount } from "svelte";

  function focusItem(element, shouldScroll = true) {
    if (!element.getAttribute("role")) {
      return focusItem(element.parentElement, false);
    }
    element.setAttribute("aria-selected", "true");
    element.focus();
    element.classList.add("selected");
    if (shouldScroll) {
      const rect = element.getBoundingClientRect();
      const ul = document.querySelector("#tweet-list");
      const main = document.querySelector("main");
      const ulParent = ul.parentElement;
      const ulParentRect = main.getBoundingClientRect();
      const ulPaddingTop = window
        .getComputedStyle(ulParent, null)
        .getPropertyValue("padding-top");
      const contextHeight = 250;
      const yToScroll =
        rect.y - ulParentRect.y - parseFloat(ulPaddingTop) - contextHeight;
      main.scrollBy(0, yToScroll);
    }
  }

  function findNextOption(currentOption) {
    const ul = document.querySelector("#tweet-list");
    const listItems = Array.from(ul.querySelectorAll("li"));
    const currentIndex = listItems.indexOf(currentOption);
    const nextItem =
      currentIndex + 1 < listItems.length
        ? listItems[currentIndex + 1]
        : listItems[0];
    return nextItem;
  }

  function findPrevOption(currentOption) {
    const ul = document.querySelector("#tweet-list");
    const listItems = Array.from(ul.querySelectorAll("li"));
    const currentIndex = listItems.indexOf(currentOption);
    const nextItem =
      currentIndex > 0
        ? listItems[currentIndex - 1]
        : listItems[listItems.length - 1];
    return nextItem;
  }

  function deselectCurrentItem(currentItem) {
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

    if (!currentItem) return;

    const shouldPreventDefault = e.key === "j" || e.key === "k";

    if (shouldPreventDefault) {
      e.preventDefault();
    }

    const selectedItem = document.querySelector(
      "#tweet-list li[role='option'][aria-selected='true']"
    );

    let itemToFocus;
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

  function handleTweetBoxClick(e) {
    const currentItem = getSelectedItemOrFirstChild();
    currentItem.setAttribute("aria-selected", "false");
    currentItem.classList.remove("selected");
    const listItem = e.target.closest("li");
    focusItem(listItem, false);
  }

  function handleClickAtLayout(e) {
    if (!e.target.classList.contains("tweet-box")) {
      const currentItem = getSelectedItemOrFirstChild();
      if (!currentItem) return;
      deselectCurrentItem(currentItem);
    }
  }

  function getSelectedItemOrFirstChild() {
    return (
      document.querySelector("#tweet-list li[aria-selected='true']") ||
      document.querySelector("#tweet-list li:first-child")
    );
  }

  export { handleTweetBoxClick };
</script>

<script lang="ts">
  import "../app.css";
  import NavigationBar from "./NavigationBar.svelte";
  import NavigationRail from "./NavigationRail.svelte";

  onMount(() => {
    document.addEventListener("click", handleClickAtLayout);
    document.addEventListener("keydown", handleKeyDown);
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
</div>
