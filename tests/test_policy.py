import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sync_capability", ROOT / "scripts/sync_capability.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class PolicyTests(unittest.TestCase):
    def test_four_profiles_match_canonical_policy(self):
        policy = (ROOT / "shared/CAPABILITY_POLICY.md").read_text(encoding="utf-8")
        for name in sync.PROFILES:
            before = (ROOT / name).read_bytes()
            self.assertEqual(before, sync.render(before, policy), name)

    def test_check_mode_does_not_write(self):
        before = [(ROOT / name).read_bytes() for name in sync.PROFILES]
        subprocess.run([sys.executable, str(ROOT / "scripts/sync_capability.py"), "--check"], check=True)
        self.assertEqual(before, [(ROOT / name).read_bytes() for name in sync.PROFILES])

    def test_existing_text_and_crlf_are_preserved(self):
        before = b"# Existing policy\r\nDo not relax permission checks.\r\n"
        result = sync.render(before, "## New\nEvidence only.")
        self.assertTrue(result.startswith(before))
        self.assertEqual(result, sync.render(result, "## New\nEvidence only."))
        self.assertNotIn(b"\n", result.replace(b"\r\n", b""))

    def test_malformed_markers_fail_without_replacement(self):
        for text in [sync.BEGIN, sync.END, sync.END + sync.BEGIN, sync.BEGIN * 2 + sync.END * 2]:
            with self.assertRaises(ValueError):
                sync.render(text.encode(), "policy")

    def test_shared_and_agy_stay_identical(self):
        self.assertEqual((ROOT / "shared/AGENTS.md").read_bytes(), (ROOT / "agy/AGENTS.md").read_bytes())

    def test_model_preferences_preserved_without_forced_high_or_sonnet_review(self):
        for name in ["shared/AGENTS.md", "agy/AGENTS.md", "claude/CLAUDE.md"]:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("Do not use Sonnet.", text)
            self.assertNotIn("all with high effort", text)
            self.assertNotIn("then Sonnet review", text)

    def test_codex_authorization_and_model_bans_retained(self):
        text = (ROOT / "codex/AGENTS.md").read_text(encoding="utf-8")
        for phrase in ["google/gemini-4-argon", "fish-audio/transcribe-1-pro", "explicit approval", "Do not disable URL verification", "Use subagents only when"]:
            self.assertIn(phrase, text)

    def test_seven_examples_and_local_document_links(self):
        text = (ROOT / "docs/seven-principles.zh-TW.md").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"^## ([1-7])\.", text, re.M), list("1234567"))
        for name in ["README.md", "docs/seven-principles.zh-TW.md", "docs/capability-controller.md"]:
            file = ROOT / name
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", file.read_text(encoding="utf-8")):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((file.parent / target).exists(), (name, target))


if __name__ == "__main__":
    unittest.main()
