# %%
import pandas as pd

# %%
# CODE THAT CONVERTS SDF FILE TO XYZ COORDINATES

# open files and create list of CID
f = open('DEDuCT_3D_structure.sdf').read()
# Create a list of CIDs for the molecules of interest
cid_list = 
key = '$$$$'

text = []

FILE_TYPES = {
    "sdf": {"num_atoms_line": 3, "split_func": lambda x: x.split()[:4]}
}

for cid in cid_list:
    first = f.find('$$$$\n' + cid + '\n')
    nxt = f.find('M  END', first+1)
    text1 = f[first:nxt].splitlines()[1:] # text1 is a list of coordinates for 1 molecule
    
    with open('coordinates_sdf.sdf','w') as tfile:
        tfile.write('\n'.join(text1))
    
    with open('coordinates_sdf.sdf', 'r') as sdf:
        lines = sdf.readlines()
        num_atoms = int(lines[FILE_TYPES['sdf']["num_atoms_line"]][:3].strip())
        lines = lines[4:4+num_atoms]
        atoms = [FILE_TYPES['sdf']["split_func"](line) for line in lines if line.strip()]
        atoms = [line for line in atoms if line]
        for i in range(len(atoms)):
            atoms[i][0],atoms[i][1],atoms[i][2], atoms[i][3] = atoms[i][3],atoms[i][0],atoms[i][1],atoms[i][2]
        atoms2 = [' '.join(atom) for atom in atoms]
        atoms2.insert(0,'$$$$')
        atoms2.insert(1,str(num_atoms))
        atoms2.insert(2,cid)
        
    text = text + atoms2 # Combines all lists for all molecules

# Saves list as a txt file 
with open('xyz_coordinates.txt','w') as tfile:
    tfile.write('\n'.join(text))

#%%
# Code to produce xyz from sdf for a particular molecule stored in coordinate_sdf txt file
text = []

FILE_TYPES = {
    "sdf": {"num_atoms_line": 3, "split_func": lambda x: x.split()[:4]}
}

with open('coordinates_sdf.sdf', 'r') as sdf:
    lines = sdf.readlines()
    num_atoms = int(lines[FILE_TYPES['sdf']["num_atoms_line"]][:3].strip())
    cid = lines[0]
    lines = lines[4:4+num_atoms]
    atoms = [FILE_TYPES['sdf']["split_func"](line) for line in lines if line.strip()]
    atoms = [line for line in atoms if line]
    for i in range(len(atoms)):
        atoms[i][0],atoms[i][1],atoms[i][2], atoms[i][3] = atoms[i][3],atoms[i][0],atoms[i][1],atoms[i][2]
    atoms2 = [' '.join(atom) for atom in atoms]
    atoms2.insert(0,'$$$$')
    atoms2.insert(1,str(num_atoms))
    atoms2.insert(2,cid)
        
text = text + atoms2 # Combines all lists for all molecules

# Saves list as a txt file 
with open('f_coordinate.txt','w') as tfile:
    tfile.write('\n'.join(text))