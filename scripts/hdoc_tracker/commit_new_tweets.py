import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from github import ContentFile, Github, InputGitTreeElement, UnknownObjectException

from hdoc_tracker.utils import compare_json_string, compare_tweets

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


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


def get_paths_to_commit() -> List[Path]:
    paths_to_commit = []
    cwd = Path.cwd()
    stats_path = cwd / "stats.json"
    for round_path in cwd.glob("round*.json"):
        paths_to_commit.append(round_path)
    paths_to_commit.append(stats_path)
    return paths_to_commit


def commit_data_files(repo_id: str):
    g = Github(ACCESS_TOKEN)
    branch = "main"
    branch = "round2-support"
    repo = g.get_repo(repo_id)
    paths = get_paths_to_commit()
    git_tree_elements = []
    for path in paths:
        relative_path = path.relative_to(Path.cwd())
        print(relative_path)
        new_data = relative_path.read_text()
        should_compare = True
        try:
            contents = repo.get_contents(f"scripts/{relative_path}", ref=branch)
        except UnknownObjectException as e:
            print(e)
            print(f"Cannot find remote file for scripts/{relative_path}. Skipping...")
            should_compare = False
            contents = None

        if should_compare:
            assert isinstance(contents, ContentFile.ContentFile)
            if compare_json_string(contents.decoded_content.decode("utf-8"), new_data):
                print(f"No new data for scripts/{relative_path}. Skipping...")
                continue
        print(f"Updating {relative_path}")
        blob = repo.create_git_blob(path.read_text(), "utf-8")
        element = InputGitTreeElement(
            path=str(relative_path), mode="100644", type="blob", sha=blob.sha
        )
        git_tree_elements.append(element)
    if len(git_tree_elements) == 0:
        print("nothing to commit")
        return
    head_sha = repo.get_branch(f"{branch}").commit.sha
    base_tree = repo.get_git_tree(sha=head_sha)
    tree = repo.create_git_tree(git_tree_elements, base_tree)
    parent = repo.get_git_commit(sha=head_sha)
    commit = repo.create_git_commit(
        "try to add multiple files in one commit", tree, [parent]
    )
    ref = repo.get_git_ref(f"heads/{branch}")
    ref.edit(sha=commit.sha)


if __name__ == "__main__":
    # pp = get_paths_to_commit()
    # print(pp)
    commit_data_files("attomos/hdoc-tracker")
