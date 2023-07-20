import { render } from "@testing-library/svelte";
import TweetBoxBody from "./TweetBoxBody.svelte";

describe("TweetBoxBody", () => {
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
    const { getByTestId, getByRole, getByText } = render(TweetBoxBody, {
      tweet,
    });

    // const profile = getByText("Atom Chaipreecha");
    // const username = getByText("@attomos");
    // console.log(profile);
    // console.log(username);
    // const mark = getByTestId("mark");
  });
});
