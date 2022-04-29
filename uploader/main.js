import dotenv from "dotenv";
import { Redis } from "@upstash/redis";
import fs from "fs";

dotenv.config();

const redis = Redis.fromEnv();

(async function run() {
  const data = fs.readFileSync("../scripts/tweets.json", "utf-8");
  const res = redis.set("round1", data);
  console.log(res);
})();
