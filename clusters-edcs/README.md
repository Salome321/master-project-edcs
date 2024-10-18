The smarts_classification_electrophile.ipynb is a jupyter notebook that selects electrophiles from a dtaabase of small molecules, clusters them based on their structural similarities and returns a smaller selection of molecules that best capture the diversity of the original dataset:
- It uses a database of chemicals with their smiles
- It selects electrophiles suing smarts for common electrophilic groups (vinyl carbonyls, ketones, halomethyl carbonyls, beta-lactams, nitriles, epoxides, phosphonates, vinyl sulfonyls, disulfides, carboxylic acids, sulfonyl halides, esters and aromatic michael acceptors)
- It clusters them based on their structural similarity (using Tanimoto coefficients) and using the selected cutoff
- It finds the cluster centroids (the molecule within each cluster that has the most similarity with the other molecules in the same cluster)
- It picks other molecules from the largest clusters (molecules that are the furthest away from the cluster centroids)
- It returns a final file with the selected molecule

In this example, the input file is a database of EDCs (DEDuCT_ChemicalBasicInformation.csv) and the output file is the final selection (selected_molecules.csv).\

Some parts of the script come from this tutorial on clustering:\
https://projects.volkamerlab.org/teachopencadd/talktorials/T005_compound_clustering.html
