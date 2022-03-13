/**
 * @jest-environment jsdom
 */
import "@testing-library/jest-dom";
import { render } from "@testing-library/svelte";
import TweetBox from "./TweetBox.svelte";

describe("TweetBox", () => {
  it("should renders correctly", () => {
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
      created_at: "string",
      public_metrics: {
        retweet_count: 1,
        reply_count: 0,
        like_count: 1,
        quote_count: 0,
      },
      conversation_id: "1",
      id: "1",
    };
    const { getByTestId, getByRole } = render(TweetBox, { tweet });

    const option = getByRole("option");
    const mark = getByTestId("mark");

    expect(mark).toBeInTheDocument();

    expect(option).toHaveTextContent("day 1 of #100DaysOfCode good morning");
  });

  it("should renders without a mark for old entities data", () => {
    const tweet = {
      text: "day 1 of #100DaysOfCode\ngood morning",
      entities: {
        days: [
          {
            start: 0,
            end: 5,
            day: "day 1",
          },
        ],
      },
      created_at: "string",
      public_metrics: {
        retweet_count: 1,
        reply_count: 0,
        like_count: 1,
        quote_count: 0,
      },
      conversation_id: "1",
      id: "1",
    };
    const { queryByTestId, getByRole } = render(TweetBox, { tweet });

    const option = getByRole("option");
    const mark = queryByTestId("mark");

    expect(mark).not.toBeInTheDocument();

    expect(option).toHaveTextContent("day 1 of #100DaysOfCode good morning");
  });
});
