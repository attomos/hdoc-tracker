const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  darkMode: "class",
  theme: {
    extend: {},
    screens: {
      xs: "850px",
      ...defaultTheme.screens,
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
