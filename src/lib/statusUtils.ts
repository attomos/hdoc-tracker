import { differenceInDays } from "date-fns/fp";

import type {
  Demo,
  ExpandedEntities,
  GroupedStatuses,
  Src,
  Status,
  StatusTuple,
  StatusUrl,
} from "./types";
import { formatTwitterDate } from "./dateUtils";

function getStatuses(tweets: GroupedStatuses, searchTerm: string) {
  if (searchTerm === "") return tweets;
  const filteredTweets = Object.entries(tweets).filter((e: StatusTuple) => {
    const [, value] = e;
    const ans = value.some(({ parsed_content }: { parsed_content: string }) =>
      parsed_content.toLowerCase().includes(searchTerm.toLowerCase())
    );
    return ans;
  });

  return Object.fromEntries(filteredTweets);
}

function getTweetEntity<T>(
  tweets: GroupedStatuses,
  tweetId: string,
  entity: string
): T[] {
  if (!tweets[tweetId]) return [];
  return (
    tweets[tweetId].map((reply) => reply.entities[entity] ?? []).flat() || []
  );
}

export function getExpandedEntities(
  status: Status,
  groupedStatuses: GroupedStatuses
): ExpandedEntities {
  const allUrls = getTweetEntity<StatusUrl>(groupedStatuses, status.id, "urls");
  const demoList = getTweetEntity<Demo>(
    groupedStatuses,
    status.id,
    "demo_list"
  );
  const srcList = getTweetEntity<Src>(groupedStatuses, status.id, "src_list");
  const latestDemo = demoList?.at(-1);
  const latestSrc = srcList?.at(-1);
  const expandedDemo = allUrls.find((url) => url.url === latestDemo?.demo);
  const expandedSrc = allUrls.find((url) => url.url === latestSrc?.src);

  const demo = {
    href: expandedDemo?.expanded_url ?? "",
    fixed: latestDemo?.fixed ?? false,
  };
  const src = {
    href: expandedSrc?.expanded_url ?? "",
    fixed: latestSrc?.fixed ?? false,
  };

  return {
    demo,
    src,
  };
}

function getStatusesLookupDict(grouped: GroupedStatuses) {
  const lookup = {};
  Object.keys(grouped).forEach((key) => {
    grouped[key].forEach((status) => {
      const createdAt = formatTwitterDate(status.created_at);
      if (lookup.hasOwnProperty(createdAt)) {
        lookup[createdAt].push(status);
      } else {
        lookup[createdAt] = [status];
      }
    });
  });

  return lookup;
}

function getStatusesCount(tweets: GroupedStatuses) {
  const groupCount = Object.keys(tweets).map((key) => {
    return tweets[key].length;
  }, 0);
  return groupCount.reduce((a, b) => a + b, 0);
}

function computeStreaks(statusesLookup: any, todayDate: string) {
  const days = Object.keys(statusesLookup);
  days.sort();

  if (days.length === 0) {
    return [{}, {}];
  }
  const streaks = [];
  let start = 0;
  let end = 0;
  let currentStreak = { start, end, count: 1 };
  let previousDate = new Date(days[start]);
  if (days.length === 1) {
    streaks.push(currentStreak);
  }

  for (end = 1; end < days.length; end++) {
    const date = new Date(days[end]);
    const diff = differenceInDays(previousDate, date);
    previousDate = date;
    if (diff === 1) {
      currentStreak = {
        ...currentStreak,
        end,
        count: currentStreak.count + 1,
      };
      if (end === days.length - 1) {
        streaks.push(currentStreak);
      }
    } else {
      streaks.push(currentStreak);
      currentStreak = {
        start: end,
        end,
        count: 1,
      };
      if (end === days.length - 1) {
        streaks.push(currentStreak);
      }
    }
  }

  let longestStreak = -1;
  let longestStreakIdx = 0;
  for (let i = 0; i < streaks.length; i++) {
    const streak = streaks[i];
    if (streak.count >= longestStreak) {
      longestStreak = streak.count;
      longestStreakIdx = i;
    }
  }

  if (days.at(-1) !== todayDate) {
    return [streaks[longestStreakIdx], {}];
  }

  if (streaks.length === 1) {
    return [streaks[0], streaks[0]];
  }

  return [streaks[longestStreakIdx], streaks.at(-1)];
}

export { getStatuses, getStatusesLookupDict, getStatusesCount, computeStreaks };
