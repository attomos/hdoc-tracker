require("dotenv").config();
const Redis = require("ioredis");
const tweetJson = require("../scripts/tweets.json");

const { REDIS_PASSWORD, REDIS_HOST, REDIS_PORT } = process.env;

let client = new Redis(
  `redis://:${REDIS_PASSWORD}@${REDIS_HOST}:${REDIS_PORT}`
);
// client.set("round1", JSON.stringify(tweetJson));

client.get("round1", (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
})

client.quit();
