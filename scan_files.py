
from utils import *
from db_ops import check_signature_in_db
from real_time_buffers import add_to_real_time_total_files, add_to_malicious_real_time_buffer, add_to_real_time_malicious_files_with_process, add_to_real_time_malicious_files_without_process, add_to_real_time_malicious_files_with_process_termiated, add_to_real_time_malicious_files_with_process_not_termiated, add_to_real_time_malicious_files_prevented, add_to_real_time_malicious_files_not_prevented



def scan_files(files, one_file=False, real_time=False):
    nums_all = len(files)
    if(one_file == True and real_time == False):
        file = files
        if(check_path(file)):
            hash_val = get_file_hash_sha256(file)
            file = os.path.abspath(file)
            if(check_signature_in_db(hash_val)):
                print("\n")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("file (" + file + ") matches a signature.")
    elif(one_file == False and real_time == False):
        for file in files:
            if(check_path(file)):
                hash_val = get_file_hash_sha256(file)	# O(V) V is the number of blocks in hashing function
                file = os.path.abspath(file)
                if(check_signature_in_db(hash_val)):
                    print("\n")
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print("file (" + file + ") matches a signature.")
    elif(one_file == True and real_time == True):
        # the parameter files represents a single file
        if(check_path(files)):
            malicious_Flag = False
            hash_val = get_file_hash_sha256(files)						# O(V) V is the number of blocks in the hashing funtion
            file = os.path.abspath(files)
            add_to_real_time_total_files(file)
            if(check_signature_in_db(hash_val)):
                malicious_Flag = True
                add_to_malicious_real_time_buffer(file)
                print("\n")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("File (" + file + ") matches a signature.")				
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("\n")
            else:
                print("File " + file + " is CLEAN")


# Scan all files in a directory recursively
def scan_directory(directory):
	if(check_path_directory(directory)):
		files = list_files_in_directory(directory)		# O(N)
		scan_files(files)		# O(N * X * M * V)	N is number of files 	X is the number of / in the path 	M is the number of processes iterated V is the number of blocks in hashing function
