import { derived, writable } from "svelte/store";
import { getTweets } from "./tweetUtils";
import data from "../../scripts/tweets.json";
import type { Tweet } from "./types";

export const searchTerm = writable("");

export const todayDate = writable(new Date());

export const tweets = derived(searchTerm, ($searchTerm) =>
  getTweets(data, $searchTerm)
);

export const topLevelTweets = derived(tweets, ($tweets) =>
  Object.keys($tweets).map((conversationId) => {
    let rootTweet: Tweet;
    let replies = [];
    $tweets[conversationId].forEach((tweet) => {
      if (tweet.conversation_id === tweet.id) {
        rootTweet = tweet;
      } else {
        replies.push(tweet);
      }
    });

    return [rootTweet, replies];
  })
);
