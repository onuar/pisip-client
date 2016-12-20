import rsa
import os.path
import base64


def sign(message):
    file_exist = os.path.isfile('privateKey.pem')
    if not file_exist:
        raise IOError('privateKey.pem not found in root folder.')

    with open('privateKey.pem') as priv_file:
        data = priv_file.read()
    priv_key = rsa.PrivateKey.load_pkcs1(data)
    signature = rsa.sign(message.encode('utf-8'), priv_key, 'SHA-1')
    signature_value = base64.b64encode(signature)
    return signature_value


def get_signature():
    signature = sign('2373665e-367b-4086-ac08-3849dab94006')
    return signature
