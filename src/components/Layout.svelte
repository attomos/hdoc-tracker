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
      const ulParent = ul.parentElement;
      const ulParentRect = ulParent.getBoundingClientRect();
      const ulPaddingTop = window
        .getComputedStyle(ul, null)
        .getPropertyValue("padding-top");
      const yToScroll = rect.y - ulParentRect.y - parseFloat(ulPaddingTop);
      ulParent.scrollBy(0, yToScroll);
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

    const currentItem = getCurrentItem();

    if (!currentItem) return;

    const shouldPreventDefault =
      e.key === "ArrowDown" ||
      e.key === "j" ||
      e.key === "ArrowUp" ||
      e.key === "k" ||
      e.key === "Enter";

    if (shouldPreventDefault) {
      e.preventDefault();
    }

    let itemToFocus;
    if (e.key === "ArrowDown" || e.key === "j") {
      itemToFocus = findNextOption(currentItem);
    } else if (e.key === "ArrowUp" || e.key === "k") {
      itemToFocus = findPrevOption(currentItem);
    } else if (e.key === "Enter") {
      itemToFocus = e.target;
    }
    if (itemToFocus) {
      deselectCurrentItem(currentItem);
      focusItem(itemToFocus);
    }
  }

  function handleTweetBoxClick(e) {
    const currentItem = getCurrentItem();
    currentItem.setAttribute("aria-selected", "false");
    currentItem.classList.remove("selected");
    const listItem = e.target.closest("li");
    focusItem(listItem, false);
  }

  function handleClickAtLayout(e) {
    if (!e.target.classList.contains("tweet-box")) {
      const currentItem = getCurrentItem();
      if (!currentItem) return;
      deselectCurrentItem(currentItem);
    }
  }

  function getCurrentItem() {
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

<div class="app-layout" tabindex="0">
  <NavigationBar />
  <NavigationRail />
  <main class="mx-auto flex w-1/2 flex-col">
    <slot />
  </main>
</div>
