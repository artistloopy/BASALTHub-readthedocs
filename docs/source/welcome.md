
 
## 1. Overview
 
### 1.1 What is BASALT?
 
BASALT (**B**inning **A**cross a **S**eries of **A**ssemblies **T**oolkit) is a comprehensive bioinformatics pipeline for metagenomic binning and post-binning refinement. It recovers, compares, and optimizes assembled genomes across a series of assemblies generated from short-read sequencing (SRS), long-read sequencing (LRS), or hybrid platforms, with the goal of producing high-quality metagenome-assembled genomes (MAGs).
 
Published in *Nature Communications* (2024), BASALT addresses a longstanding bottleneck in genome-resolved metagenomics: the low efficiency of conventional binning tools in recovering adequate numbers of high-quality MAGs from complex environmental datasets.
 
> **Reference:** Qiu Z, Yuan L, Lian C, et al. BASALT refines binning from metagenomic data and increases resolution of genome-resolved metagenomic analysis. *Nat. Commun.* 2024, 15, 2179. https://doi.org/10.1038/s41467-024-46539-7
 
---
 
### 1.2 Key Features
 
- **Multi-binner integration** — Runs MetaBAT2, MaxBin2, CONCOCT, and SemiBin simultaneously with multiple thresholds to maximize initial bin diversity.
- **Neural network-based redundancy removal** — Uses AI to identify and remove redundant bins while retaining the best representative for each genome.
- **Short- and long-read support** — Fully supports SRS, LRS (Nanopore/PacBio), HiFi, and hybrid datasets, including Hi-C data.
- **Post-binning refinement** — Dedicated refinement algorithms using tetranucleotide frequency (TNF) and coverage correlation to clean contaminated bins.
- **Sequence retrieval** — Recruits unbinned sequences back into target bins using pair-end tracking.
- **Polishing and reassembly** — Integrates Pilon, Racon, and SPAdes Hybrid for bin polishing and gap filling.
- **Open-frame toolkit** — Modular design allows users to import externally generated bins (e.g., from VAMB) and run only the refinement steps.
- **Standalone module execution** — Each functional module (Automated Binning, Bin Selection, Refinement, Gap Filling) can be run independently.
 
---
 
### 1.3 How BASALT Works
 
BASALT is organized into **four functional modules**, each comprising one or more in-house designed algorithms:
 
```
Raw Reads / Assemblies
        │
        ▼
┌─────────────────────┐
│  Automated Binning  │  ← MetaBAT2, MaxBin2, CONCOCT, SemiBin (multi-threshold)
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│    Bin Selection    │  ← Best-bins grouping, Core Sequence ID, Outlier Removal
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│     Refinement      │  ← Sequence Retrieval, Polishing (LRS), rOLC, Reassembly
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│     Gap Filling     │  ← Complementing genome gaps from unbinned sequences
└─────────────────────┘
         │
         ▼
  High-Quality MAGs
```
 
A set of nine in-house programs work in concert: **Auto-binning**, **Bin selection**, **Best-bins grouping**, **Core Sequence Identification**, **Outlier Removal**, **Sequence Retrieval**, **Polishing**, **Restrained Overlap–Layout–Consensus (rOLC)**, and **Reassembly**.
 
---
 
### 1.4 Performance Benchmarks
 
BASALT has been validated against CAMI (Critical Assessment of Metagenome Interpretation) benchmark datasets and real-world environmental samples:
 
| Metric | BASALT vs. metaWRAP | BASALT vs. VAMB | BASALT vs. DASTool |
|--------|--------------------|-----------------|--------------------|
| MAGs recovered (CAMI-high) | +~2× | +~2× | +~2× |
| MAGs from lake sediment | ~30% more | — | — |
| Unique class-level lineages recovered | +21 unique classes | — | — |
| Non-redundant ORFs retrieved | +47.6% | — | — |
| Unique MAGs absent in other tools | 69 exclusive MAGs | — | — |
 
Bins produced by BASALT show significantly higher completeness, lower contamination, and higher overall quality scores compared to all other tested tools (Kruskal–Wallis test, P < 10⁻⁷).
 
---
 
### 1.5 Citation
 
If you use BASALT in your research, please cite:
 
> Qiu, Z., Yuan, L., Lian, C., Lin, B., Chen, J., Mu, R., Qiao, X., Zhang, L., Xu, Z., Fan, L., Zhang, Y., Wang, S., Li, J., Cao, H., Li, B., Chen, B., Song, C., Liu, Y., Shi, L., Tian, Y., Ni, J., Zhang, T., Zhou, J., Zhuang, W., & Yu, K. (2024). BASALT refines binning from metagenomic data and increases resolution of genome-resolved metagenomic analysis. *Nature Communications*, 15, 2179. https://doi.org/10.1038/s41467-024-46539-7
 

 
