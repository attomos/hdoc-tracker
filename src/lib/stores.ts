import { derived, readable, writable } from "svelte/store";
import { getTweets } from "./tweetUtils";

export const searchTerm = writable("");

export const todayDate = readable(new Date());

export const tweets = derived(searchTerm, ($searchTerm) =>
  getTweets($searchTerm)
);

export const topLevelTweets = derived(tweets, ($tweets) =>
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
