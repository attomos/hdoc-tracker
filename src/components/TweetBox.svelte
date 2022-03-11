<script lang="ts">
  import type { Tweet } from "src/lib/types";

  export let tweet: Tweet;

  let tweetHtmlText = tweet.text;
  if (tweet.entities.days?.length) {
    const { start, end } = tweet.entities.days[0];
    tweetHtmlText =
      `<mark class="bg-teal-300 p-1 rounded-sm">${tweetHtmlText.substring(
        start,
        end
      )}</mark>` + tweetHtmlText.substring(end);
  }

  // export let tweet;
  // const tweetHtmlText = tweet.text.replaceAll("\n", "<br>") + tweet.idx;

  let active = false;

  function handleFocus() {
    active = true;
  }

  function handleMouseOver() {
    active = true;
  }

  function handleMouseOut() {
    active = false;
  }

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

  function handleKeyDown(e) {
    const currentItem =
      document.querySelector("#tweet-list li[aria-selected='true']") ||
      document.querySelector("#tweet-list li[aria-selected]:first-child");

    const shouldPreventDefault =
      e.key === "ArrowDown" ||
      e.key === "j" ||
      e.key === "ArrowUp" ||
      e.key === "k" ||
      e.key === "Enter";

    if (shouldPreventDefault) {
      e.preventDefault();
    }

    function deselectCurrentItem() {
      currentItem.setAttribute("aria-selected", "false");
      currentItem.classList.remove("selected");
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
      deselectCurrentItem();
      focusItem(itemToFocus);
    }
  }

  function handleClick(e) {
    const currentItem =
      document.querySelector("#tweet-list li[aria-selected='true']") ||
      document.querySelector("#tweet-list li[aria-selected]:first-child");

    currentItem.setAttribute("aria-selected", "false");
    currentItem.classList.remove("selected");
    const listItem = e.target.closest("li");
    focusItem(listItem, false);
  }
</script>

<!-- {@debug tweet} -->
<!-- on:mouseout={handleMouseOut} -->
<!-- on:focus={handleFocus}
on:mouseover={handleMouseOver}
on:blur={handleMouseOut}
 -->

<li
  role="option"
  aria-selected={active}
  on:keydown={handleKeyDown}
  on:click={handleClick}
  class={active ? "" : ""}
>
  <div
    class="tweet-box {tweet.conversation_id === tweet.id
      ? ''
      : 'tweet-box-child'}"
    tabindex="0"
  >
    {@html tweetHtmlText}
  </div>
</li>
