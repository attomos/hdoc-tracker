import data from "../../scripts/tweets.json";
import { formatTwitterDate } from "./dateUtils";
import type { TweetResponse } from "./types";

function getTweets() {
  return data;
}

function getTweetsLookupDict(tweets: TweetResponse) {
  const lookup = {};
  tweets.data.forEach((tweet) => {
    const createdAt = formatTwitterDate(tweet.created_at);
    if (lookup.hasOwnProperty(createdAt)) {
      lookup[createdAt].push(tweet);
    } else {
      lookup[createdAt] = [tweet];
    }
  });
  return lookup;
}

export { getTweets, getTweetsLookupDict };
