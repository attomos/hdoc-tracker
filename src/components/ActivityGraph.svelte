<script lang="ts">
  import type { Tweet } from "src/lib/types";

  import { onMount } from "svelte";
  import {
    DAYS,
    getMonthString,
    getWeeksUntilNow,
    MONTHS,
  } from "../lib/dateUtils";
  import { tweets } from "../lib/stores";
  import { getFillColor } from "../lib/styleUtils";
  import {
    computeStreaks,
    getTweetsCount,
    getTweetsLookupDict,
  } from "../lib/tweetUtils";

  const tweetsLookup = getTweetsLookupDict($tweets);
  const daysCount = Object.keys(tweetsLookup)
    .map((key) => {
      return tweetsLookup[key].filter((tweet: Tweet) => {
        return tweet.text.includes("of #100DaysOfCode");
      });
    })
    .flat().length;
  const tweetsCount = getTweetsCount($tweets);

  const [longestStreak, currentStreak] = computeStreaks(tweetsLookup);

  const weeks = getWeeksUntilNow().map((week) => {
    return week.map((date) => {
      return {
        date,
        count: tweetsLookup[date]?.length || 0,
        month: getMonthString(date),
      };
    });
  });

  const GAP = 3;
  const RECT_W = 10;
  const RECT_W_2 = RECT_W + GAP;
  const RECT_H = 10;
  const RECT_H_2 = RECT_H + GAP;
  const START_X = 36;
  const START_Y = 6;

  function mouseOverHandler(e: MouseEvent) {
    const [date, count] = [
      (e.target as SVGRectElement).getAttribute("data-date"),
      parseInt((e.target as SVGRectElement).getAttribute("data-count"), 10),
    ];
    const tooltip = document.getElementById("tooltip");
    if (count > 0) {
      tooltip.innerText = `${count} tweets on ${date}`;
    } else {
      tooltip.innerText = `No tweets on ${date}`;
    }

    tooltip.style.display = "block";
    tooltip.style.left = e.pageX - 30 + "px";
    tooltip.style.top = e.pageY - 40 + "px";
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
    const activityGraph = document.querySelector("#activities-graph");
    const groups = activityGraph.querySelectorAll("g");
    const firstGroup = activityGraph.querySelector("g");

    function appendDays() {
      const rectsInFirstGroup = firstGroup.querySelectorAll("rect[data-date]");
      let j = 0;
      const { top: svgTop } = activityGraph.getBoundingClientRect();
      rectsInFirstGroup.forEach((rect, i) => {
        if (i % 2 == 0) {
          const { x, y, top } = rect.getBoundingClientRect();
          const text = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
          );
          text.classList.add("text-[9px]", "dark:fill-white");
          text.setAttribute("dx", "4");
          text.setAttribute("dy", `${top - svgTop + RECT_W_2 - 5}`);
          text.innerHTML = DAYS[j];
          activityGraph.appendChild(text);
          j++;
        }
      });
    }

    function appendMonths() {
      const columns = Array.from(groups).map((group) => {
        const dataMonths = Array.from(
          group.querySelectorAll("rect[data-date]")
        ).map((rect) => rect.getAttribute("data-month"));
        return [...new Set(dataMonths)];
      });
      let currentIndex = 0;
      const answer = [];
      columns.forEach((column, columnIndex) => {
        if (column.includes(MONTHS[currentIndex])) {
          const text = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
          );
          text.classList.add("text-[9px]", "dark:fill-white");
          text.setAttribute("dx", `${36 + RECT_W_2 * columnIndex}`);
          text.setAttribute("dy", "10");
          text.innerHTML = MONTHS[currentIndex];
          activityGraph.appendChild(text);
          answer.push(columnIndex);
          currentIndex++;
        }
      });
    }

    appendDays();
    appendMonths();
  });
</script>

<!-- {@debug weeks} -->

<!-- TODO: get year from store, updated from year navbar -->
<div>
  <h2 class="my-2 text-lg font-bold">
    {tweetsCount} tweets in 2022
  </h2>

  <div
    id="tooltip"
    class="absolute hidden rounded-md bg-slate-700 py-2 px-1 text-xs text-white dark:bg-slate-500"
  >
    mock data
  </div>
  <div class="flex flex-col">
    <svg
      viewBox="0 0 862 126"
      width="862"
      height="126"
      xmlns="http://www.w3.org/2000/svg"
      class="mx-auto min-w-max rounded-md border-2 border-gray-200 dark:border-gray-700"
      id="activities-graph"
    >
      {#each weeks as week, i}
        <g
          class="hover2:stroke-fuchsia-300 hover2:stroke-2"
          transform="translate({i * RECT_W_2}, {START_Y})"
        >
          <rect
            class="fill-white dark:fill-[#15141a]"
            width={RECT_W + 4}
            height={RECT_H * 8 + GAP * 8}
            x={START_X - 2}
            y={RECT_H_2 - 8}
            rx="2"
          />
          {#each week as { date, month, count }, j}
            <rect
              class="stroke-gray-400 hover:cursor-pointer hover:ring-2 dark:stroke-gray-600 {getFillColor(
                count
              )}"
              width={RECT_W}
              height={RECT_H}
              x={START_X}
              y={j * RECT_H_2 + RECT_H_2}
              rx="2"
              data-date={date}
              data-month={month}
              data-count={count}
            />
          {/each}
        </g>
      {/each}
    </svg>

    <div class="mx-auto mt-4 flex gap-x-16">
      <div>
        <span class="font-bold">Total days:</span>
        {daysCount}
      </div>
      <div>
        <span class="font-bold">Longest streak:</span>
        {longestStreak.count}
      </div>
      <div>
        <span class="font-bold">Current streak:</span>
        {currentStreak.count}
      </div>
    </div>
  </div>
</div>
