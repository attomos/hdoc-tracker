import { render } from "@testing-library/svelte";
import { todayDate } from "../lib/stores";
import TweetBoxHeader from "./TweetBoxHeader.svelte";

afterEach(() => {
  todayDate.set(new Date());
});

describe("TweetBoxHeader", () => {
  it("should renders correctly", () => {
    todayDate.set(new Date("2022-12-01"));
    const tweet = {
      text: "day 1 of #100DaysOfCode\ngood morning",
      entities: {
        day_list: [
          {
            start: 0,
            end: 5,
            day: "day 1",
          },
        ],
      },
      created_at: "2022-03-21T16:48:22.000Z",
      public_metrics: {
        retweet_count: 1,
        reply_count: 0,
        like_count: 1,
        quote_count: 0,
      },
      conversation_id: "1",
      id: "1",
    };
    const { getByTestId, getByText } = render(TweetBoxHeader, {
      tweet,
    });

    const profile = getByText("Atom Chaipreecha");
    const username = getByText("@attomos");
    const timestamp = getByTestId("timestamp");

    expect(profile).toBeVisible();
    expect(username).toBeVisible();
    expect(timestamp.textContent).toEqual("Mar 21");
  });

  it("should renders timestamp correctly", () => {
    todayDate.set(new Date("2023-12-01"));
    const tweet = {
      text: "day 1 of #100DaysOfCode\ngood morning",
      entities: {
        day_list: [
          {
            start: 0,
            end: 5,
            day: "day 1",
          },
        ],
      },
      created_at: "2022-03-21T16:48:22.000Z",
      public_metrics: {
        retweet_count: 1,
        reply_count: 0,
        like_count: 1,
        quote_count: 0,
      },
      conversation_id: "1",
      id: "1",
    };
    const { getByTestId, getByText } = render(TweetBoxHeader, {
      tweet,
    });

    const profile = getByText("Atom Chaipreecha");
    const username = getByText("@attomos");
    const timestamp = getByTestId("timestamp");

    expect(profile).toBeVisible();
    expect(username).toBeVisible();
    expect(timestamp.textContent).toEqual("Mar 21, 2022");
  });
});
