import sys
from pathlib import Path

from pre_commit.main import main as pre_commit_main


CDFILE = Path(__file__).parent / '.cooldown'


DEFAULT_COOLDOWN_HOURS = str(2**8)


COOLDOWN_NAMES = ['-C', '--cd', '--cooldown', '--cooldown-hours']


def _parse_argv():
    cooldown, args = DEFAULT_COOLDOWN_HOURS, sys.argv[1:]
    for i, arg in enumerate(args):
        if arg in COOLDOWN_NAMES and i + 1 < len(args):
            cooldown = args[i + 1]
            assert cooldown.isdigit()
            args = args[:i] + args[i + 2 :]
            break
        for name in COOLDOWN_NAMES:
            preifx = f'{name}='
            if arg.startswith(preifx):
                cooldown = arg.replace(preifx, '', 1)
                assert cooldown.isdigit()
                args = args[:i] + args[i + 1 :]
                break
    return int(cooldown), args


def main():
    cooldown, args = _parse_argv()
    print(f'{cooldown = }')
    print(f'{args = }')
    return  # pre_commit_main(['autoupdate'] + args)


if __name__ == '__main__':
    main()
