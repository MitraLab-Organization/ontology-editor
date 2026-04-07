# BAP Human Head Ontology

A collaborative repository for managing the Brain Architecture Project (BAP) 
Human (Homo sapiens) head anatomical ontology.

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
- **Focus:** Head and neck anatomy

<!-- STATS_START -->
📊 **Ontology Statistics**
```
├── Structures: 382
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
│   │   ├── Scapula (L)
│   │   └── Scapula (R)
│   ├── Hindlimb (L)
│   ├── Hindlimb (R)
│   └── Tail
├── Head
│   ├── Head cavities and passages
│   │   ├── Ear Cavities
│   │   │   ├── Eustachian tube (L)
│   │   │   ├── Eustachian tube (R)
│   │   │   ├── External acoustic meatus (L)
│   │   │   ├── External acoustic meatus (R)
│   │   │   ├── Internal acoustic meatus (L)
│   │   │   ├── Internal acoustic meatus (R)
│   │   │   ├── Tympanic cavity (L)
│   │   │   └── Tympanic cavity (R)
│   │   ├── Nasal cavity
│   │   ├── Oral cavity
│   │   ├── Paranasal sinuses (L)
│   │   └── Paranasal sinuses (R)
│   ├── Head endocrine and exocrine system
│   │   ├── Lacrimal gland
│   │   │   ├── Extraorbital lacrimal gland (L)
│   │   │   ├── Extraorbital lacrimal gland (R)
│   │   │   ├── Harderian gland (L)
│   │   │   ├── Harderian gland (R)
│   │   │   ├── Intraorbital lacrimal gland (L)
│   │   │   └── Intraorbital lacrimal gland (R)
│   │   ├── Palatal submucosa (L)
│   │   ├── Palatal submucosa (R)
│   │   ├── Salivary glands
│   │   │   ├── Parotid glands (L)
│   │   │   ├── Parotid glands (R)
│   │   │   ├── Sublingual glands (L)
│   │   │   ├── Sublingual glands (R)
│   │   │   ├── Submandibular glands (L)
│   │   │   └── Submandibular glands (R)
│   │   └── Sebaceous glands
│   ├── Head integumentary system
│   │   ├── External ear
│   │   │   ├── Pinna (L)
│   │   │   └── Pinna (R)
│   │   ├── Head skin (L)
│   │   ├── Head skin (R)
│   │   ├── Whiskers (L)
│   │   └── Whiskers (R)
│   ├── Head musculoskeletal system
│   │   ├── Cranial muscles
│   │   │   ├── Eye Muscles
│   │   │   │   ├── Inferior oblique (L)
│   │   │   │   ├── Inferior oblique (R)
│   │   │   │   ├── Lateral rectus (L)
│   │   │   │   ├── Lateral rectus (R)
│   │   │   │   ├── Levator palpebrae superioris (L)
│   │   │   │   ├── Levator palpebrae superioris (R)
│   │   │   │   ├── Medial rectus (L)
│   │   │   │   ├── Medial rectus (R)
│   │   │   │   ├── Retractor bulbi (L)
│   │   │   │   ├── Retractor bulbi (R)
│   │   │   │   ├── Superior oblique muscle
│   │   │   │   │   └── Superior oblique tendon
│   │   │   │   │       ├── Trochlea (L)
│   │   │   │   │       └── Trochlea (R)
│   │   │   │   ├── Superior rectus (L)
│   │   │   │   └── Superior rectus (R)
│   │   │   ├── Middle ear muscles
│   │   │   │   ├── Stapedius (L)
│   │   │   │   ├── Stapedius (R)
│   │   │   │   ├── Tensor tympani (L)
│   │   │   │   └── Tensor tympani (R)
│   │   │   ├── Muscles of facial expression
│   │   │   │   ├── Buccinatorius (L)
│   │   │   │   ├── Buccinatorius (R)
│   │   │   │   ├── Ceratohyoideus (L)
│   │   │   │   ├── Ceratohyoideus (R)
│   │   │   │   ├── Depressor rhinarii (L)
│   │   │   │   ├── Depressor rhinarii (R)
│   │   │   │   ├── Depressor septi nasi (L)
│   │   │   │   ├── Depressor septi nasi (R)
│   │   │   │   ├── Digastricus anterior (L)
│   │   │   │   ├── Digastricus anterior (R)
│   │   │   │   ├── Digastricus posterior (L)
│   │   │   │   ├── Digastricus posterior (R)
│   │   │   │   ├── Dilatator nasi (L)
│   │   │   │   ├── Dilatator nasi (R)
│   │   │   │   ├── External Ear Muscles
│   │   │   │   │   ├── Auricularis anterior (L)
│   │   │   │   │   ├── Auricularis anterior (R)
│   │   │   │   │   ├── Auricularis posterior (L)
│   │   │   │   │   ├── Auricularis posterior (R)
│   │   │   │   │   ├── Auricularis superior (L)
│   │   │   │   │   └── Auricularis superior (R)
│   │   │   │   ├── Frontalis (L)
│   │   │   │   ├── Frontalis (R)
│   │   │   │   ├── Geniohyoideus (L)
│   │   │   │   ├── Geniohyoideus (R)
│   │   │   │   ├── Interscutularis (L)
│   │   │   │   ├── Interscutularis (R)
│   │   │   │   ├── Levator anguli oris (L)
│   │   │   │   ├── Levator anguli oris (R)
│   │   │   │   ├── Levator labii superioris (L)
│   │   │   │   ├── Levator labii superioris (R)
│   │   │   │   ├── Levator labii superioris alaeque nasi (L)
│   │   │   │   ├── Levator labii superioris alaeque nasi (R)
│   │   │   │   ├── Levator rhinarii (L)
│   │   │   │   ├── Levator rhinarii (R)
│   │   │   │   ├── Mandibuloauricularis (L)
│   │   │   │   ├── Mandibuloauricularis (R)
│   │   │   │   ├── Mylohyoideus (L)
│   │   │   │   ├── Mylohyoideus (R)
│   │   │   │   ├── Nasalis (L)
│   │   │   │   ├── Nasalis (R)
│   │   │   │   ├── Occipitalis (L)
│   │   │   │   ├── Occipitalis (R)
│   │   │   │   ├── Orbicularis oculi (L)
│   │   │   │   ├── Orbicularis oculi (R)
│   │   │   │   ├── Orbicularis oris
│   │   │   │   ├── Orbito-temporo-auricularis (L)
│   │   │   │   ├── Orbito-temporo-auricularis (R)
│   │   │   │   ├── Platysma cervicale (L)
│   │   │   │   ├── Platysma cervicale (R)
│   │   │   │   ├── Platysma myoides (L)
│   │   │   │   ├── Platysma myoides (R)
│   │   │   │   ├── Sphincter colli profundus (L)
│   │   │   │   ├── Sphincter colli profundus (R)
│   │   │   │   ├── Sphincter colli superficialis (L)
│   │   │   │   ├── Sphincter colli superficialis (R)
│   │   │   │   ├── Stylohyoideus (L)
│   │   │   │   ├── Stylohyoideus (R)
│   │   │   │   ├── Stylopharyngeus (L)
│   │   │   │   ├── Stylopharyngeus (R)
│   │   │   │   ├── Zygomaticus major (L)
│   │   │   │   ├── Zygomaticus major (R)
│   │   │   │   ├── Zygomaticus minor (L)
│   │   │   │   └── Zygomaticus minor (R)
│   │   │   ├── Muscles of mastication
│   │   │   │   ├── Masseter
│   │   │   │   │   ├── Deep masseter (L)
│   │   │   │   │   ├── Deep masseter (R)
│   │   │   │   │   ├── Superficial masseter (L)
│   │   │   │   │   ├── Superficial masseter (R)
│   │   │   │   │   ├── Zygomaticomandibularis (L)
│   │   │   │   │   └── Zygomaticomandibularis (R)
│   │   │   │   ├── Pterygoideus lateralis (L)
│   │   │   │   ├── Pterygoideus lateralis (R)
│   │   │   │   ├── Pterygoideus medialis (L)
│   │   │   │   ├── Pterygoideus medialis (R)
│   │   │   │   └── Temporalis
│   │   │   │       ├── Temporalis lateralis (L)
│   │   │   │       ├── Temporalis lateralis (R)
│   │   │   │       ├── Temporalis medialis (L)
│   │   │   │       └── Temporalis medialis (R)
│   │   │   ├── Sternohyoideus (L)
│   │   │   ├── Sternohyoideus (R)
│   │   │   └── Tongue muscles
│   │   │       ├── Extrinsic tongue muscles
│   │   │       │   ├── Genioglossus (L)
│   │   │       │   ├── Genioglossus (R)
│   │   │       │   ├── Hyoglossus (L)
│   │   │       │   ├── Hyoglossus (R)
│   │   │       │   ├── Palatoglossus (L)
│   │   │       │   ├── Palatoglossus (R)
│   │   │       │   ├── Styloglossus (L)
│   │   │       │   └── Styloglossus (R)
│   │   │       └── Intrinsic tongue muscles
│   │   │           ├── Inferior longitudinal (L)
│   │   │           ├── Inferior longitudinal (R)
│   │   │           ├── Superior longitudinal (L)
│   │   │           ├── Superior longitudinal (R)
│   │   │           ├── Transverse (L)
│   │   │           ├── Transverse (R)
│   │   │           ├── Vertical (L)
│   │   │           └── Vertical (R)
│   │   └── Cranium
│   │       ├── Inner Ear
│   │       │   ├── Cochlea (L)
│   │       │   ├── Cochlea (R)
│   │       │   ├── Semicircular canals (L)
│   │       │   ├── Semicircular canals (R)
│   │       │   ├── Vestibule (L)
│   │       │   └── Vestibule (R)
│   │       ├── Middle ear
│   │       │   ├── Incus (L)
│   │       │   ├── Incus (R)
│   │       │   ├── Malleus (L)
│   │       │   ├── Malleus (R)
│   │       │   ├── Stapes (L)
│   │       │   └── Stapes (R)
│   │       ├── Neurocranium
│   │       │   ├── Basisphenoid (L)
│   │       │   ├── Basisphenoid (R)
│   │       │   ├── Ethmoid (L)
│   │       │   ├── Ethmoid (R)
│   │       │   ├── Frontal
│   │       │   ├── Interparietal (L)
│   │       │   ├── Interparietal (R)
│   │       │   ├── Occipital
│   │       │   ├── Parietal (L)
│   │       │   ├── Parietal (R)
│   │       │   ├── Presphenoid (L)
│   │       │   ├── Presphenoid (R)
│   │       │   ├── Tympanic membrane (L)
│   │       │   └── Tympanic membrane (R)
│   │       └── Viscerocranium
│   │           ├── Jaw apparatus
│   │           │   ├── Articular disk (L)
│   │           │   ├── Articular disk (R)
│   │           │   ├── Mandible (L)
│   │           │   ├── Mandible (R)
│   │           │   ├── Maxilla (L)
│   │           │   └── Maxilla (R)
│   │           ├── Lacrimal (L)
│   │           ├── Lacrimal (R)
│   │           ├── Nasal (L)
│   │           ├── Nasal (R)
│   │           ├── Nasal septum
│   │           ├── Palatine (L)
│   │           ├── Palatine (R)
│   │           ├── Premaxilla (L)
│   │           ├── Premaxilla (R)
│   │           ├── Sphenoid
│   │           ├── Squamosal (L)
│   │           ├── Squamosal (R)
│   │           ├── Vomer
│   │           ├── Zygomatic (L)
│   │           └── Zygomatic (R)
│   ├── Head nervous system
│   │   ├── Head central nervous system
│   │   │   └── Brain
│   │   └── Head peripheral nervous system
│   │       └── Cranial Nerves
│   │           ├── Abducens nerve (L)
│   │           ├── Abducens nerve (R)
│   │           ├── Accessory nerve (L)
│   │           ├── Accessory nerve (R)
│   │           ├── Facial nerve (L)
│   │           ├── Facial nerve (R)
│   │           ├── Glossopharyngeal nerve (L)
│   │           ├── Glossopharyngeal nerve (R)
│   │           ├── Hypoglossal nerve (L)
│   │           ├── Hypoglossal nerve (R)
│   │           ├── Oculomotor nerve (L)
│   │           ├── Oculomotor nerve (R)
│   │           ├── Olfactory nerve (L)
│   │           ├── Olfactory nerve (R)
│   │           ├── Optic nerve (L)
│   │           ├── Optic nerve (R)
│   │           ├── Terminal nerve (L)
│   │           ├── Terminal nerve (R)
│   │           ├── Trigeminal nerve (L)
│   │           ├── Trigeminal nerve (R)
│   │           ├── Trochlear nerve (L)
│   │           ├── Trochlear nerve (R)
│   │           ├── Vagus nerve (L)
│   │           ├── Vagus nerve (R)
│   │           ├── Vestibulocochlear nerve (L)
│   │           └── Vestibulocochlear nerve (R)
│   ├── Head vascular system
│   │   ├── Arteries
│   │   │   ├── Lingual artery (L)
│   │   │   ├── Lingual artery (R)
│   │   │   ├── Maxillary artery (L)
│   │   │   ├── Maxillary artery (R)
│   │   │   ├── Temporal artery (L)
│   │   │   └── Temporal artery (R)
│   │   ├── Head lymphatics (L)
│   │   ├── Head lymphatics (R)
│   │   ├── Head veins (L)
│   │   └── Head veins (R)
│   └── Sense organs
│       ├── Eye (L)
│       ├── Eye (R)
│       ├── Gustatory epithelium (L)
│       ├── Gustatory epithelium (R)
│       ├── Inner ear (L)
│       ├── Inner ear (R)
│       ├── Olfactory epithelium (L)
│       ├── Olfactory epithelium (R)
│       ├── Whisker barrels (L)
│       └── Whisker barrels (R)
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
