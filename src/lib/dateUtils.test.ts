import {
  formatTwitterDate,
  formatTwitterDateToShortFormat,
  getAddedDate,
} from "./dateUtils";

describe("dateUtils", () => {
  describe("getAddedData", () => {
    beforeAll(() => {
      vi.useFakeTimers();
    });

    it("should return with days added correctly", () => {
      vi.setSystemTime(new Date("2022-03-04").getTime());
      const date = new Date("2022-02-25");
      const newDate = getAddedDate(date, 7);
      expect(newDate).toEqual(new Date());
    });

    it("should return new date with days decreased correctly", () => {
      vi.setSystemTime(new Date("2022-02-18").getTime());
      const date = new Date("2022-02-25");
      const newDate = getAddedDate(date, -7);
      expect(newDate).toEqual(new Date());
    });

    afterAll(() => {
      // Back to reality...
      vi.useRealTimers();
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

  describe("formatTwitterDateToShortFormat", () => {
    it("should format date from the same year correctly", () => {
      const twitterDate = "2022-03-21T16:48:22.000Z";
      const todayDate = new Date("2022-01-01");
      const result = formatTwitterDateToShortFormat(twitterDate, todayDate);
      expect(result).toBe("Mar 21");
    });
    it("should format date from a different year correctly", () => {
      const twitterDate = "2022-03-21T16:48:22.000Z";
      const todayDate = new Date("2024-01-01");
      const result = formatTwitterDateToShortFormat(twitterDate, todayDate);
      expect(result).toBe("Mar 21, 2022");
    });
  });
});

export {};
