#In my case, I chose hashlib to generate hashes
import hashlib

#You can use hashes to crack passwords that are more efficient, for example Zip and Winrar File Burteforce use hashes that are more efficient.
target = "61b4a64be663682e8cb037d9719ad8cd"

#To check passwords between 0 and 1000, use a for loop
for i in range(0,1000):
    #Passwords are stored in a variable called password string
    password = str(i)

    #Generate a hash with a password, and if the password matches, the same target hash will be generated
    hashed = hashlib.md5(password.encode()).hexdigest()

    #If hash equals target_hash, then password found, so we crack it
    if hashed == target:
        #Finally print the password
        print(f"Passowrd Found :{i}")
        break
