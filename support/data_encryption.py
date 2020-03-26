import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_buffer(_stream_buffer):
    __encoded_password = b'12345'
    __salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=__salt,
        iterations=100000,
        backend=default_backend()
    )

    __key = base64.urlsafe_b64encode(kdf.derive(__encoded_password))
    __fernet = Fernet(__key)
    __encrypted = __fernet.encrypt(_stream_buffer)
    return __encrypted


def encrypt_file(_password):
    _input_file = 'backdoor/text.txt'
    _output_file = 'backdoor/text.encrypted'

    _encoded_password = _password
    _salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=_salt,
        iterations=100000,
        backend=default_backend()
    )

    _key = base64.urlsafe_b64encode(kdf.derive(_password))

    file = open('backdoor/key.key', 'wb')
    file.write(_key)
    file.close()

    with open(_input_file, 'rb') as f:
        _data = f.read()

    fernet = Fernet(_key)
    _encrypted = fernet.encrypt(_data)

    with open(_output_file, 'wb') as f:
        f.write(_encrypted)

    return _encrypted


def decrypt():
    _input_file = 'backdoor/text.encrypted'
    _output_file = 'backdoor/text.decrypted'

    file = open('backdoor/key.key', 'rb')
    _key = file.read()
    file.close()

    with open(_input_file, 'rb') as f:
        _data = f.read()

    _fernet = Fernet(_key)
    _encrypted = _fernet.decrypt(_data)
    with open(_output_file, 'wb') as f:
        f.write(_encrypted)

    return _encrypted



