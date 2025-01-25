
from utils import *
from db_ops import check_signature_in_db
def scan_files(files, one_file=False):
    nums_all = len(files)
    if(one_file == True):
        file = files
        if(check_path(file)):
            hash_val = get_file_hash_sha256(file)
            file = os.path.abspath(file)
            if(check_signature_in_db(hash_val)):
                print("\n")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("file (" + file + ") matches a signature.")
    elif(one_file == False):
        for file in files:
            if(check_path(file)):
                hash_val = get_file_hash_sha256(file)	# O(V) V is the number of blocks in hashing function
                file = os.path.abspath(file)
                if(check_signature_in_db(hash_val)):
                    print("\n")
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print("file (" + file + ") matches a signature.")

# Scan all files in a directory recursively
def scan_directory(directory):
	if(check_path_directory(directory)):
		files = list_files_in_directory(directory)		# O(N)
		scan_files(files)		# O(N * X * M * V)	N is number of files 	X is the number of / in the path 	M is the number of processes iterated V is the number of blocks in hashing function
