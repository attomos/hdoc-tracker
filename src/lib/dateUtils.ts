import { formatInTimeZone } from "date-fns-tz";
import {
  add,
  endOfWeekWithOptions,
  getMonth,
  startOfWeekWithOptions,
  startOfYear,
} from "date-fns/fp";

export const DAYS = ["Mon", "Wed", "Fri", "Sun"];
export const MONTHS = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

export function getAddedDate(original: Date, days: number) {
  var date = new Date(original.valueOf());
  date.setDate(date.getDate() + days);
  return date;
}

export function getDateRange(startDate: Date, endDate: Date) {
  let dates = [];
  let currentDate = startDate;
  while (currentDate < endDate) {
    dates.push(currentDate);
    currentDate = getAddedDate(currentDate, 1);
  }
  return dates;
}

export function formatTwitterDate(twitterDate: string) {
  // UTC => UTC+7 in short ISO format
  // return new Date(twitterDate).toISOString().substring(0, 10);
  // TODO: add unit test for this
  return formatInTimeZone(new Date(twitterDate), "Asia/Bangkok", "yyyy-MM-dd");
}

export function getWeeksUntilNow() {
  const today = new Date();
  const firstMondayOfCalendar = startOfWeekWithOptions({
    weekStartsOn: 1,
  })(startOfYear(today));

  const lastSundayOfCalendar = endOfWeekWithOptions({
    weekStartsOn: 1,
  })(endOfWeekWithOptions({ weekStartsOn: 1 })(today));

  const range = getDateRange(firstMondayOfCalendar, lastSundayOfCalendar);
  const weeks = [];
  let aWeek = [];

  for (let day of range) {
    aWeek.push(formatInTimeZone(day, "Asia/Bangkok", "yyyy-MM-dd"));
    if (aWeek.length === 7) {
      weeks.push(aWeek);
      aWeek = [];
    }
  }

  return weeks;
}

export function getWeeksForThisRound(tweetDates: string[]) {
  tweetDates.sort();
  const firstDate = new Date(tweetDates[0]) || new Date();
  const firstMondayOfCalendar = startOfWeekWithOptions({
    weekStartsOn: 1,
  })(startOfYear(firstDate));

  // assuming each round tooks <= 4 months
  // TODO: take tweets data into account, doing Math.max(tweet_max_date, firstDate+4month)
  const fourMonthFromFirstDate = add({ months: 4 })(firstDate);
  console.log(fourMonthFromFirstDate);

  const lastSundayOfCalendar = endOfWeekWithOptions({
    weekStartsOn: 1,
  })(endOfWeekWithOptions({ weekStartsOn: 1 })(fourMonthFromFirstDate));

  const range = getDateRange(firstMondayOfCalendar, lastSundayOfCalendar);
  const weeks: string[][] = [];
  let aWeek: string[] = [];

  for (let day of range) {
    aWeek.push(formatInTimeZone(day, "Asia/Bangkok", "yyyy-MM-dd"));
    if (aWeek.length === 7) {
      weeks.push(aWeek);
      aWeek = [];
    }
  }

  return weeks;
}

export function getMonthString(shortDate: string) {
  const month = getMonth(new Date(shortDate));
  return MONTHS[month] || "unknown";
}
