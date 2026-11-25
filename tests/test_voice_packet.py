"""Offline routing/packaging regressions; no model-generation quality claims."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".claude/skills/bakhtin"
SPEC = importlib.util.spec_from_file_location("voice_packet", SKILL / "scripts/voice_packet.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VoicePacketTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.install = self.root / "installed-bakhtin"
        shutil.copytree(SKILL, self.install)
        self.custom = self.root / "voice-custom" / "SKILL.md"
        self.custom.parent.mkdir()
        self.custom.write_text("# Мой голос\n\nГоворю на ты. Мой уникальный пример.\n", encoding="utf-8")

    def test_cold_install_default_from_unrelated_directory(self):
        unrelated = self.root / "unrelated"
        unrelated.mkdir()
        result = subprocess.run([sys.executable, str(self.install / "scripts/voice_packet.py")],
                                cwd=unrelated, capture_output=True, text=True, check=True)
        packet = json.loads(result.stdout)
        self.assertEqual(packet["effective_voice"], "neutral-base")
        self.assertEqual(packet["selected_by"], "default")
        self.assertEqual(packet["voice_text"], (self.install / "voice/neutral-base.md").read_text())
        self.assertEqual(packet["signature_concepts"], [])

    def test_implicit_and_explicit_default_have_identical_style(self):
        implicit = MODULE.build_packet(skill_dir=self.install)
        explicit = MODULE.build_packet(voice="neutral-base", skill_dir=self.install)
        for key in ["voice_text", "source_sha256", "calibration_example"]:
            self.assertEqual(implicit[key], explicit[key])

    def test_explicit_custom_overrides_project_and_contains_no_default(self):
        packet = MODULE.build_packet(voice=str(self.custom), project_voice="neutral-base", skill_dir=self.install)
        self.assertEqual(packet["voice_text"], self.custom.read_text())
        self.assertEqual(packet["effective_voice"], "custom")
        self.assertEqual(packet["selected_by"], "explicit")
        self.assertNotIn("calibration_example", packet)
        self.assertNotIn("нейтральный", packet["voice_text"])

    def test_configured_project_voice_overrides_default(self):
        packet = MODULE.build_packet(project_voice=str(self.custom), skill_dir=self.install)
        self.assertEqual(packet["selected_by"], "project")
        self.assertEqual(packet["voice_text"], self.custom.read_text())

    def test_named_custom_voice(self):
        path = self.install / "voice/custom.md"
        path.write_text(self.custom.read_text())
        self.assertEqual(MODULE.build_packet(voice="custom", skill_dir=self.install)["voice_text"], path.read_text())

    def test_missing_explicit_voice_is_not_replaced_by_default(self):
        with self.assertRaises(FileNotFoundError):
            MODULE.build_packet(voice="missing-author", skill_dir=self.install)

    def test_cli_missing_voice_returns_error_without_packet(self):
        result = subprocess.run([sys.executable, str(self.install / "scripts/voice_packet.py"), "--voice", "missing-author"],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")

    def test_missing_bundled_profile_is_an_installation_error(self):
        (self.install / "voice/neutral-base.md").unlink()
        with self.assertRaises(FileNotFoundError):
            MODULE.build_packet(skill_dir=self.install)

    def test_empty_voice_is_an_error(self):
        self.custom.write_text("")
        with self.assertRaises(ValueError):
            MODULE.build_packet(voice=str(self.custom), skill_dir=self.install)
        with self.assertRaises(ValueError):
            MODULE.build_packet(voice="", skill_dir=self.install)

    def test_custom_file_named_neutral_base_does_not_inherit_bundled_example(self):
        path = self.root / "neutral-base.md"
        path.write_text(self.custom.read_text())
        packet = MODULE.build_packet(voice=str(path), skill_dir=self.install)
        self.assertNotIn("calibration_example", packet)
        self.assertEqual(packet["voice_text"], path.read_text())

    def test_packet_content_matches_hash_and_contains_five_verbatim_anchors(self):
        packet = MODULE.build_packet(skill_dir=self.install)
        self.assertEqual(hashlib.sha256(packet["voice_text"].encode()).hexdigest(), packet["source_sha256"])
        anchors = [line for line in packet["voice_text"].splitlines() if line.startswith("> ")]
        self.assertEqual(len(anchors), 5)


if __name__ == "__main__":
    unittest.main()
