# SkillForge

Create shareable AI agent skill packs from a repo, docs folder, URL, or topic.

This is a minimal starter CLI that emits a skill manifest, README, and verifier prompt.

## Install

```bash
python -m pip install -e .
```

## Usage

```bash
skillforge ./some-repo --name my-skill --out dist/my-skill
skillforge "recent-context: agent skills" --name agent-skills-briefing
```

## Test

```bash
pytest
```
