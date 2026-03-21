## 2. Installation
 
### 2.1 System Requirements
 
- **Operating System:** Linux (64-bit recommended)
- **CPU:** Multi-core recommended (default threads: 2; 32+ cores recommended for large datasets)
- **RAM:** Minimum 64 GB; 230 GB or more recommended for large datasets with reassembly
- **Storage:** Varies with dataset size; allow several hundred GB for intermediate files
- **Software prerequisite:** [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)
- **Python:** 3.12 (managed via conda)
 
> A workstation with Intel Xeon Gold 5218 CPU @ 2.30 GHz with 32 cores is expected to complete the demo dataset within approximately 6 hours.
 
---
 
### 2.2 Installing BASALT v1.2.0 (Recommended)
 
**Step 1 — Clone the repository**
 
```bash
git clone https://github.com/EMBL-PKU/BASALT.git
cd BASALT
```
 
**Step 2 — Create the conda environment**
 
```bash
conda create -n basalt_env -c conda-forge -c bioconda \
    python=3.12 \
    megahit metabat2 maxbin2 concoct prodigal semibin \
    bedtools blast bowtie2 diamond checkm2 \
    unicycler spades samtools racon pplacer pilon \
    ncbi-vdb minimap2 miniasm idba hmmer entrez-direct \
    biopython uv --yes
```
 
> This step installs all sequence processing, assembly, polishing, and genome quality assessment tools. Allow significant time for environment solving and package downloads.
 
**Step 3 — Activate the environment and install Python packages**
 
```bash
conda activate basalt_env
 
uv pip install tensorflow torch torchvision tensorboard tensorboardx \
    lightgbm scikit-learn numpy==1.26.4 python-igraph scipy pandas matplotlib \
    cython biolib joblib tqdm requests checkm-genome
```
 
**Step 4 — Add BASALT to your PATH (or use BASALT.py directly)**
 
```bash
# Option A: Run via the installed conda command
BASALT --help
 
# Option B: Standalone users (no PATH modification needed)
python BASALT.py --help
```
 
---
 
### 2.3 Setting Up CheckM2 Database
 
> **Note:** The CheckM2 database is **not** bundled with BASALT v1.0.1 and later installations. It must be set up separately.
 
Follow the official CheckM2 user guide:
```
https://github.com/chklovski/CheckM2
```
 
After activating `basalt_env`, run:
 
```bash
checkm2 database --download
```
 
---
 
### 2.4 Using Mirror Channels (China / Slow Networks)
 
If you are in China or experiencing slow download speeds, configure Tsinghua mirror channels before creating the environment:
 
```bash
site=https://mirrors.tuna.tsinghua.edu.cn/anaconda
conda config --add channels ${site}/pkgs/free/
conda config --add channels ${site}/pkgs/main/
conda config --add channels ${site}/cloud/bioconda/
conda config --add channels ${site}/cloud/conda-forge/
```
 
If you encounter errors downloading deep learning model files, use a VPN or download them manually from:
- **Figshare:** Download directly, then rename the file `41093033` to `BASALT.zip`
- **Tencent Weiyun:** Available via web browser download
 
---
 
### 2.5 Verifying Installation with Demo Files
 
BASALT provides demo files to verify successful installation. The demo package (`Data.tar.gz`) contains:
 
- Short-read and long-read raw sequence files
- An OPERA-MS assembled contig file
- `Final_bestbinset.tar.gz` — expected output for validation
- `basalt.sh` — example run script
 
```bash
# Download and extract demo data, then run
bash basalt.sh
```
 
Compare your output bins with those in `Final_bestbinset.tar.gz` to confirm the installation is functioning correctly.
 
---
 
### 2.6 Troubleshooting
 
| Problem | Possible Cause | Solution |
|--------|----------------|----------|
| `conda env create` fails with unsatisfiable dependencies | Strict channel priority or outdated conda | Use `conda config --set channel_priority flexible` or update conda |
| Model download fails | Network connectivity | Use VPN or download models manually from Figshare/Weiyun |
| `tqdm` version conflict | Pinned dependency in older env file | Use the v1.2.0 installation method (manual conda create + uv pip install) |
| Reassembly runs out of memory | `-m` limit too low | Increase `-m` value; reassembly requires the most RAM |
| Error mid-run | Transient failure | Resubmit the task; BASALT supports re-running with `--mode continue` |
 

 