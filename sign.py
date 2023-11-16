import rsa
import sys
file_path = sys.argv[1]
def get_sign(private_key_bin, document_bin):##paths of the private key and the document to be signed
    ##load the private key into a variable
    private_key = rsa.PrivateKey.load_pkcs1(private_key_bin)

    ##get the file content and then the sign
    file_content = document_bin.split(b"signature:")[0]
    signature = rsa.sign(file_content, private_key, "SHA-512").hex()
    return signature


def main():
    signer = sys.argv[2]
    with open("private.pem", "rb") as f:
        private_key_bin = f.read()
    with open(file_path, "rb+") as f:
        document_bin = f.read()
        signature = get_sign(private_key_bin, document_bin)
        f.write(b"signature:")
        f.write(signer.encode())
        f.write(signature.encode())
        f.write(signer.encode())
        print(signature)

main()