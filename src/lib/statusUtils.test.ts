import {
  computeStreaks,
  getExpandedEntities,
  getStatuses,
} from "./statusUtils";
import type { GroupedStatuses } from "./types";

const mockStatuses: GroupedStatuses = {
  "1234": [
    {
      entities: {},
      in_reply_to_id: "1234",
      id: "1234",
      created_at: "2022-02-19T12:15:37.000Z",
      parsed_content: "nothing",
      author_id: "2699175613",
    },
    {
      entities: {},
      in_reply_to_id: "1234",
      id: "1235",
      created_at: "2022-02-19T12:16:01.000Z",
      parsed_content: "just a comment",
      author_id: "2699175613",
    },
  ],
  "5555": [
    {
      entities: {},
      in_reply_to_id: "5555",
      id: "5555",
      created_at: "2022-02-19T12:15:37.000Z",
      parsed_content: "this is for testing yo #100DaysOfCode",
      author_id: "2699175613",
    },
    {
      entities: {
        urls: [
          {
            start: 5,
            end: 21,
            url: "https://t.co/src",
            expanded_url: "https://github.com/attomos/test",
            display_url: "github.com/attomos/test",
          },
          {
            start: 43,
            end: 59,
            url: "https://t.co/app",
            expanded_url: "https://test-attomos.vercel.app",
            display_url: "test-attomos.vercel.app",
          },
        ],
        src_list: [
          {
            start: 5,
            end: 21,
            src: "https://t.co/src",
            fixed: false,
          },
        ],
        demo_list: [
          {
            start: 43,
            end: 59,
            demo: "https://t.co/app",
            fixed: false,
          },
        ],
      },
      in_reply_to_id: "5555",
      id: "5556",
      created_at: "2022-02-19T12:16:01.000Z",
      parsed_content:
        "src: https://t.co/src #100DaysOfCode demo: https://t.co/app",
      author_id: "2699175613",
    },
  ],
  "1498337671441424384": [
    {
      entities: {
        urls: [
          {
            start: 153,
            end: 176,
            url: "https://t.co/RUdHzhtdjW",
            expanded_url: "https://hdoc-tracker.vercel.app/",
            display_url: "hdoc-tracker.vercel.app",
          },
          {
            start: 177,
            end: 200,
            url: "https://t.co/9Kl0MZgskN",
            expanded_url:
              "https://twitter.com/attomos/status/1498337671441424384/photo/1",
            display_url: "pic.twitter.com/9Kl0MZgskN",
          },
        ],
        hashtags: [{ start: 10, end: 24, tag: "100DaysOfCode" }],
        day_list: [{ day: "day 49", start: 0, end: 6 }],
        demo_list: [
          {
            demo: "https://t.co/RUdHzhtdjW",
            start: 153,
            end: 176,
            fixed: false,
          },
        ],
      },
      in_reply_to_id: "1498337671441424384",
      id: "1498337671441424384",
      created_at: "2022-02-28T16:41:53.000Z",
      parsed_content:
        "day 49 of #100DaysOfCode\n\nContinue with my progress tracker website.\n\n- Fixed days count logic\n- Added client side routing using svelte-navigator\n\ndemo: https://t.co/RUdHzhtdjW https://t.co/9Kl0MZgskN",
      author_id: "2699175613",
    },
  ],
  "1495009175201808388": [
    {
      entities: {
        urls: [
          {
            start: 82,
            end: 105,
            url: "https://t.co/xdgnwdedub",
            expanded_url: "https://codepen.io/attomos/full/PoOQLrpd",
            display_url: "codepen.io/attomos/full/P\u2026",
          },
          {
            start: 183,
            end: 206,
            url: "https://t.co/yVD7oZb9rL",
            expanded_url:
              "https://twitter.com/attomos/status/1495009175201808388/photo/1",
            display_url: "pic.twitter.com/yVD7oZb9rL",
          },
        ],
        hashtags: [{ start: 10, end: 24, tag: "100DaysOfCode" }],
        day_list: [{ day: "day 40", start: 0, end: 6 }],
        demo_list: [
          {
            demo: "https://t.co/xdgnwdedub",
            start: 82,
            end: 105,
            fixed: false,
          },
        ],
      },
      in_reply_to_id: "1495009175201808388",
      id: "1495009175201808388",
      created_at: "2022-02-19T12:15:37.000Z",
      parsed_content:
        'day 40 of #100DaysOfCode \n\n- Complete freeCodeCamp "Tribute Page" challenge\ndemo: https://t.co/xdgnwdedub\n- Add total days, longest streak, and current streak to the tracker project. https://t.co/yVD7oZb9rL',
      author_id: "2699175613",
    },
    {
      entities: {
        urls: [
          {
            start: 12,
            end: 35,
            url: "https://t.co/jLcMovxM7E",
            expanded_url: "https://codepen.io/attomos/full/PoOQLrp",
            display_url: "codepen.io/attomos/full/P\u2026",
          },
        ],
        hashtags: [{ start: 37, end: 51, tag: "100DaysOfCode" }],
        demo_list: [
          {
            demo: "https://t.co/jLcMovxM7E",
            start: 12,
            end: 35,
            fixed: true,
          },
        ],
      },
      in_reply_to_id: "1495009175201808388",
      id: "1495208706946256897",
      created_at: "2022-02-20T01:28:30.000Z",
      parsed_content: "fixed demo: https://t.co/jLcMovxM7E\n\n#100DaysOfCode",
      author_id: "2699175613",
    },
  ],
  "1483483848403202052": [
    {
      id: "1483483848403202052",
      entities: {
        hashtags: [
          { start: 10, end: 24, tag: "100DaysOfCode" },
          { start: 59, end: 73, tag: "100DaysOfCode" },
        ],
        urls: [
          {
            start: 195,
            end: 218,
            url: "https://t.co/8pHew9P6Zl",
            expanded_url: "https://github.com/attomos/hdoc-ribbon",
            display_url: "github.com/attomos/hdoc-r\u2026",
          },
          {
            start: 224,
            end: 247,
            url: "https://t.co/rk6AqGEIHx",
            expanded_url: "https://www.npmjs.com/package/hdoc-ribbon",
            display_url: "npmjs.com/package/hdoc-r\u2026",
          },
          {
            start: 281,
            end: 304,
            url: "https://t.co/GimkrJmNPr",
            expanded_url:
              "https://twitter.com/attomos/status/1483483848403202052/video/1",
            display_url: "pic.twitter.com/GimkrJmNPr",
          },
        ],
        day_list: [{ day: "day 11", start: 0, end: 6 }],
        src_list: [
          {
            src: "https://t.co/8pHew9P6Zl",
            start: 195,
            end: 218,
            fixed: false,
          },
        ],
      },
      in_reply_to_id: "1483483848403202052",
      author_id: "2699175613",
      parsed_content:
        "day 11 of #100DaysOfCode \n\nCreated a custom element to put #100DaysOfCode ribbon. It has some customizability so that you can put it in either top right or top left corner of the web page.\n\nsrc: https://t.co/8pHew9P6Zl\nnpm: https://t.co/rk6AqGEIHx\nPlease check out the demo below. https://t.co/GimkrJmNPr",
      created_at: "2022-01-18T16:58:05.000Z",
    },
  ],
  "1479514795829174274": [
    {
      id: "1479514795829174274",
      entities: {
        hashtags: [{ start: 9, end: 23, tag: "100DaysOfCode" }],
        urls: [
          {
            start: 214,
            end: 237,
            url: "https://t.co/sxheLXSxla",
            expanded_url:
              "https://github.com/attomos/100-days-of-code/tree/ec0689d204451587ba78f13915afa17f860cb7f3/days/day5",
            display_url: "github.com/attomos/100-da\u2026",
          },
          {
            start: 244,
            end: 267,
            url: "https://t.co/lmexIesDo1",
            expanded_url:
              "https://attomos.github.io/100-days-of-code/days/day5/",
            display_url: "attomos.github.io/100-days-of-co\u2026",
          },
          {
            start: 268,
            end: 291,
            url: "https://t.co/GazKrsmuJb",
            expanded_url:
              "https://twitter.com/attomos/status/1479514795829174274/photo/1",
            display_url: "pic.twitter.com/GazKrsmuJb",
          },
        ],
        annotations: [
          {
            start: 60,
            end: 71,
            probability: 0.6946,
            type: "Product",
            normalized_parsed_content: "GitHub Pages",
          },
        ],
        day_list: [{ day: "day 5", start: 0, end: 5 }],
        src_list: [
          {
            src: "https://t.co/sxheLXSxla",
            start: 214,
            end: 237,
            fixed: false,
          },
        ],
        demo_list: [
          {
            demo: "https://t.co/lmexIesDo1",
            start: 244,
            end: 267,
            fixed: false,
          },
        ],
      },
      in_reply_to_id: "1479514795829174274",
      author_id: "2699175613",
      parsed_content:
        "day 5 of #100DaysOfCode \n\nI made my 100-days-of-code repo a GitHub Pages so that all days are accessible.\n\nFor the actual project of day 5, I created a simple search form found in Tailwind CSS documentation.\n\nsrc: https://t.co/sxheLXSxla\ndemo: https://t.co/lmexIesDo1 https://t.co/GazKrsmuJb",
      created_at: "2022-01-07T18:06:30.000Z",
    },
  ],
};

describe("statusUtils", () => {
  describe("getStatuses", () => {
    it("should return correctly when the search term is found in top-level status", () => {
      const result = getStatuses(mockStatuses, "nothing");
      expect(result).toEqual({
        "1234": [
          {
            entities: {},
            in_reply_to_id: "1234",
            id: "1234",
            created_at: "2022-02-19T12:15:37.000Z",
            parsed_content: "nothing",
            author_id: "2699175613",
          },
          {
            entities: {},
            in_reply_to_id: "1234",
            id: "1235",
            created_at: "2022-02-19T12:16:01.000Z",
            parsed_content: "just a comment",
            author_id: "2699175613",
          },
        ],
      });
    });

    it("should return correctly when the search term is found in replies", () => {
      const result = getStatuses(mockStatuses, "just a comment");
      expect(result).toEqual({
        "1234": [
          {
            entities: {},
            in_reply_to_id: "1234",
            id: "1234",
            created_at: "2022-02-19T12:15:37.000Z",
            parsed_content: "nothing",
            author_id: "2699175613",
          },
          {
            entities: {},
            in_reply_to_id: "1234",
            id: "1235",
            created_at: "2022-02-19T12:16:01.000Z",
            parsed_content: "just a comment",
            author_id: "2699175613",
          },
        ],
      });
    });
  });

  describe("computeStreaks", () => {
    it("should compute streaks correctly for 0 day (no data)", () => {
      const statusesLookup = {};
      const todayDate = "2022-01-01";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([{}, {}]);
    });

    it("should compute streaks correctly for 1 day", () => {
      const statusesLookup = {
        "2022-01-01": [],
      };
      const todayDate = "2022-01-01";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 0,
          end: 0,
          count: 1,
        },
        {
          start: 0,
          end: 0,
          count: 1,
        },
      ]);
    });

    it("should compute streaks correctly for 2 days in a row (head)", () => {
      const statusesLookup = {
        "2022-01-01": [],
        "2022-01-02": [],
        "2022-01-04": [],
      };
      const todayDate = "2022-01-04";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 0,
          end: 1,
          count: 2,
        },
        {
          start: 2,
          end: 2,
          count: 1,
        },
      ]);
    });

    it("should compute streaks correctly for 2 days in a row (tail)", () => {
      const statusesLookup = {
        "2022-01-01": [],
        "2022-01-03": [],
        "2022-01-04": [],
      };
      const todayDate = "2022-01-04";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 1,
          end: 2,
          count: 2,
        },
        {
          start: 1,
          end: 2,
          count: 2,
        },
      ]);
    });

    it("should compute streaks correctly for sparse days (every other day)", () => {
      const statusesLookup = {
        "2022-01-01": [],
        "2022-01-03": [],
        "2022-01-05": [],
      };
      const todayDate = "2022-01-05";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 2,
          end: 2,
          count: 1,
        },
        {
          start: 2,
          end: 2,
          count: 1,
        },
      ]);
    });

    it("should compute streaks correctly when all streaks have number of days (3-3-3)", () => {
      const statusesLookup = {
        "2022-01-01": [],
        "2022-01-02": [],
        "2022-01-03": [],
        "2022-01-05": [],
        "2022-01-06": [],
        "2022-01-07": [],
        "2022-01-09": [],
        "2022-01-10": [],
        "2022-01-11": [],
      };
      const todayDate = "2022-01-11";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 6,
          end: 8,
          count: 3,
        },
        {
          start: 6,
          end: 8,
          count: 3,
        },
      ]);
    });

    it("should compute streaks correctly for 3 days for longest and 0 days for current", () => {
      const statusesLookup = {
        "2022-01-01": [],
        "2022-01-02": [],
        "2022-01-03": [],
      };
      const todayDate = "2022-01-05";
      const streaks = computeStreaks(statusesLookup, todayDate);
      expect(streaks).toEqual([
        {
          start: 0,
          end: 2,
          count: 3,
        },
        {},
      ]);
    });
  });

  describe("getExpandedEntities", () => {
    it("should return correctly when there's no entity at all", () => {
      const status = mockStatuses["1234"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "",
          fixed: false,
        },
        src: {
          href: "",
          fixed: false,
        },
      });
    });

    it("should return correctly when the status has fixed demo in the replies", () => {
      const status = mockStatuses["1495009175201808388"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "https://codepen.io/attomos/full/PoOQLrp",
          fixed: true,
        },
        src: {
          href: "",
          fixed: false,
        },
      });
    });

    it("should return correctly when the status has only the demo", () => {
      const status = mockStatuses["1498337671441424384"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "https://hdoc-tracker.vercel.app/",
          fixed: false,
        },
        src: {
          href: "",
          fixed: false,
        },
      });
    });

    it("should return correctly when the status has only the src", () => {
      const status = mockStatuses["1483483848403202052"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "",
          fixed: false,
        },
        src: {
          href: "https://github.com/attomos/hdoc-ribbon",
          fixed: false,
        },
      });
    });

    it("should return correctly when top level status has both demo and src", () => {
      const status = mockStatuses["1479514795829174274"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "https://attomos.github.io/100-days-of-code/days/day5/",
          fixed: false,
        },
        src: {
          href: "https://github.com/attomos/100-days-of-code/tree/ec0689d204451587ba78f13915afa17f860cb7f3/days/day5",
          fixed: false,
        },
      });
    });

    it("should return correctly when demo and src are in replies only", () => {
      const status = mockStatuses["5555"][0];
      const expandedEntities = getExpandedEntities(status, mockStatuses);
      expect(expandedEntities).toEqual({
        demo: {
          href: "https://test-attomos.vercel.app",
          fixed: false,
        },
        src: {
          href: "https://github.com/attomos/test",
          fixed: false,
        },
      });
    });
  });
});

export {};
