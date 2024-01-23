# Masters thesis: Computational risk assessment of the DNA damage potential of EDCs
Scripts and files for my Masters thesis on the Computational assessment of the DNA damage potential of Endocring Disrupting Chemicals (EDCs).\
Masters thesis in the LCBC lab (Laboratoire de Chimie et Biochimie Computationnelle) at EPFL.

## Database
The Database of Endocrine Disrupting Chemicals and their Toxicity Profiles (DEDuCT).
- B.S. Karthikeyan#, J. Ravichandran#,*, K. Mohanraj$, R.P. Vivek-Ananth$ & A. Samal*, A curated knowledgebase on endocrine disrupting chemicals and their biological systems-level perturbations, Science of the Total Environment, 692: 281-296 (2019).

## Scripts

### benchmarks-orca
Benchmarks performed to select the best basis set, level of theory and number of cores for Orca.\
MatPlotLib plots to show the results.

### clusters-edcs
Selection of electrophiles from the EDCs database, clustering based on their structural similarities (Tanimoto coefficients) and selection of a smaller number of molecules that best capture the diversity in the original dataset.

### coordinates-edcs
Conversion of sdf coordinates to xyz coordinates (the DEDuCT database of the 3D coordinates of the EDCs were in the sdf format, but Orca requires the xyz format).

### similarity classification
Classification of the EDCs based on their similarity with BPA or estradiol. This script was used to select the relevant EDCs for further study.
