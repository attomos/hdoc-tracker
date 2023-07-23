import { render } from "@testing-library/svelte";
import StatusBox from "./StatusBox.svelte";

describe("StatusBox", () => {
  it("should renders correctly", () => {
    const status = {
      parsed_content: "day 1 of #100DaysOfCode\ngood morning",
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
      in_reply_to_id: "1",
      id: "1",
    };
    const replies = [];
    const { getByTestId, getByRole } = render(StatusBox, {
      status,
      replies,
    });

    const option = getByRole("option");
    const mark = getByTestId("mark");

    expect(mark).toBeInTheDocument();
    expect(option).toHaveTextContent("day 1 of #100DaysOfCode good morning");
  });

  it("should renders without a mark for old entities data", () => {
    const status = {
      parsed_content: "day 1 of #100DaysOfCode\ngood morning",
      entities: {
        days: [
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
      in_reply_to_id: "1",
      id: "1",
    };

    const replies = [];
    const { queryByTestId, getByRole } = render(StatusBox, {
      status,
      replies,
    });

    const option = getByRole("option");
    const mark = queryByTestId("mark");

    expect(mark).not.toBeInTheDocument();
    expect(option).toHaveTextContent("day 1 of #100DaysOfCode good morning");
  });
});
