import {
  startOfYear,
  startOfWeekWithOptions,
  endOfWeekWithOptions,
  endOfYear,
} from "date-fns/fp";

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
