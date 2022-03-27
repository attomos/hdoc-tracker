/**
 * @jest-environment jsdom
 */
import "@testing-library/jest-dom";
import { render } from "@testing-library/svelte";
import StyledLink from "./StyledLink.svelte";

describe("StyledLink", () => {
  it("should", () => {
    const href = "";
    render(StyledLink, {
      href,
    });
    expect(0).toBe(0);
  });
});

export {};
