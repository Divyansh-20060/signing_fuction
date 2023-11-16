Steps to get started. Please read these steps very carefully before proceeding.
Once the keys are lost they can not be recovered. 
You will need the latest python interpetert and pip.

******* IF YOU ARE A NEW USER *******
1. Download latest python3 interpeter from https://www.python.org/
2. Download latest veriosn of pip from https://pypi.org/project/pip/
3. Install rsa by running "pip install rsa" in your command line.
4. Verify that you have got rsa and python3 interpeter

key_gen:
    first run 'python3 key_gen.py', it'll generate 'private.pem' and 'public.pem'
    in the current folder which will be used by the programs to sign and verify.
    re-running it will overwrite the current keys. PLEASE KEEP THIS FILE SAFE IT CANNOT BE RECOVRED.

to sign:
    run 'python3 sign.py filepath signer' signer can be 'admin', 'seller' or 'buyer'
    this function also prints the hexadecimal signture on the stdout which could
    be copy-pasted to while uploading signature for signing contracts.
    
to verify:
    run 'python3 verify.py filepath signer'
    here 'signer' is the one who you want to veriy the document as, should be 
    the same as the one used during signing inorder to be verified.
