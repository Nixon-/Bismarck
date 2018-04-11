import getpass
from multiprocessing import Process

from bismarck.command_processor.modules.applications.chrome_service import ChromeService
from bismarck.command_processor.service import CommandApi, Coordinator
from bismarck.disambiguation.disambiguate import SemanticAnalyzer
from bismarck.security.security import SecretHandler


def main():
    while True:
        try:
            secret_handler = SecretHandler(getpass.getpass("What's the encryption password for your shit dawg? "))
            break
        except ValueError:
            print('Wrong pass')
    services = list()
    services.append(CommandApi())
    services.append(Coordinator())
    services.append(SemanticAnalyzer())
    # services.append(IoService())
    services.append(ChromeService(secret_handler))
    process_pool = list()
    for service in services:
        process_pool.append(Process(target=service.start))
    for process in process_pool:
        process.start()
    for process in process_pool:
        process.join()


if __name__ == "__main__":
    main()
