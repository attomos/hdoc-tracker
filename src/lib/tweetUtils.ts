import { differenceInDays } from "date-fns/fp";
import data from "../../scripts/tweets.json";
import { formatTwitterDate } from "./dateUtils";
import type { GroupedTweets, TweetTuple } from "./types";

function getTweets(searchTerm: string) {
  if (searchTerm === "") return data;
  const filteredTweets = Object.entries(data).filter((e: TweetTuple) => {
    const [, value] = e;
    const ans = value
      .filter((tweet) => tweet.conversation_id === tweet.id)
      .some(({ text }: { text: string }) =>
        text.toLowerCase().includes(searchTerm.toLowerCase())
      );
    return ans;
  });

  return Object.fromEntries(filteredTweets);
}

function getTweetsLookupDict(tweets: GroupedTweets) {
  const lookup = {};
  Object.keys(tweets).forEach((key) => {
    tweets[key].forEach((tweet) => {
      const createdAt = formatTwitterDate(tweet.created_at);
      if (lookup.hasOwnProperty(createdAt)) {
        lookup[createdAt].push(tweet);
      } else {
        lookup[createdAt] = [tweet];
      }
    });
  });

  return lookup;
}

function getTweetsCount(tweets: GroupedTweets) {
  const groupCount = Object.keys(tweets).map((key) => {
    return tweets[key].length;
  }, 0);
  return groupCount.reduce((a, b) => a + b, 0);
}

function computeStreaks(tweetsLookup: any) {
  const days = Object.keys(tweetsLookup);
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

  if (streaks.length === 1) {
    return [streaks[0], streaks[0]];
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

  return [streaks[longestStreakIdx], streaks.at(-1)];
}

export { getTweets, getTweetsLookupDict, getTweetsCount, computeStreaks };
