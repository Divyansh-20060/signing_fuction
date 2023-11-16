import rsa

import sys
file_path = sys.argv[1]

def verify_doc(public_key_bin, document_bin, signer):
    try:
        public_key = rsa.PublicKey.load_pkcs1(public_key_bin)
        content = document_bin.split(b"signature:")[0]
        signature = document_bin.split(signer.encode())[-2]
        rsa.verify(content, bytes.fromhex(signature.decode()), public_key)
        return True
    except rsa.pkcs1.CryptoError as crypto_error:
        print(crypto_error)
        return False
    except Exception as e:
        print("error:", e)
        return False


def main():
    with open("public.pem", "rb") as f:
        public_key = f.read()
    with open(file_path, "rb") as f:
        document_bin = f.read()
    signer = sys.argv[2]
    if verify_doc(public_key, document_bin, signer):
        print("verified")
    else:
        print("verification failed")



main()