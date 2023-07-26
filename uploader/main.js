import dotenv from "dotenv";
import { Redis } from "@upstash/redis";
import fs from "fs";

dotenv.config();

const redis = Redis.fromEnv();

(async function run() {
  const data = fs.readFileSync("../scripts/round2.json", "utf-8");
  const res = redis.json.set("round2", "$", data);
  console.log(res);
})();
