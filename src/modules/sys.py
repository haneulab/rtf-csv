from time import sleep
import sys


def error(type: str, message: str, middleware=None):
    print(f"{type}: {message}")
    if middleware:
        print(middleware)
    sys.exit(1)


def print_help() -> None:
    print("Build command: 'python main.py -b' or 'python main.py --build'")
    print("Test command: 'python main.py -t' or 'python main.py --test'")


def print_build() -> None:
    print("Build")


def print_test() -> None:
    print("Test")


def parse(type: str = None) -> int:
    if type is None:
        return error("ParseArgumentError",
                     "You must pass an argument when running main program.", "Run 'python main.py -h' or 'python main.py --help' to see possible flag options.")
    if type in ['-h', '--help']:
        #
        print_help()
        return "help"
    if type in ['-b', '--build']:
        #
        print_build()
        return "build"
    if type in ['-t', '--test']:
        #
        print_test()
        return "test"
    return error("ParseArgumentError",
                 "You must pass an argument when running main program.", "Run 'python main.py -h' or 'python main.py --help' to see possible flag options.")
