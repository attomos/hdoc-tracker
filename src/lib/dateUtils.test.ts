import { formatTwitterDate, getAddedDate } from "./dateUtils";

describe("getAddedData", () => {
  beforeAll(() => {
    jest.useFakeTimers("modern"); // tell Jest to use a different timer implementation.
  });

  it("should return with days added correctly", () => {
    jest.setSystemTime(new Date("2022-03-04").getTime());
    const date = new Date("2022-02-25");
    const newDate = getAddedDate(date, 7);
    expect(newDate).toEqual(new Date());
  });

  it("should return new date with days decreased correctly", () => {
    jest.setSystemTime(new Date("2022-02-18").getTime());
    const date = new Date("2022-02-25");
    const newDate = getAddedDate(date, -7);
    expect(newDate).toEqual(new Date());
  });

  afterAll(() => {
    // Back to reality...
    jest.useRealTimers();
  });
});

describe("formatTwitterDate", () => {
  it("should return formatted date correctly (UTC+7 is preferred)", () => {
    const formatted = formatTwitterDate("2022-02-24T17:46:10.000Z");
    expect(formatted).toBe("2022-02-25");
  });
});

describe("getMonthString", () => {
  it("get month string correctly", () => {
    // const shortDates = ["20"];
  });
});

export {};
