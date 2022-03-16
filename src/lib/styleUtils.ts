export function getFillColor(count: number) {
  switch (count) {
    case 0:
      return "fill-gray-200 dark:fill-gray-700";
    case 1:
      return "fill-fuchsia-200";
    case 2:
      return "fill-fuchsia-400";
    case 3:
      return "fill-fuchsia-600";
    case 4:
      return "fill-fuchsia-800";
    default:
      return "fill-fuchsia-800";
  }
}
