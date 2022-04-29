import { derived, writable, get } from "svelte/store";
import { getTweets } from "./tweetUtils";
import type { GroupedTweets, Tweet } from "./types";

export const searchTerm = writable("");
export const currentRound = writable("1");

export const loading = writable(true);
const data = writable<GroupedTweets>({});

const url = derived(
  currentRound,
  ($currentRound) =>
    `https://hdoc-tracker.attomos.workers.dev?round=${$currentRound}`
);

async function fetchTweets() {
  loading.set(true);
  const response = await fetch(get(url));
  const result = await response.json();

  // Cloudflare Workers is too fast, need to add some delay here...
  setTimeout(() => {
    data.set(JSON.parse(result.result));
    loading.set(false);
  }, 300);
}

url.subscribe(() => fetchTweets());

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
