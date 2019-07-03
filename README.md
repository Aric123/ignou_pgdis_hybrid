# Secure-File-Storage-Using-Hybrid-Cryptography 

## Objective: To Achieve a secure Platform for storing of files on Cloud using Hybrid Cryptography.</br>

# Methodology
To achieve the above goal, the following methodology been followed:</br>
1. Load the file on the server.</br>
2. Dividing the uploaded file into N parts, Where N depends on the Buffer Size of the uploaded file </br>
3. Encrypting all the parts(N- numbers) of the file using any one of the selected algorithms 
(Algorithm is changed with every part in round robin fashion).</br>
4. The keys for cryptography algorithms is then secured using a different algorithm and the key for this algorithm is 
provided to the user as public key.</br>
5. The Key for cryptography Algorithms is been sent to user's email id</br>

After the above 4 steps you will have a N files which are in encrypted form which are stored on the server and a key 
which is downloaded as public key for decrypting the file and downloading it.</br>

To restore the file, follow the following steps:</br>
1. Load the key on the server.</br>
2. Decrypt the keys of the algorithms.</br>
3. Decrypt all the N parts of the file using the same algorithms which were used to encrypt them.</br>
4. Combine all the N parts to form the original file and provide it to the user for downloading.</br>

# How to Run

**NOTE:** The project is based on Python 2.7.15 platform running it on any other platform might create some issues.</br>

Step 1: Install Requirements</br>
`pip install -r requirements.txt`</br>

Step 2: Run the application</br>
`sudo python app.py`</br>

Step 3: Visit the localhost from your browser</br>
Default URL is given is 0.0.0.0 and Port is 80, which is good for Production environment as well. 
 
Step 4: Enjoy :-0

**IF YOU ENCOUNTER ANY BUGS OR FOR ANY SUGGESTIONS REGARDING THE IMPROVEMENT OF THE PROJECT FEEL FREE TO CONTACT ME :**

Abhishek Kumar<br/>
hello@kumarabhi.com<br/>
abhishek.ricky88@gmail.com
"""
