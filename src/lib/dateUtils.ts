import {
  startOfYear,
  startOfWeekWithOptions,
  endOfWeekWithOptions,
  endOfYear,
  getMonth,
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

function getAddedDate(original: Date, days: number) {
  var date = new Date(original.valueOf());
  date.setDate(date.getDate() + days);
  return date;
}

function getDateRange(startDate: Date, endDate: Date) {
  let dates = [];
  let currentDate = startDate;
  while (currentDate < endDate) {
    dates.push(currentDate);
    currentDate = getAddedDate(currentDate, 1);
  }
  return dates;
}

function format(date: Date) {
  return date.toISOString().slice(0, 10);
}

export function formatTwitterDate(twitterDate: string) {
  // UTC => UTC+7 in short ISO format
  return new Date(twitterDate).toISOString().substring(0, 10);
}

export function getWeeksUntilNow() {
  const today = new Date();
  const firstMondayOfCalendar = startOfWeekWithOptions({
    weekStartsOn: 1,
  })(startOfYear(today));

  const lastSundayOfCalendar = endOfWeekWithOptions({
    weekStartsOn: 1,
  })(endOfYear(today));

  const range = getDateRange(firstMondayOfCalendar, lastSundayOfCalendar);
  const weeks = [];
  let aWeek = [];

  for (let day of range) {
    aWeek.push(format(day));
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
