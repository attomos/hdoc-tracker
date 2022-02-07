import data from "../../scripts/tweets.json";
import { formatTwitterDate } from "./dateUtils";
import type { TweetResponse } from "./types";

function getTweets() {
  return data;
}

function getTweetsCounter(tweets: TweetResponse) {
  const counter = {};
  tweets.data.forEach((tweet) => {
    const createdAt = formatTwitterDate(tweet.created_at);
    if (counter.hasOwnProperty(createdAt)) {
      counter[createdAt]++;
    } else {
      counter[createdAt] = 1;
    }
  });
  return counter;
}

export { getTweets, getTweetsCounter };
