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
    print(handler.get_information_set(identity))


if __name__ == "__main__":
    main()
