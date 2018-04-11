import getpass

import sys
sys.path.append('src')
from bismarck.security.security import SecretHandler


def main():
    while True:
        try:
            handler = SecretHandler(getpass.getpass(prompt='Password: '))
            break
        except ValueError:
            pass

    identity = input("What's the group name? ")
    data = {key: val for key, val in get_next_arg()}
    handler.insert_information_set(identity, **data)


def get_next_arg():
    while True:
        yield get_validated('Key Name'), get_validated('Value')
        more = input('Another? (y/n) ')
        if more.lower() != 'y':
            break


def get_validated(prompt):
    key_name = None
    check = None
    while check is None or check != key_name:
        key_name = getpass.getpass('{}? '.format(prompt))
        check = getpass.getpass('{} again? '.format(prompt))
    return key_name


if __name__ == "__main__":
    main()
