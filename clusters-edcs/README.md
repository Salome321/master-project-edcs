The smarts_classification_electrophile.ipynb is a jupyter notebook that clusters molecules and returns a smaller selection of molecules that bet capture the divesrity of the original dataset:
- It uses a database of chemicals with their smiles
- It clusters them based on their structural similarity (using Tanimoto coefficients) and using the selected cutoff
- It finds the cluster centroids (the molecule within each cluster that has the most similarity with the other molecules in the same cluster)
- It picks other molecules from the largest clusters (molecules that are the furthest away from the cluster centroids)
- It returns a final file with the selected molecule

In this example, the input file is a database of EDCs (DEDuCT_ChemicalBasicInformation.csv) and the output file is the final selection (selected_molecules.csv).
