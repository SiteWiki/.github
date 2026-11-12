
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ORG = "SiteWiki"
README = Path("profile/README.md")

START = "<!-- REPOSITORIES:START -->"
END = "<!-- REPOSITORIES:END -->"


def fetch_repositories():
    repos = []
    page = 1
    token = os.getenv("GITHUB_TOKEN")

    while True:
        params = urlencode({
            "type": "public",
            "sort": "updated",
            "direction": "desc",
            "per_page": 100,
            "page": page,
        })

        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        request = Request(
            f"https://api.github.com/orgs/{ORG}/repos?{params}",
            headers=headers,
        )

        with urlopen(request) as response:
            data = json.loads(response.read())

        if not data:
            break

        repos.extend(data)
        page += 1

    return [
        repo for repo in repos
        if repo["name"] != ".github"
    ]


def generate_markdown(repos):
    if not repos:
        return "_No public repositories found yet._"

    lines = []

    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        description = (
            repo.get("description") or "No description provided."
        ).replace("|", "\\|").replace("\n", " ")

        language = repo.get("language") or "Other"
        stars = repo.get("stargazers_count", 0)

        lines.append(
            f"- 📦 **[{name}]({url})** — {description}  \n"
            f"  ` {language} ` ⭐ {stars}"
        )

    return "\n".join(lines)


def update_readme(content):
    readme = README.read_text(encoding="utf-8")

    start = readme.find(START)
    end = readme.find(END)

    if start == -1 or end == -1 or end < start:
        raise ValueError("Repository markers not found in README.")

    updated = (
        readme[:start + len(START)]
        + "\n\n"
        + content
        + "\n\n"
        + readme[end:]
    )

    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    repositories = fetch_repositories()
    markdown = generate_markdown(repositories)
    update_readme(markdown)

    print(f"Updated {len(repositories)} repositories.")
