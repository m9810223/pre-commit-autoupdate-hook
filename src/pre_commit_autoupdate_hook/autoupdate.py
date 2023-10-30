import sys

from pre_commit.main import main as pre_commit_main


def main():
    pre_commit_main(['autoupdate'] + sys.argv[1:])


if __name__ == '__main__':
    main()
