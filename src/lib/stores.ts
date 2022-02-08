import { readable } from "svelte/store";
import { getTweets } from "./tweetUtils";

export const tweets = readable(getTweets());
