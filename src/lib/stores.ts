import { derived, writable, get } from "svelte/store";
import { getStatuses } from "./statusUtils";
import type { GroupedStatuses, Status } from "./types";

export const searchTerm = writable("");
export const currentRound = writable("1");

export const loading = writable(true);
const data = writable<GroupedStatuses>({});

// const url = derived(
//   currentRound,
//   ($currentRound) =>
//     `https://hdoc-tracker.attomos.workers.dev?round=${$currentRound}`
// );

// const url = writable("http://localhost:3000/grouped.json");
const url = writable("https://hdoc-tracker.attomos.workers.dev?round=1"); // TODO: clean up this mess later

async function fetchTweets() {
  loading.set(true);
  const response = await fetch(get(url));
  const result = await response.json();

  // Cloudflare Workers is too fast, need to add some delay here...
  const resultValue = JSON.parse(result.result);
  // reverse sort resultValue by key
  const sortedResult = Object.keys(resultValue)
    .sort((a, b) => parseInt(b, 10) - parseInt(a, 10))
    .reduce((obj, key) => {
      obj[key] = resultValue[key];
      return obj;
    }, {});

  data.set(sortedResult);

  loading.set(false);
}

url.subscribe(() => fetchTweets());

export const todayDate = writable(new Date());

export const statuses = derived([data, searchTerm], ([$data, $searchTerm]) =>
  getStatuses($data, $searchTerm)
);

export const topLevelStatuses = derived(statuses, ($tweets) =>
  Object.keys($tweets).map((conversationId) => {
    let rootTweet: Status;
    let replies = [];
    $tweets[conversationId].forEach((status) => {
      if (status.in_reply_to_id === status.id) {
        rootTweet = status;
      } else {
        replies.push(status);
      }
    });

    return [rootTweet, replies];
  })
);
