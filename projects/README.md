# Projects Folder

This folder contains all my hands on QA and automation projects.

Each project has its own README, tests, and documentation.

## Quick Setup

To install all requirements for every project at once, from the `projects` folder run:

```bash 
pip install -r requirements.txt
```

For Playwright projects, also run:
```bash
playwright install
```

Notes: 
- Mark the `projects` folder as Sources Root in PyCharm to avoid path issues.
- Tests use Chrome by default. Selenium and Playwright handle driver installation automatically in recent versions.