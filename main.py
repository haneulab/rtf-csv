from src import config, setup
from src.modules import sys, path, test, build
from sys import argv


def main() -> None:

    print("config.path : ", config.paths())
    print("setup.resovle : ", setup.resolve(config.paths()['data']))
    try:
        run_type = sys.parse(argv[1])
        if not run_type:
            return
        if run_type == "build":
            build.process()
        elif run_type == "test":
            test.compare()

    except IndexError:
        sys.parse()


if __name__ == "__main__":
    main()
