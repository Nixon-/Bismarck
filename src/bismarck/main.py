from multiprocessing import Process

from bismarck.disambiguation import SemanticAnalyzer
from bismarck.command_processor.service import CommandApi, Coordinator


def main():
    services = [CommandApi(), Coordinator(), SemanticAnalyzer()]
    process_pool = list()
    for service in services:
        process_pool.append(Process(target=service.start))
    for process in process_pool:
        process.start()
    for process in process_pool:
        process.join()


if __name__ == "__main__":
    main()
