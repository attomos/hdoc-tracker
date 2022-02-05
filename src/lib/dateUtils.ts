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

export function getDaysUntilNow() {
  const range = getDateRange(new Date("2022-01-01"), new Date());
  const weeks = [];
  let aWeek = [];

  for (let day of range) {
    aWeek.push(day);
    if (aWeek.length === 7) {
      weeks.push(aWeek);
      aWeek = [];
    }
  }

  return weeks;
}
