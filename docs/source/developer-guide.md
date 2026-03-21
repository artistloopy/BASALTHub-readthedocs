## 5. Developer Guide
 
### 5.1 Architecture Overview
 
BASALT is implemented in **Python 3** and structured as a command-line toolkit. The main entry point is `BASALT.py` (or the `BASALT` console script installed into the conda environment). Each functional module is organized as a separate Python script within the repository.
 
```
BASALT/
├── BASALT.py              # Main entry point
├── basalt_env.yml         # Legacy conda environment file
├── TUTORIAL.md            # Command reference
├── README.md              # Quick start and overview
└── scripts/               # Module-specific scripts
    ├── autobinning/
    ├── binselection/
    ├── refinement/
    └── gapfilling/
```
 
---
 
### 5.2 The Four Modules
 
#### Module 1 — Automated Binning
 
The automated binning module runs multiple binning tools (**MetaBAT2**, **MaxBin2**, **CONCOCT**, **SemiBin**) each with multiple sensitivity thresholds. Read mapping is performed with **Bowtie2** (SRS) or **Minimap2** (LRS). Coverage depth is computed with **SAMtools** and **BEDTools**.
 
The key insight is that running multiple binners with multiple thresholds generates a diverse pool of bin candidates — the subsequent modules then select and refine the best representatives.
 
#### Module 2 — Bin Selection
 
1. **Best-bins grouping** — Bins with overlapping contig IDs are merged into hybrid bins, then grouped by average nucleotide identity (ANI).
2. **Core Sequence Identification** — Within each group, a neural network identifies "core sequences" (high-confidence inliers) for each bin by comparing coverage estimates.
3. **Redundancy removal** — Bins sharing the same core sequences are flagged as redundant; only the highest-quality representative is retained.
4. **Outlier Removal** — Tetranucleotide frequency (TNF) and coverage correlation coefficient (CCC) are combined in multidimensional IQR detection to remove contaminating contigs.
 
#### Module 3 — Refinement
 
The refinement module enhances bin quality through a series of steps:
 
- **Sequence Retrieval** — Recruits unused (unbinned) sequences into target bins using pair-end tracking. For LRS data, this step maximizes utilization of long reads.
- **Polishing** — If LRS data is available, Pilon (SRS) or Racon (LRS) are applied to correct assembly errors. Polishing at the bin level saves ~90% of computation time compared to assembly-level polishing.
- **rOLC (Restrained Overlap–Layout–Consensus)** — An in-house consensus correction algorithm.
- **Reassembly** — Uses **SPAdes Hybrid** (default for hybrid data) to improve bin contiguity and fill sequence gaps.
 
> **Note:** Reassembly is not available for LRS-alone datasets in the current version.
 
#### Module 4 — Gap Filling
 
The gap-filling module attempts to complement genome gaps that cannot be recovered from the initial bin set, using sequences that remain unbinned after all previous steps.
 
---
 
### 5.3 Integrated Tools & Dependencies
 
#### Sequence Processing
| Tool | Purpose |
|------|---------|
| Bowtie2 | Short-read alignment |
| BWA | Alternative short-read aligner |
| SAMtools | BAM/SAM processing, coverage calculation |
| Minimap2 | Long-read alignment |
| BEDTools | Coverage depth computation |
| Prodigal | Gene prediction (used in quality assessment) |
| BLAST+ | Sequence similarity search |
| HMMER | Profile HMM search (CheckM marker genes) |
 
#### Binning Tools
| Tool | Role in BASALT |
|------|---------------|
| MetaBAT2 | Primary binner (multiple thresholds) |
| MaxBin2 | Primary binner (multiple thresholds) |
| CONCOCT | Primary binner (multiple thresholds) |
| SemiBin | Primary binner (added in v1.2.0) |
| MetaBinner | Optional extra binner (`-e m`) |
 
#### Assembly & Polishing
| Tool | Purpose |
|------|---------|
| SPAdes | Hybrid reassembly (SRS + LRS) |
| MEGAHIT | Assembly option |
| IDBA-UD | Assembly option |
| Unicycler | Assembly option |
| Pilon | Short-read polishing |
| Racon | Long-read polishing |
| Miniasm | Long-read assembly |
 
#### Quality Assessment
| Tool | Purpose |
|------|---------|
| CheckM | MAG quality assessment (completeness, contamination) |
| CheckM2 | ML-based MAG quality assessment (v1.0.1+) |
| pplacer | Phylogenetic placement (used by CheckM) |
| Diamond | Protein alignment (used by CheckM2) |
 
#### Python ML/Scientific Stack
- TensorFlow, PyTorch — Neural network-based redundancy detection
- LightGBM, scikit-learn — Machine learning utilities
- NumPy (==1.26.4), SciPy, pandas — Numerical and data processing
- python-igraph — Graph-based clustering
- Biopython — Sequence I/O and manipulation
 
---
 
### 5.4 Contributing
 
BASALT is an open-source project hosted at [https://github.com/EMBL-PKU/BASALT](https://github.com/EMBL-PKU/BASALT).
 
To contribute:
 
1. **Fork** the repository on GitHub
2. **Create a feature branch:** `git checkout -b feature/my-improvement`
3. **Commit your changes** with clear messages
4. **Test** your changes against the demo dataset
5. **Open a Pull Request** describing your changes and motivation
 
For bug reports and feature requests, please use the [GitHub Issues tracker](https://github.com/EMBL-PKU/BASALT/issues).
 
For direct contact, reach the development team at: **yuke.sz@pku.edu.cn**
 
---
 
### 5.5 License
 
BASALT is released under the **MIT License**. See the `LICENSE` file in the repository for full terms.
 
The software integrates multiple third-party tools (MetaBAT2, MaxBin2, CONCOCT, SemiBin, CheckM, CheckM2, SPAdes, etc.), each of which is subject to its own license. Users are responsible for complying with the licenses of all integrated tools when using BASALT in their research or workflows.
 
