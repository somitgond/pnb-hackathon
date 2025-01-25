# Licensed under GNU GPL2
# Author: Somit Gond

from scan_files import *
from utils import *
from db_ops import *

# # Activating DB initialization
# from db_ops import db

# event loop
while(True):
    op = input('''Specify your operation:\n-----------------------
1: Scan a file
2: Scan a directory (recursively for all sub-directories)
3: Add a SHA-256 signature to the database
4: Exit

Your choice is: ''')
    print("\n")
    if(op == '1'):
        file = input("Enter the path of the file: ")
        print("\n")
        if(check_path(file)):
            scan_files(file, one_file=True)		# O(X * M * V) X is the number of / in the path M is the number of processes iterated V is the number of blocks in hashing function
        else:
            print("This Path Is NOT A Valid File Path!")
        print("\n*******************************************************\n")

    elif(op == '2'):
        directory = input("Enter the path of the directory: ")
        if(check_path_directory(directory)):
            absolute_path = os.path.abspath(directory)
            print("\nSCANNING (" + absolute_path + " )")
            print("-----------------------------------------------------------------------")
            scan_directory(directory)	# O(N * X * M * V)	N is number of files 	X is the number of / in the path 	M is the number of processes iterated V is the number of blocks in hashing function
        else:
            print("This Path Is NOT A Valid Directory Path!")
        print("\n*******************************************************\n")

    elif(op == '3'):
        signature = input("Enter the signature to add: ")
        if(check_signature(signature)):				# O(N) N is the signature length
            result = add_signature(signature)
            if(result == False):
                print("Signature Added Successfully")
            else:
                print("Failed To Add The Signature ( " + str(result) + " )")
        else:
            print("Invalid SHA-256 Signature!")
    elif(op == '4'):
        break
    else:
        print("Invalid operation!")
        print("\n*******************************************************\n")

###############################################################################################################################################

db.close()
