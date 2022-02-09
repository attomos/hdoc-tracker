<script lang="ts">
  import { onMount } from "svelte";
  import { getWeeksUntilNow } from "../lib/dateUtils";
  import { tweets } from "../lib/stores";
  import { getFillColor } from "../lib/styleUtils";
  import { getTweetsLookupDict } from "../lib/tweetUtils";

  const DAYS = ["Mon", "Wed", "Fri", "Sun"];

  const tweetsLookup = getTweetsLookupDict($tweets);

  // const weeks = Array(53).fill(Array(7).fill(1));
  const weeks = getWeeksUntilNow().map((week) => {
    return week.map((date) => {
      return {
        date,
        count: tweetsLookup[date]?.length || 0,
      };
    });
  });

  const RECT_W = 10;
  const RECT_W_2 = RECT_W + 5;
  const RECT_H = 10;
  const RECT_H_2 = RECT_H + 5;
  const START_X = 36;
  const START_Y = 5;

  function mouseOverHandler(e: MouseEvent) {
    const date = (e.target as SVGRectElement).getAttribute("data-date");
    const tooltip = document.getElementById("tooltip");
    tooltip.innerText = date;
    tooltip.style.display = "block";
    tooltip.style.left = e.pageX - 30 + "px";
    tooltip.style.top = e.pageY - 40 + "px";

    console.log(date);
  }

  function mouseLeaveHandler() {
    const tooltip = document.getElementById("tooltip");
    tooltip.innerText = "";
    tooltip.style.display = "none";
  }

  onMount(async () => {
    const rects = document.querySelectorAll("[data-date]");
    rects.forEach((rect) => {
      // rect.addEventListener("mouseover", mouseOverHandler);
      rect.addEventListener("mousemove", mouseOverHandler);
      rect.addEventListener("mouseleave", mouseLeaveHandler);
    });
  });
</script>

<!-- {@debug weeks} -->

<!-- TODO: get year from store, updated from year navbar -->
<div>
  <h2 class="text-lg font-bold my-2">
    {$tweets.data.length} tweets in 2022
  </h2>

  <div
    id="tooltip"
    class="text-xs bg-slate-700 rounded-md text-white py-2 px-1 absolute hidden"
  >
    mock data
  </div>
  <div class="flex">
    <svg
      viewBox="0 0 862 140"
      width="862"
      height="140"
      xmlns="http://www.w3.org/2000/svg"
      class="border-2 border-black rounded-md mx-auto"
    >
      {#each weeks as week, i}
        <g
          class="hover2:stroke-fuchsia-300 hover2:stroke-2"
          transform="translate({i * RECT_W_2}, {START_Y})"
        >
          <rect
            class="fill-teal-100"
            width={RECT_W + 4}
            height={RECT_H * 12}
            x={START_X - 2}
            y={RECT_H_2 - 10}
            rx="2"
          />
          {#each week as { date, count }, j}
            <rect
              class="hover:cursor-pointer hover:ring-2 stroke-gray-400 {getFillColor(
                count
              )} stroke-gray-400 {getFillColor(count)}"
              width={RECT_W}
              height={RECT_H}
              x={START_X}
              y={j * RECT_H_2 + RECT_H_2}
              rx="2"
              data-date={date}
              data-count={count}
            />
          {/each}
        </g>
      {/each}
      {#each DAYS as day, i}
        <text class="text-xs" dx="0" dy={30 + 29 * i}>{day}</text>
      {/each}
    </svg>
  </div>
</div>
