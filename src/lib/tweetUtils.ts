import data from "../../scripts/tweets.json";
import { formatTwitterDate } from "./dateUtils";
import type { GroupedTweets } from "./types";

function getTweets() {
  return data;
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

export { getTweets, getTweetsLookupDict, getTweetsCount };
