<script lang="ts">
  import { onMount } from "svelte";

  import Moon from "./Moon.svelte";
  import Sun from "./Sun.svelte";

  let themeToggle: HTMLButtonElement;

  onMount(() => {
    const body = document.querySelector("body");
    const lastSpan = themeToggle.querySelector("span:last-child");
    body.classList.remove("dark");
    const theme = localStorage.getItem("theme");
    if (theme) {
      body.classList.add(theme);
    }

    themeToggle.setAttribute(
      "aria-checked",
      theme === "dark" ? "true" : "false"
    );
    if (theme === "dark") {
      toggle(themeToggle, lastSpan);
    }
  });

  function handleClick() {
    const body = document.querySelector("body");
    body.classList.toggle("dark");

    Array.from(document.querySelectorAll(".theme-toggle")).forEach((tt) => {
      const lastSpan = tt.querySelector("span:last-child");
      const srOnly = tt.querySelector(".sr-only");

      const checked = tt.getAttribute("aria-checked");
      const newValue = checked === "true" ? "false" : "true";

      let srText = newValue === "true" ? "Disable" : "Enable";
      srOnly.innerHTML = `${srText} dark mode`;

      tt.setAttribute("aria-checked", newValue);
      localStorage.setItem("theme", newValue === "true" ? "dark" : "light");

      toggle(tt as HTMLElement, lastSpan);
    });
  }

  function toggle(switchElement: HTMLElement, lastSpan: Element) {
    const firstSun = switchElement.querySelector(".sun:nth-child(2)");
    const firstMoon = switchElement.querySelector(".moon:nth-child(3)");

    const secondSun = switchElement.querySelector(".sun:nth-child(1)");
    const secondMoon = switchElement.querySelector(".moon:nth-child(2)");

    firstSun.classList.toggle("scale-100");
    firstSun.classList.toggle("scale-0");
    firstMoon.classList.toggle("scale-100");
    firstMoon.classList.toggle("scale-0");

    lastSpan.classList.toggle("translate-x-[2.625rem]");

    secondSun.classList.toggle("opacity-0");
    secondSun.classList.toggle("opacity-100");
    secondMoon.classList.toggle("opacity-0");
    secondMoon.classList.toggle("opacity-100");
  }
</script>

<button
  class="theme-toggle relative inline-flex max-w-min items-center rounded-full bg-violet-200 py-1.5 px-2 text-violet-300 transition-colors duration-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-purple-400 focus-visible:ring-offset-2 focus-visible:ring-offset-white dark:bg-slate-700 dark:focus-visible:ring-violet-600 dark:focus-visible:ring-offset-slate-800"
  role="switch"
  type="button"
  tabindex="0"
  aria-checked="false"
  on:click={handleClick}
  bind:this={themeToggle}
>
  <span class="sr-only">Disable<!-- --> dark mode</span>
  <Sun className="transform transition-transform scale-0 duration-300" />
  <Moon
    className="ml-3.5 transform transition-transform scale-100 duration-500 text-purple-700"
  />
  <span
    class="absolute top-0.5 left-0.5 flex h-8 w-8 transform items-center justify-center rounded-full bg-white transition duration-500"
  >
    <Sun
      className="flex-none transition duration-500 transform text-purple-800 opacity-100 scale-100"
    />
    <Moon
      className="flex-none -ml-6 transition duration-500 transform text-violet-500 opacity-0 scale-100"
    />
  </span>
</button>
