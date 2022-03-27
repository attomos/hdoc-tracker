module.exports = {
  transform: {
    "^.+\\.(t|j)sx?$": "@swc/jest",
    "^.+\\.svelte$": [
      "svelte-jester",
      {
        preprocess: true,
      },
    ],
    "^.+\\.css$": "jest-css-modules-transform",
  },
  moduleFileExtensions: ["js", "ts", "svelte"],
  collectCoverageFrom: [
    "src/**/*.svelte",
    "src/lib/*.ts",
    "!src/routes/*.svelte",
    "!src/App.svelte",
    "!src/components/ActivityGraph.svelte",
    "!src/icons/*.svelte",
  ],
};
