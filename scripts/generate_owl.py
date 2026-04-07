#!/usr/bin/env python3
"""
BAP OWL Generator

Generates OWL/RDF XML files from YAML structure and relationship definitions.

Ontology title/description:
  * Branch ``main`` → Mouse head atlas (original).
  * Any other branch (e.g. ``hand``, ``human-hand``) → Human hand atlas.
  Override: ``--ontology mouse|hand``, or ``--branch NAME`` with ``--ontology auto``.

CI sets ``GITHUB_REF_NAME``; that is used when ``git`` is unavailable.

Usage:
    python scripts/generate_owl.py --output bap.owl
    python scripts/generate_owl.py --ontology hand
    python scripts/generate_owl.py --ontology auto --branch main
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


# ============================================================================
# Configuration
# ============================================================================

ROOT_DIR = Path(__file__).parent.parent
STRUCTURES_DIR = ROOT_DIR / "structures"
RELATIONSHIPS_DIR = ROOT_DIR / "relationships"

# Namespace definitions
NAMESPACES = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'owl': 'http://www.w3.org/2002/07/owl#',
    'xml': 'http://www.w3.org/XML/1998/namespace',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'obo': 'http://purl.obolibrary.org/obo/',
    'dce': 'http://purl.org/dc/elements/1.1/',
    'dcterms': 'http://purl.org/dc/terms/',
}

# OBO relation IRIs
OBO_RELATIONS = {
    'part_of': 'http://purl.obolibrary.org/obo/BFO_0000050',
    'has_part': 'http://purl.obolibrary.org/obo/BFO_0000051',
    'develops_from': 'http://purl.obolibrary.org/obo/RO_0002202',
    'innervated_by': 'http://purl.obolibrary.org/obo/RO_0002005',
    'innervates': 'http://purl.obolibrary.org/obo/RO_0002134',
    'supplied_by': 'http://purl.obolibrary.org/obo/RO_0002178',
    'supplies': 'http://purl.obolibrary.org/obo/RO_0002179',
    'adjacent_to': 'http://purl.obolibrary.org/obo/RO_0002220',
    'continuous_with': 'http://purl.obolibrary.org/obo/RO_0002150',
    'attaches_to': 'http://purl.obolibrary.org/obo/RO_0002371',
}

# IAO annotation property
IAO_DEFINITION = 'http://purl.obolibrary.org/obo/IAO_0000115'

# Ontology metadata (IRI stable; title/description set per branch — see resolve_ontology_metadata)
BASE_IRI = "http://purl.obolibrary.org/obo/bap.owl"
VERSION = "1.0.0"

MOUSE_HEAD_TITLE = "BAP Mouse Head Atlas"
MOUSE_HEAD_DESCRIPTION = "Brain Architecture Project Mouse Head Anatomical Atlas"
HUMAN_HAND_TITLE = "BAP Human Hand Atlas"
HUMAN_HAND_DESCRIPTION = (
    "Brain Architecture Project human hand and forelimb anatomical ontology"
)


def detect_git_branch(repo_root: Path) -> str:
    """Current branch: CI env first, then `git rev-parse`, else main."""
    for key in ("GITHUB_REF_NAME", "CI_COMMIT_REF_NAME", "GIT_BRANCH"):
        val = os.environ.get(key)
        if val:
            return val.strip()
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "main"


def resolve_ontology_metadata(
    branch: str,
    override: Optional[str],
) -> Tuple[str, str, str]:
    """
    Return (title, description, profile_label).

    - override 'mouse' | 'hand' forces profile.
    - auto: ``main`` → Mouse head atlas; any other branch → Human hand atlas.
    """
    if override == "mouse":
        return MOUSE_HEAD_TITLE, MOUSE_HEAD_DESCRIPTION, "mouse"
    if override == "hand":
        return HUMAN_HAND_TITLE, HUMAN_HAND_DESCRIPTION, "hand"

    b = (branch or "main").strip().lower()
    if b == "main":
        return MOUSE_HEAD_TITLE, MOUSE_HEAD_DESCRIPTION, "mouse"
    return HUMAN_HAND_TITLE, HUMAN_HAND_DESCRIPTION, "hand"


# ============================================================================
# Data Loading
# ============================================================================

def load_yaml_files(directory: Path) -> List[dict]:
    """Load all YAML files from a directory."""
    data = []
    if not directory.exists():
        return data
    
    for filepath in sorted(directory.glob("*.yaml")):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                if content:
                    data.append(content)
        except Exception as e:
            print(f"Warning: Failed to load {filepath}: {e}")
    
    return data


def load_all_structures() -> Dict[str, dict]:
    """Load all structures from YAML files."""
    structures = {}
    for data in load_yaml_files(STRUCTURES_DIR):
        for struct in data.get("structures", []):
            if "id" in struct:
                structures[struct["id"]] = struct
    return structures


def load_all_relationships() -> List[dict]:
    """Load all relationships from YAML files."""
    relationships = []
    for data in load_yaml_files(RELATIONSHIPS_DIR):
        rels = data.get("relationships") or []  # Handle None case
        relationships.extend([r for r in rels if r is not None])
    return relationships


# ============================================================================
# OWL Generation
# ============================================================================

def escape_xml(text: str) -> str:
    """Escape special XML characters."""
    if text is None:
        return ''
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&apos;'))


def bap_id_to_iri(bap_id: str) -> str:
    """Convert BAP ID to full IRI."""
    # BAP_0001234 -> http://purl.obolibrary.org/obo/BAP_0001234
    return f"http://purl.obolibrary.org/obo/{bap_id}"


def get_relation_iri(predicate: str) -> str:
    """Get the OBO IRI for a relationship predicate."""
    return OBO_RELATIONS.get(predicate, f"{BASE_IRI}#{predicate}")


def generate_owl(
    structures: Dict[str, dict],
    relationships: List[dict],
    *,
    title: str,
    description: str,
) -> str:
    """Generate complete OWL/RDF XML document."""
    lines = []
    
    # XML declaration
    lines.append('<?xml version="1.0"?>')
    
    # RDF root with namespaces
    lines.append(f'<rdf:RDF xmlns="{BASE_IRI}#"')
    lines.append(f'     xml:base="{BASE_IRI}"')
    for prefix, uri in sorted(NAMESPACES.items()):
        lines.append(f'     xmlns:{prefix}="{uri}"')
    lines[-1] = lines[-1] + '>'
    
    # Ontology metadata
    lines.append(f'    <owl:Ontology rdf:about="{BASE_IRI}">')
    lines.append(f'        <dcterms:title>{escape_xml(title)}</dcterms:title>')
    lines.append(f'        <dcterms:description>{escape_xml(description)}</dcterms:description>')
    lines.append(f'        <owl:versionInfo>{VERSION}</owl:versionInfo>')
    lines.append('        <dcterms:license rdf:resource="https://creativecommons.org/licenses/by/4.0/"/>')
    lines.append('    </owl:Ontology>')
    lines.append('')
    
    # Annotation properties
    lines.append('    <!-- Annotation Properties -->')
    lines.append(f'    <owl:AnnotationProperty rdf:about="{IAO_DEFINITION}"/>')
    lines.append('    <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/description"/>')
    lines.append('    <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/title"/>')
    lines.append('    <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/license"/>')
    lines.append('')
    
    # Object properties
    lines.append('    <!-- Object Properties -->')
    for name, iri in sorted(OBO_RELATIONS.items()):
        lines.append(f'    <owl:ObjectProperty rdf:about="{iri}">')
        lines.append(f'        <rdfs:label>{name.replace("_", " ")}</rdfs:label>')
        lines.append('    </owl:ObjectProperty>')
        lines.append('')
    
    # Build relationship lookup
    rel_lookup: Dict[str, List[dict]] = {}
    for rel in relationships:
        subject = rel.get("subject")
        if subject:
            if subject not in rel_lookup:
                rel_lookup[subject] = []
            rel_lookup[subject].append(rel)
    
    # Classes (structures)
    lines.append('    <!-- Classes (Anatomical Structures) -->')
    lines.append('')
    
    for struct_id in sorted(structures.keys()):
        struct = structures[struct_id]
        iri = bap_id_to_iri(struct_id)
        
        lines.append(f'    <!-- {iri} -->')
        lines.append(f'    <owl:Class rdf:about="{iri}">')
        
        # Parent (subClassOf)
        parent = struct.get("parent")
        if parent and parent in structures:
            parent_iri = bap_id_to_iri(parent)
            lines.append(f'        <rdfs:subClassOf rdf:resource="{parent_iri}"/>')
        
        # Relationships as existential restrictions
        if struct_id in rel_lookup:
            for rel in rel_lookup[struct_id]:
                predicate = rel.get("predicate")
                obj = rel.get("object")
                if predicate and obj and obj in structures:
                    rel_iri = get_relation_iri(predicate)
                    obj_iri = bap_id_to_iri(obj)
                    lines.append('        <rdfs:subClassOf>')
                    lines.append('            <owl:Restriction>')
                    lines.append(f'                <owl:onProperty rdf:resource="{rel_iri}"/>')
                    lines.append(f'                <owl:someValuesFrom rdf:resource="{obj_iri}"/>')
                    lines.append('            </owl:Restriction>')
                    lines.append('        </rdfs:subClassOf>')
        
        # Definition
        definition = struct.get("definition")
        if definition:
            lines.append(f'        <obo:IAO_0000115 xml:lang="en">{escape_xml(definition)}</obo:IAO_0000115>')
        
        # Label
        name = struct.get("name", struct_id)
        lines.append(f'        <rdfs:label xml:lang="en">{escape_xml(name)}</rdfs:label>')
        
        # Abbreviation
        abbrev = struct.get("abbreviation")
        if abbrev:
            lines.append(f'        <obo:IAO_0000111>{escape_xml(abbrev)}</obo:IAO_0000111>')
        
        lines.append('    </owl:Class>')
        lines.append('')
    
    lines.append('</rdf:RDF>')
    lines.append('')
    lines.append('<!-- Generated by BAP Ontology Generator -->')
    lines.append('')
    
    return '\n'.join(lines)


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Generate OWL from YAML definitions")
    parser.add_argument("--output", "-o", default="bap-mousehead.owl", help="Output file path")
    parser.add_argument("--validate", "-v", action="store_true", help="Validate XML output")
    parser.add_argument(
        "--ontology",
        choices=("auto", "mouse", "hand"),
        default="auto",
        help="Ontology title/description: auto from branch (main=Mouse head, else Human hand), or force mouse/hand",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Override branch name for --ontology auto (default: detect from git or CI)",
    )
    args = parser.parse_args()

    branch = args.branch if args.branch else detect_git_branch(ROOT_DIR)
    override = None if args.ontology == "auto" else args.ontology
    title, description, profile = resolve_ontology_metadata(branch, override)
    print(f"Branch: {branch!r}  Profile: {profile}  Title: {title}")
    
    print("Loading structures...")
    structures = load_all_structures()
    print(f"  Loaded {len(structures)} structures")
    
    print("Loading relationships...")
    relationships = load_all_relationships()
    print(f"  Loaded {len(relationships)} relationships")
    
    print("Generating OWL...")
    owl_content = generate_owl(structures, relationships, title=title, description=description)
    
    # Validate XML if requested
    if args.validate:
        try:
            from xml.etree import ElementTree as ET
            ET.fromstring(owl_content)
            print("  ✓ XML is valid")
        except Exception as e:
            print(f"  ✗ XML validation failed: {e}")
            return 1
    
    # Write output
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(owl_content)
    
    print(f"\n✓ Generated {output_path}")
    print(f"  Structures: {len(structures)}")
    print(f"  Relationships: {len(relationships)}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
