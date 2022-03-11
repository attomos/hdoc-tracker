import { computeStreaks } from "./tweetUtils";

describe("computeStreaks", () => {
  it("should compute streaks correctly for 0 day (no data)", () => {
    const tweetsLookup = {};
    const streaks = computeStreaks(tweetsLookup);
    expect(streaks).toEqual([{}, {}]);
  });

  it("should compute streaks correctly for 1 day", () => {
    const tweetsLookup = {
      "2022-01-01": [],
    };
    const streaks = computeStreaks(tweetsLookup);
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
    const tweetsLookup = {
      "2022-01-01": [],
      "2022-01-02": [],
      "2022-01-04": [],
    };
    const streaks = computeStreaks(tweetsLookup);
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
    const tweetsLookup = {
      "2022-01-01": [],
      "2022-01-03": [],
      "2022-01-04": [],
    };
    const streaks = computeStreaks(tweetsLookup);
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
    const tweetsLookup = {
      "2022-01-01": [],
      "2022-01-03": [],
      "2022-01-05": [],
    };
    const streaks = computeStreaks(tweetsLookup);
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
    const tweetsLookup = {
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
    const streaks = computeStreaks(tweetsLookup);
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
});

export {};
