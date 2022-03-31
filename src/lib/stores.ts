import { derived, writable } from "svelte/store";
import { getTweets } from "./tweetUtils";
import data from "../../scripts/tweets.json";

export const searchTerm = writable("");

export const todayDate = writable(new Date());

export const tweets = derived(searchTerm, ($searchTerm) =>
  getTweets(data, $searchTerm)
);

export const topLevelTweets0 = derived(tweets, ($tweets) =>
  Object.keys($tweets)
    .map((conversationId) => {
      return $tweets[conversationId].map((tweet) => {
        if (tweet.conversation_id === tweet.id) {
          return tweet;
        }
      });
    })
    .flat()
    .filter((tweet) => tweet !== undefined)
);

export const topLevelTweets = derived(
  tweets,
  ($tweets) =>
    Object.keys($tweets).map((conversationId) => {
      let rootTweet;
      let replies = [];
      $tweets[conversationId].forEach((tweet) => {
        if (tweet.conversation_id === tweet.id) {
          rootTweet = tweet;
        } else {
          replies.push(tweet);
        }
      });
      // console.log(rootTweet);
      // console.log(replies);

      return [rootTweet, replies];
    })
  // .flat()
  // .filter((tweet) => tweet !== undefined)
);
