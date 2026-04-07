#!/usr/bin/env python3
"""
Generate OWL as RDF/XML from YAML (OWL 2 RDF/XML serialisation).

Implementation is shared with generate_owl.py; this script is a convenience entry
point with an XML-oriented default output name.

Usage:
    python scripts/generate_owl_xml.py
    python scripts/generate_owl_xml.py -o dist/bap-hand.owl
    python scripts/generate_owl_xml.py -o ontology.xml --validate
"""

import argparse
import sys
from pathlib import Path

from generate_owl import (
    ROOT_DIR,
    detect_git_branch,
    generate_owl,
    load_all_relationships,
    load_all_structures,
    resolve_ontology_metadata,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate OWL/RDF XML from structures/ and relationships/ YAML"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="bap-ontology.owl.xml",
        help="Output file path (default: %(default)s)",
    )
    parser.add_argument(
        "-v",
        "--validate",
        action="store_true",
        help="Parse generated output as XML after writing",
    )
    parser.add_argument(
        "--ontology",
        choices=("auto", "mouse", "hand"),
        default="auto",
        help="Same as generate_owl.py: auto from branch (main=Mouse, else Human hand)",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Override branch for --ontology auto",
    )
    args = parser.parse_args()

    branch = args.branch if args.branch else detect_git_branch(ROOT_DIR)
    override = None if args.ontology == "auto" else args.ontology
    title, description, profile = resolve_ontology_metadata(branch, override)
    print(f"Branch: {branch!r}  Profile: {profile}")

    print("Loading structures...")
    structures = load_all_structures()
    print(f"  Loaded {len(structures)} structures")

    print("Loading relationships...")
    relationships = load_all_relationships()
    print(f"  Loaded {len(relationships)} relationships")

    print("Generating OWL/RDF XML...")
    content = generate_owl(
        structures, relationships, title=title, description=description
    )

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"Wrote {out.resolve()}")

    if args.validate:
        try:
            from xml.etree import ElementTree as ET

            ET.fromstring(content)
            print("XML parse: OK")
        except Exception as e:
            print(f"XML parse failed: {e}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
