import json

from skillforge.main import main


def test_smoke_generates_skill(tmp_path):
    out = tmp_path / "skill"
    assert main(["recent-context: agent skills", "--name", "agent-skills", "--out", str(out)]) == 0

    manifest = json.loads((out / "skill.json").read_text())
    assert manifest["name"] == "agent-skills"
    assert manifest["permissions"]["network"] is True
    assert (out / "README.md").exists()
    assert (out / "verifier.md").exists()
