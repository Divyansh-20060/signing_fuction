#*************** Please Read ********************
# Make sure to keep the public and private keys * 
# in the same folder/directory as this file.    *
#                                               *
# set full path of the pdf file at line 12.     *
#                                               *
# enter your user type buyer or seller          *
# at line 31 and 33.                            *
#*************** Please Read ********************

import rsa
file_path = "" #set the path of the cotract to signing. For example "path/to/file.pdf"

def get_sign(private_key_bin, document_bin):##paths of the private key and the document to be signed
    ##load the private key into a variable
    private_key = rsa.PrivateKey.load_pkcs1(private_key_bin)

    file_content = document_bin.split(b"signature:")[0]
    signature = rsa.sign(file_content, private_key, "SHA-512").hex()
    return signature



def main():
    with open("private.pem", "rb") as f:
        private_key_bin = f.read()
    with open(file_path, "rb+") as f:
        document_bin = f.read()
        signature = get_sign(private_key_bin, document_bin)
        f.write(b"signature:")
        f.write(b"") # your user type buyer or seller in "". For example "buyer", "seller".
        f.write(signature.encode())
        f.write(b"") # your user type buyer or selle in "". For example "buyer", "seller".
        print(signature)
        print(len(signature))

main()