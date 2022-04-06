import { derived, writable } from "svelte/store";
import { getTweets } from "./tweetUtils";
// import data from "../../scripts/tweets.json";
import type { GroupedTweets, Tweet } from "./types";

export const searchTerm = writable("");

export const loading = writable(true);
const data = writable<GroupedTweets>({});

const url = "https://hdoc-tracker.attomos.workers.dev";

async function fetchTweets() {
  const response = await fetch(url);
  const result = await response.json();

  // Cloudflare Workers is too fast, need to add some delay here...
  setTimeout(() => {
    data.set(JSON.parse(result.result));
    loading.set(false);
  }, 1000);
}

fetchTweets();

export const todayDate = writable(new Date());

export const tweets = derived([data, searchTerm], ([$data, $searchTerm]) =>
  getTweets($data, $searchTerm)
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
