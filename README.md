# BAP Human Hand Ontology

A collaborative repository for managing the Brain Architecture Project (BAP) 
Human (Homo sapiens) **hand and forelimb** anatomical ontology.

## 📚 [**View the Auto-Generated Wiki →**](https://mitralab-organization.github.io/bap-ontology-editor/)

Complete documentation with detailed reports, statistics, and visualizations - 
**automatically updated on every push!**

## Overview

This repository provides a human-readable way to manage:
- **Anatomical structures** (muscles, nerves, blood vessels, bones)
- **Hierarchies** (parent-child relationships)
- **Biological relationships** (innervation, blood supply, developmental origins)

Changes are validated automatically via GitHub Actions and generate OWL files 
for use in WebProtégé and other tools.

## Species Information

- **Common name:** Human
- **Scientific name:** Homo sapiens
- **NCBI Taxonomy:** 9606
- **Focus:** Hand and forelimb (head/neck subtree retained but marked deprecated for this scope)

<!-- STATS_START -->
📊 **Ontology Statistics**
```
├── Structures: 390
├── Hierarchy depth: 7 levels
└── Relationships: 0
```
<!-- STATS_END -->

## Current Hierarchy

<!-- HIERARCHY_START -->
```
Body
├── Appendages
│   ├── Forelimb
│   │   ├── Clavicle (L)
│   │   ├── Clavicle (R)
│   │   ├── Hand
│   │   │   ├── Hand cavities and passages
│   │   │   ├── Hand endocrine and exocrine system
│   │   │   ├── Hand integumentary system
│   │   │   ├── Hand musculoskeletal system
│   │   │   ├── Hand nervous system
│   │   │   ├── Hand sensory structures
│   │   │   └── Hand vascular system
│   │   ├── Scapula (L)
│   │   └── Scapula (R)
│   ├── Hindlimb (L)
│   ├── Hindlimb (R)
│   └── Tail
├── Neck
│   ├── Neck cavities and passages
│   │   ├── Larynx
│   │   └── Pharynx
│   │       ├── Esophagus
│   │       ├── Sternofacialis left (L)
│   │       └── Sternofacialis left (R)
│   ├── Neck endocrine and exocrine system
│   │   └── Thyroid gland
│   ├── Neck integumentary system
│   │   ├── Neck skin (L)
│   │   └── Neck skin (R)
│   ├── Neck musculoskeletal system
│   │   ├── Neck muscles
│   │   │   ├── Cleidomastoideus (L)
│   │   │   ├── Cleidomastoideus (R)
│   │   │   ├── Cleidooccipitalis (L)
│   │   │   ├── Cleidooccipitalis (R)
│   │   │   ├── Cricothyroideus (L)
│   │   │   ├── Cricothyroideus (R)
│   │   │   ├── Jugulohyoideus (L)
│   │   │   ├── Jugulohyoideus (R)
│   │   │   ├── Laryngeal muscles
│   │   │   │   ├── Arytenoideus (L)
│   │   │   │   ├── Arytenoideus (R)
│   │   │   │   ├── Cricoarytenoideus alaris (L)
│   │   │   │   ├── Cricoarytenoideus alaris (R)
│   │   │   │   ├── Cricoarytenoideus lateralis (L)
│   │   │   │   ├── Cricoarytenoideus lateralis (R)
│   │   │   │   ├── Cricoarytenoideus posterior (L)
│   │   │   │   ├── Cricoarytenoideus posterior (R)
│   │   │   │   ├── Thyroarytenoideus (L)
│   │   │   │   └── Thyroarytenoideus (R)
│   │   │   ├── Omohyoideus (L)
│   │   │   ├── Omohyoideus (R)
│   │   │   ├── Pharyngeal muscles
│   │   │   │   ├── Constrictor pharyngis inferior (L)
│   │   │   │   ├── Constrictor pharyngis inferior (R)
│   │   │   │   ├── Constrictor pharyngis medius (L)
│   │   │   │   ├── Constrictor pharyngis medius (R)
│   │   │   │   ├── Constrictor pharyngis superior (L)
│   │   │   │   ├── Constrictor pharyngis superior (R)
│   │   │   │   ├── Levator veli palatini (L)
│   │   │   │   ├── Levator veli palatini (R)
│   │   │   │   ├── Palatopharyngeus (L)
│   │   │   │   ├── Palatopharyngeus (R)
│   │   │   │   ├── Pterygopharyngeus (L)
│   │   │   │   ├── Pterygopharyngeus (R)
│   │   │   │   ├── Salpingopharyngeus (L)
│   │   │   │   ├── Salpingopharyngeus (R)
│   │   │   │   ├── Tensor veli palatini (L)
│   │   │   │   └── Tensor veli palatini (R)
│   │   │   ├── Sternomastoideus (L)
│   │   │   ├── Sternomastoideus (R)
│   │   │   ├── Sternothyroideus (L)
│   │   │   ├── Sternothyroideus (R)
│   │   │   ├── Thyrohyoideus (L)
│   │   │   ├── Thyrohyoideus (R)
│   │   │   └── Trapezius
│   │   │       ├── Acromiotrapezius (L)
│   │   │       ├── Acromiotrapezius (R)
│   │   │       ├── Spinotrapezius (L)
│   │   │       └── Spinotrapezius (R)
│   │   └── Neck skeletal system
│   │       ├── Cervical vertebra
│   │       ├── Laryngeal skeletal system
│   │       │   ├── Arytenoid cartilage (L)
│   │       │   ├── Arytenoid cartilage (R)
│   │       │   ├── Cricoid cartilage (L)
│   │       │   ├── Cricoid cartilage (R)
│   │       │   ├── Epiglottis
│   │       │   ├── Laryngeal alar cartilage (L)
│   │       │   ├── Laryngeal alar cartilage (R)
│   │       │   └── Thyroid cartilage
│   │       └── Pharyngeal skeleton
│   │           └── Hyoid bone
│   ├── Neck nervous system
│   │   ├── Neck central nervous system
│   │   │   └── Spinal Cord
│   │   └── Neck peripheral nervous system
│   │       ├── Cervical nerves (L)
│   │       └── Cervical nerves (R)
│   └── Neck vascular system
│       ├── Neck arteries (L)
│       ├── Neck arteries (R)
│       ├── Neck lymphatics (L)
│       ├── Neck lymphatics (R)
│       ├── Neck veins (L)
│       └── Neck veins (R)
└── Trunk
    ├── Abdomen (L)
    ├── Abdomen (R)
    ├── Pelvis (L)
    ├── Pelvis (R)
    └── Thorax
        ├── Sternum (L)
        └── Sternum (R)
```
<!-- HIERARCHY_END -->

## Relationships

<!-- MERMAID_START -->

<!-- MERMAID_END -->

<!-- TABLES_START -->

<!-- TABLES_END -->

## Getting Started

### Add Structures via Issue Templates

1. Go to [Issues → New Issue](../../issues/new/choose)
2. Select **"➕ Add New Structure"**
3. Fill out the form and submit
4. Wait for approval and automatic PR creation

### Local Development

```bash
# Clone and setup
git clone <this-repo>
cd bap-ontology-human

# Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Validate
python scripts/validate.py

# Generate OWL
python scripts/generate_owl.py --output bap-human.owl
```

## Repository Structure

```
bap-ontology-human/
├── structures/           # Anatomical structure definitions
│   ├── body_regions.yaml # Base hierarchy
│   ├── muscles.yaml      # Muscle structures
│   ├── nerves.yaml       # Nerve structures
│   ├── vessels.yaml      # Blood vessel structures
│   └── skeletal.yaml     # Bone structures
├── relationships/        # Cross-structure relationships
│   ├── innervation.yaml  # Nerve → muscle connections
│   ├── blood_supply.yaml # Vessel → structure connections
│   └── developmental.yaml# Developmental origins
├── schemas/              # JSON Schema for validation
├── scripts/              # Build and validation scripts
└── .github/workflows/    # CI/CD automation
```

## Contributing

1. Create a feature branch from `main`
2. Make your changes to YAML files
3. Run `python scripts/validate.py` locally
4. Open a Pull Request
5. Address review feedback
6. Merge after approval

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) - Brain Architecture Project
