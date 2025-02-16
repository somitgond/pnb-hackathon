import os, sqlite3
from utils import get_file_hash_sha256


# Database initialization
def db_init():
	if not(os.path.exists('./SIGNATURES.db')):
		db = sqlite3.connect('SIGNATURES.db', check_same_thread=False)
		db.execute('''CREATE TABLE SIGNATURES
	          (SIGN CHAR(64) PRIMARY KEY     NOT NULL
	         );''')
		return db
	else:
		db = sqlite3.connect('SIGNATURES.db', check_same_thread=False)
		db.execute('''CREATE TABLE IF NOT EXISTS SIGNATURES
	          	(SIGN CHAR(64) PRIMARY KEY     NOT NULL
	         	);''')
		return db

#-------------------------------------------------------------------------------------------------

db = db_init()

#-------------------------------------------------------------------------------------------------

# Add a signature to the db O(1)
def add_signature(signature):
	params = [signature]
	try:
		db.execute('''INSERT INTO SIGNATURES VALUES(?);''', params) 	# O(1)
		db.commit()
		return False
	except sqlite3.Error as e:
		return e

#-------------------------------------------------------------------------------------------------

# Delete a signature from the db 	O(1)
def delete_signature(signature):
	params = [signature]
	if(os.path.exists('./SIGNATURES.db')):
		try:
			db.execute('''DELETE FROM SIGNATURES WHERE SIGN=?''', params) 	# O(1) 
			db.commit()
			return False
		except sqlite3.Error as e:
			return e
	else:
		return "Database Not Found"

#-------------------------------------------------------------------------------------------------

# Check if the signature is in the db 		O(1)
def check_signature_in_db(signature):
	params = [signature]
	query = db.execute('''SELECT * FROM SIGNATURES WHERE SIGN=?;''', params) 	# O(1)
	res = query.fetchall()
	if(len(res) == 0):
		return False
	else:
		return True

#-------------------------------------------------------------------------------------------------

# Get all signatures from the db 		O(N)
def get_all_signatures():
	signs = []
	query = db.execute('''SELECT * FROM SIGNATURES ''') 	# O(N)
	rows = query.fetchall()
	for row in rows:
		signs.append(row[0])
	return signs

#-------------------------------------------------------------------------------------------------

# Mark a file as a virus 		O(M) M is number of blocks in hashing function
def mark_as_virus(file):
	file_sig = get_file_hash_sha256(file)	# O(M) M is number of blocks in hashing function
	result = add_signature(file_sig)	# O(1)
	return result

#-------------------------------------------------------------------------------------------------

# Unmark a file from being a virus 		O(M) M is number of blocks in hashing function
def unmark(file):
	file_sig = get_file_hash_sha256(file) 	# O(M) M is number of blocks in hashing function
	result = delete_signature(file_sig) 	# O(1)
	return result
