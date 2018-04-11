import base64
import getpass
from pathlib import Path
import uuid

import os
import pyotp
import json

import simplecrypt
from simplecrypt import encrypt, decrypt


class Encryptor:

    def __init__(self, password):
        self.password = password

    def encrypt(self, data):
        return encrypt(self.password, data)

    def decrypt(self, data):
        return decrypt(self.password, data)


class SecretHandler:

    def __init__(self, password, base_path=None):
        if base_path is None:
            self.base_path = '{}/.config/bismarck/passwords'.format(str(Path.home()))
        self.encryptor = Encryptor(password)
        if not os.path.exists(self.base_path):
            self.information = {}
            self._save()
        else:
            self.information = self._get_information()

    def get_information_set(self, identification):
        return self.information.get(identification, None)

    def insert_information_set(self, identification, **kwargs):
        self.information[identification] = kwargs
        self._save()

    def remove_information_set(self, identification):
        self.information.pop(identification)
        self._save()

    def _get_information(self):
        with open(self.base_path, 'rb') as mf:
            try:
                return json.loads(str(self.encryptor.decrypt(mf.read()), 'utf-8'))
            except simplecrypt.DecryptionException as e:
                raise ValueError('Password provided is wrong', e)

    def _save(self):
        with open(self.base_path, 'wb') as mf:
            mf.write(self.encryptor.encrypt(bytes(json.dumps(self.information), 'utf-8')))
