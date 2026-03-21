## 4. Tutorial
 
### 4.1 Quick Start
 
After installation and activating the `basalt_env` environment:
 
```bash
conda activate basalt_env
 
# Basic run with short reads and one assembly
BASALT -a assembly.fasta -s sample_R1.fq,sample_R2.fq -t 32 -m 128
 
# Run with multiple assemblies and both short- and long-read data
BASALT -a assembly1.fasta,assembly2.fasta \
       -s short1.R1.fq,short1.R2.fq/short2.R1.fq,short2.R2.fq \
       -l nanopore1.fastq,nanopore2.fastq \
       -t 60 -m 230
```
 
---
 
### 4.2 Input File Formats
 
**Assemblies (`-a`)**
- Accepted formats: `.fa`, `.fna`, `.fasta`
- Compressed files: `.gz`, `.tar.gz`, `.zip`
- Multiple assemblies are comma-separated: `-a assembly1.fa,assembly2.fa`
 
**Short-read datasets (`-s`)**
- Paired-end reads, with reads within a pair separated by `,` and pairs separated by `/`
- Example: `-s d1_r1.fq,d1_r2.fq/d2_r1.fq,d2_r2.fq`
- Compressed formats (`.gz`, `.tar.gz`, `.zip`) are supported
 
**Long-read datasets (`-l`)**
- Nanopore or PacBio long reads
- Multiple files comma-separated: `-l nanopore1.fastq,nanopore2.fastq`
 
**HiFi dataset (`-hf`)**
- PacBio HiFi reads
 
**Hi-C dataset (`-c`)**
- Hi-C read pairs: `-c hc1.fq,hc2.fq`
 
---
 
### 4.3 Command-Line Arguments Reference
 
```
BASALT [-h] [-a ASSEMBLIES] [-s SR_DATASETS] [-l LONG_DATASETS]
       [-hf HIFI_DATASET] [-c HI_C_DATASET] [-t THREADS] [-m RAM]
       [-e EXTRA_BINNER] [-qc QC_SOFTWARE]
       [--min-cpn MIN_COMPLETENESS] [--max-ctn MAX_CONTAMINATION]
       [--mode RUNNING_MODE] [--module FUNCTIONAL_MODULE]
       [--autopara AUTOBINING_PARAMETERS]
       [--refinepara REFINEMENT_PARAMETER]
```
 
#### Required Arguments
 
| Argument | Description |
|----------|-------------|
| `-a` | Comma-separated list of assembly files (`.fa`, `.fna`, `.fasta`, or compressed) |
| `-s` | Short-read paired-end datasets. Pairs separated by `/`, reads within pair by `,` |
 
#### Optional Arguments
 
| Argument | Default | Description |
|----------|---------|-------------|
| `-l` | — | Long-read datasets (Nanopore/PacBio), comma-separated |
| `-hf` | — | HiFi dataset |
| `-c` | — | Hi-C dataset(s) |
| `-t` | 2 | Number of CPU threads |
| `-m` | 64 | Maximum RAM in GB (critical for reassembly step) |
| `-e` | — | Extra binner: `m` = MetaBinner, `v` = VAMB (external bins only) |
| `-qc` | checkm | Quality control software (`checkm` or `checkm2`) |
| `--min-cpn` | 35 | Completeness cutoff for refinement (only bins ≥ this value are refined) |
| `--max-ctn` | 20 | Contamination cutoff for refinement (only bins ≤ this value are refined) |
| `--mode` | — | Running mode: `continue` to resume an interrupted run |
| `--module` | — | Run a specific module only |
| `--autopara` | — | Override automatic binning parameters (e.g., `more-sensitive`) |
| `--refinepara` | — | Override refinement parameters |
 
---
 
### 4.4 Example Use Cases
 
#### Case 1 — Short-read only, single assembly
```bash
BASALT -a assembly.fasta \
       -s reads_R1.fq,reads_R2.fq \
       -t 32 -m 128
```
 
#### Case 2 — Multiple assemblies with hybrid data (SRS + LRS)
```bash
BASALT -a assembly1.fasta,assembly2.fasta \
       -s short1.R1.fq,short1.R2.fq/short2.R1.fq,short2.R2.fq \
       -l nanopore1.fastq,nanopore2.fastq \
       -t 60 -m 230
```
 
#### Case 3 — Import external bins for refinement only
If you have bins from another tool (e.g., VAMB, metaWRAP), use the standalone refinement module:
```bash
BASALT --module refinement \
       -a assembly.fasta \
       -s reads_R1.fq,reads_R2.fq \
       --min-cpn 35 --max-ctn 20 \
       -t 32 -m 128
```
 
#### Case 4 — Using CheckM2 as quality control
```bash
BASALT -a assembly.fasta \
       -s reads_R1.fq,reads_R2.fq \
       -qc checkm2 \
       -t 48 -m 200
```
 
#### Case 5 — Resuming an interrupted run
```bash
BASALT -a assembly.fasta \
       -s reads_R1.fq,reads_R2.fq \
       --mode continue \
       -t 32 -m 128
```
 
---
 
### 4.5 Running Individual Modules
 
BASALT v1.1.0+ supports running modules independently:
 
| Module | `--module` value | Description |
|--------|-----------------|-------------|
| Automated Binning | `autobinning` | Initial multi-binner binning step |
| Bin Selection | `binselection` | Redundancy removal and core sequence identification |
| Refinement | `refinement` | Outlier removal, sequence retrieval, polishing |
| Gap Filling | `gapfilling` | Reassembly to fill genome gaps |
| De-replication | `dereplication` | Standalone dereplication of any bin set |
 
---
 
### 4.6 Understanding Output
 
After a successful BASALT run, the primary output directory will contain:
 
- **`Final_bestbinset/`** — The final set of high-quality, non-redundant MAGs in FASTA format
- **`CheckM_results/`** (or CheckM2 equivalent) — Quality assessment results for each bin (completeness, contamination, strain heterogeneity)
- **`Binning_results/`** — Intermediate binsets from each binner at each threshold
- **`Refinement_results/`** — Output from the refinement module
- **Log files** — Detailed logs for each processing step
 
MAG quality is assessed using the MIMAG standard: a MAG with **Completeness − 5 × Contamination ≥ 50** is considered medium-to-high quality.
 

 