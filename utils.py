import os
import hashlib

# Check path validity for files 	O(1)
def check_path(path):
	if(os.path.exists(path)): 
		if(os.path.isfile(path)): 
			return True
		else:
			return False
	else:
		return False

#-------------------------------------------------------------------------------------------------

# Check path validity for directories 		O(1)
def check_path_directory(path):
	if(os.path.exists(path)):
		if(os.path.isdir(path)):
			return True 
		else:
			return False
	else:
		return False

#-------------------------------------------------------------------------------------------------

# Check signature validity 	O(N)
def check_signature(sig):
	sig = sig.replace(" ", "") 		# O(N)
	if(len(sig) == 64):
		return True 
	else:
		return False

#-------------------------------------------------------------------------------------------------

# Check the validity of a group of signatures 	O(M * N)
def check_signature_group(sigs):
	for s in sigs:		# O(M * N)
		if not(check_signature(s)): 	# O(N)
			return False
	return True

#-------------------------------------------------------------------------------------------------

# Check if the string represents a number 		O(1)
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# List all files in a directory recursively 		# O(N)
def list_files_in_directory(directory):
	if(check_path_directory(directory)):
		files = []
		entries_in_directory = os.listdir(directory)
		for entry in entries_in_directory:
			entry_full_Path = os.path.join(directory, entry)
			if check_path_directory(entry_full_Path):
				files = files + list_files_in_directory(entry_full_Path)
			else:
				if(check_path(entry_full_Path)):
					files.append(entry_full_Path)
		return files

# Get hash values for a file using sha256 	O(N) where N is number of blocks in the file
def get_file_hash_sha256(file):
	sha256_hash = hashlib.sha256()
	with open(file,"rb") as f:
		for block_of_512_bytes in iter(lambda: f.read(512),b""):
				sha256_hash.update(block_of_512_bytes)
		return sha256_hash.hexdigest()
