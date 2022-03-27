/**
 * @jest-environment jsdom
 */
import "@testing-library/jest-dom";
import { render } from "@testing-library/svelte";
import Tweets from "./Tweets.svelte";

describe("Tweets", () => {
  it("should", () => {
    render(Tweets);
    expect(0).toBe(0);
  });
});

export {};
