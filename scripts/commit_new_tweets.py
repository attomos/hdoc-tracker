import json
import os
from pathlib import Path

from dotenv import load_dotenv
from github import ContentFile, Github

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def compare_tweets(old_tweets_text, new_tweets_text):
    old_json = json.loads(old_tweets_text)
    new_json = json.loads(new_tweets_text)

    old_count = 0
    new_count = 0
    for k, v in old_json.items():
        old_count += len(v)

    for k, v in new_json.items():
        new_count += len(v)
    return old_count == new_count


def update_tweets_and_commit(repo_id: str):
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(repo_id)
    contents = repo.get_contents("scripts/tweets.json", ref="main")
    new_tweets = Path("./tweets.json").read_text()

    assert isinstance(contents, ContentFile.ContentFile)
    print("Comparing local tweets.json with the remote file")
    if compare_tweets(contents.decoded_content.decode("utf-8"), new_tweets):
        print("No new tweets. Skipping...")
    else:
        print("Updating scripts/tweets.json")

        commit = repo.update_file(
            contents.path,
            "chore: update tweets.json (automated)",
            new_tweets,
            contents.sha,
            branch="main",
        )
        print(commit)


if __name__ == "__main__":
    update_tweets_and_commit("attomos/hdoc-tracker")
