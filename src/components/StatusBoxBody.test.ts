import { render } from "@testing-library/svelte";
import StatusBoxBody from "./StatusBoxBody.svelte";

describe("StatusBoxBody", () => {
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
      in_reply_to_id: "1",
      id: "1",
    };
    const { getByTestId, getByRole, getByText } = render(StatusBoxBody, {
      status,
    });

    // const profile = getByText("Atom Chaipreecha");
    // const username = getByText("@attomos");
    // console.log(profile);
    // console.log(username);
    // const mark = getByTestId("mark");
  });
});
