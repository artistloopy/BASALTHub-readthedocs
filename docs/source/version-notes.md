## 3. Version Notes
 
### 3.1 v1.2.0 (Current)
 
**Released:** 2024 (latest stable)
 
This is the recommended version for new installations. Key changes from v1.1.0:
 
- Updated installation procedure using `uv pip install` for faster, more reliable Python package resolution
- Updated to **Python 3.12** environment
- Added **SemiBin** as a default binner alongside MetaBAT2, MaxBin2, and CONCOCT
- Added **Diamond** and **CheckM2** as conda-installable dependencies
- Improved compatibility with current conda-forge and bioconda channel versions
- `python-igraph` replaces older graph library
 
**Installation note:** CheckM2 database must still be set up separately after installation. See [Section 2.3](#23-setting-up-checkm2-database).
 
---
 
### 3.2 v1.1.0
 
**Released:** June 12, 2024 (tagged `v1.1.0`)
 
This release introduced significant functional expansions:
 
- **Bug fixes** across multiple core scripts
- **Standalone module function** — Users can now invoke individual modules (Refinement, De-replication, etc.) independently without running the full pipeline
- **Data feeding function** — Allows importing externally binned data into the BASALT workflow
- **Standalone de-replication function** — Can be used to dereplicate bins from any source
- **Standalone refinement function** — Enables post-binning refinement of bins produced by other tools (e.g., VAMB, metaWRAP)
 
---
 
### 3.3 v1.0.1
 
**Released:** February 13, 2024
 
- Minor patch release following the original v1.0.0 publication release
- **Note:** CheckM2 database is **not** compiled with this version. Manual database setup is required (see [Section 2.3](#23-setting-up-checkm2-database))
- VAMB temporarily removed from the BASALT environment due to environment conflicts and suboptimal performance on environmental datasets. Bins generated externally with VAMB can still be imported into BASALT for refinement
 
---
 
### 3.4 v1.0.0
 
**Released:** August 18, 2023 (tagged `v1.0.0`); official publication release February 2024
 
- Initial public release coinciding with the *Nature Communications* publication
- Implements the four core modules: Automated Binning, Bin Selection, Refinement, and Gap Filling
- Supports short-read, long-read, and hybrid sequencing inputs
- Hi-C dataset integration for scaffolding/binning
- Benchmarked against CAMI-high dataset (596 genomes) and Aiding Lake sediment dataset
 
---
 
### 3.5 Known Limitations
 
- **Reassembly with LRS-alone datasets** is not supported in the current version (SRS or hybrid required). This feature is planned for a future release.
- **VAMB** is no longer included in the BASALT environment but can be used as an external binner with outputs fed into BASALT.
- **Reassembly is computationally intensive** — it significantly increases runtime but also substantially improves genome quality. Allocate memory accordingly.
- The **CheckM2 database** must be downloaded and configured separately in v1.0.1 and later.
 

 