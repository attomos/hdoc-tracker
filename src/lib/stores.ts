import { derived, writable, get } from "svelte/store";
import { getStatuses } from "./statusUtils";
import type { GroupedStatuses, Status } from "./types";

export const searchTerm = writable("");
export const currentRound = writable("2");

export const loading = writable(true);
const data = writable<GroupedStatuses>({});

const url = derived(
  currentRound,
  ($currentRound) =>
    `https://hdoc-tracker.attomos.workers.dev?round=${$currentRound}`
);

function replaceSomeUnicode(text: string) {
  // TODO: find a better name for this function
  const regex = /\\U([0-9a-fA-F]{8})/g;

  // Function to replace the matched \U sequences with the equivalent JavaScript Unicode sequences
  function replaceUnicode(match, p1) {
    const hexValue = parseInt(p1, 16);
    return String.fromCodePoint(hexValue);
  }

  return text.replace(regex, replaceUnicode);
}

async function fetchTweets() {
  loading.set(true);
  const response = await fetch(get(url));
  const result = await response.text();

  const tmp = JSON.parse(replaceSomeUnicode(result));
  const resultValue = JSON.parse(tmp.result);
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
      if (
        status.in_reply_to_id === null ||
        status.in_reply_to_id === status.id
      ) {
        rootTweet = status;
      } else {
        replies.push(status);
      }
    });

    return [rootTweet, replies];
  })
);
