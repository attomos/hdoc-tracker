<script lang="ts">
  import type { Tweet } from "src/lib/types";

  export let tweet: Tweet;
  const tweetHtmlText = tweet.text.replaceAll("\n", "<br>");

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

  function focusItem(element) {
    element.setAttribute("aria-selected", "true");
    element.classList.add("focused");
    const rect = element.getBoundingClientRect();
    console.log(rect);
    console.log(element.offsetTop);
    const { y, height } = element.getBoundingClientRect();
    const ulParent = document.querySelector("#tweet-list").parentElement;
    console.log(ulParent);
    // ulParent.scrollBy(0, y - height - 80);
    // ulParent.scrollBy(0, height);
    // ulParent.scrollTo(element.offsetTop, 0);
    // ul.scrollBy()
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

    if (e.key === "ArrowDown" || e.key === "j") {
      const nextItem = findNextOption(currentItem);
      currentItem.setAttribute("aria-selected", "false");
      currentItem.classList.remove("focused");
      focusItem(nextItem);
    } else if (e.key === "ArrowUp" || e.key === "k") {
      const prevItem = findPrevOption(currentItem);
      currentItem.setAttribute("aria-selected", "false");
      currentItem.classList.remove("focused");
      focusItem(prevItem);
    }
    e.preventDefault();
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
  class={active ? "" : ""}
>
  {#if tweet.conversation_id === tweet.id}
    <a class="tweet-box" href="#content">
      {@html tweetHtmlText}
    </a>
  {:else}
    <a class="tweet-box tweet-box-child" href="#content">
      {@html tweetHtmlText}
    </a>
  {/if}
</li>
