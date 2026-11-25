#!/usr/bin/env python3
"""Resolve one writing voice and print its complete, uncompressed JSON packet."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

SKILL_DIR = Path(__file__).resolve().parents[1]


def resolve_voice(value, skill_dir):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Voice must be a non-empty slug or Markdown path")
    value = value.strip()
    path = Path(value).expanduser()
    if path.is_absolute() or path.suffix == ".md" or "/" in value or "\\" in value:
        return path.resolve()
    return (skill_dir / "voice" / (value + ".md")).resolve()


def build_packet(voice=None, project_voice=None, skill_dir=SKILL_DIR):
    skill_dir = Path(skill_dir).resolve()
    if voice is not None:
        selected, selected_by = voice, "explicit"
    elif project_voice is not None:
        selected, selected_by = project_voice, "project"
    else:
        selected, selected_by = "neutral-base", "default"
    path = resolve_voice(selected, skill_dir)
    data = path.read_bytes()  # Missing explicit voices are errors, never silent fallbacks.
    text = data.decode("utf-8")
    if not text.strip():
        raise ValueError(f"Empty voice profile: {path}")
    bundled = path == (skill_dir / "voice/neutral-base.md").resolve()
    slug = path.parent.name if path.stem == "SKILL" else path.stem
    if path.stem == "SKILL" and slug.startswith("voice-"):
        slug = slug[len("voice-"):]
    packet = {
        "schema_version": 1,
        "effective_voice": "neutral-base" if bundled else slug,
        "selected_by": selected_by,
        "source_path": str(path),
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "voice_text": text,
        "signature_concepts": [] if bundled else None,
    }
    if bundled:
        example_path = skill_dir / "voice/neutral-base.example.md"
        packet["calibration_example"] = example_path.read_text(encoding="utf-8")
        packet["calibration_example_sha256"] = hashlib.sha256(example_path.read_bytes()).hexdigest()
        packet["calibration_example_origin"] = "model-written sample accepted by the user; not part of measured source corpus"
    return packet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--voice", help="Explicit voice slug or Markdown path")
    parser.add_argument("--project-voice", help="Voice explicitly configured by the project")
    args = parser.parse_args()
    try:
        packet = build_packet(args.voice, args.project_voice)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"voice_packet: {exc}\n")
    print(json.dumps(packet, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
