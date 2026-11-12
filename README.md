# SiteWiki - Organization Configuration

This repository contains the shared GitHub configuration, organization profile, and automation workflows for **SiteWiki**.

## Purpose

SiteWiki is an open knowledge hub for collecting, organizing, and sharing useful websites, SEO resources, online tools, and technical knowledge.

## Repository Structure

```text
.github/
├── profile/
│   └── README.md
├── scripts/
│   └── update_repositories.py
└── workflows/
    └── update-repositories.yml
```

## Automation

We use GitHub Actions to automatically maintain the organization profile.

### Repository Directory

The repository synchronization workflow:

- Fetches public repositories from the SiteWiki organization.
- Retrieves repository descriptions, websites, topics, languages, and stars.
- Generates a repository directory.
- Updates the organization profile README automatically.

The workflow runs periodically and can also be triggered manually.

## Organization Profile

The organization profile is maintained in:

`profile/README.md`

## Contributing

Improvements to the organization configuration and automation are welcome.

Please open an issue or submit a pull request.

---

Maintained by the SiteWiki community.
