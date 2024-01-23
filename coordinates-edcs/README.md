The extract_coordinates.py script converts sdf coordinates files to xyz coordinate files.\
\
It can be used in two ways:
### 1. List of sdf coordinates
The script will extract teh sdf coordinates for the cid of interest listed in cid_list\
input: sdf file which contains sdf coordinates of several molecules separated by $$$$ (eg. DEDuCT_3D_structure.sdf)\
output: xyz_coordinates.txt file which contains xyz coordiantes of the molecules separated by $$$$, their number of atoms and identifier (eg. CID)
### 2. Single sdf file
input: sdf coordinates stored in eg. coordinates_sdf.sdf\
output: f_coordinate.txt file of xyz coordinates
