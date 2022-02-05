<script lang="ts">
  import { getDaysUntilNow as getWeeksUntilNow } from "./dateUtils";

  const array = Array(150).fill(1);

  const DAYS = ["Mon", "Wed", "Fri", "Sun"];

  // const weeks = Array(53).fill(Array(7).fill(1));
  const weeks = getWeeksUntilNow();

  const RECT_W = 10;
  const RECT_W_2 = RECT_W + 5;
  const RECT_H = 10;
  const RECT_H_2 = RECT_H + 5;
  const START_X = 36;
  const START_Y = 5;
</script>

<svg
  viewBox="0 0 900 140"
  width="900"
  height="140"
  xmlns="http://www.w3.org/2000/svg"
  class="border-2 border-black rounded-md"
>
  {#each weeks as week, i}
    <g
      class="hover2:stroke-fuchsia-300 hover2:stroke-2"
      transform="translate({i * RECT_W_2}, {START_Y})"
    >
      <rect
        class="fill-[#ccfbf1]"
        width={RECT_W + 4}
        height={RECT_H * 12}
        x={START_X - 2}
        y={RECT_H_2 - 10}
        rx="2"
      />
      {#each week as d, j}
        <rect
          class="hover:cursor-pointer fill-gray-200 hover:fill-fuchsia-300 stroke-gray-400"
          width={RECT_W}
          height={RECT_H}
          x={START_X}
          y={j * RECT_H_2 + RECT_H_2}
          rx="2"
        />
      {/each}
    </g>
  {/each}
  {#each DAYS as day, i}
    <text class="text-xs" dx="0" dy={30 + 29 * i}>{day}</text>
  {/each}
</svg>

<style>
</style>
