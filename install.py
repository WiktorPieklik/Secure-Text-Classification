from typing import List
from sys import platform, executable
from subprocess import check_call

common = [
    'numpy',
    'pandas',
    'jupyter',
    'matplotlib',
    'scikit-learn',
    'tensorflow-addons',
    'livelossplot',
]

windows = [
    # add any windows specific packages here
]

darwin = [
    'tensorflow-macos',
    'tensorflow-metal'
]

linux = [
    # add any linux specific packages here
]


def install(packages: List[str]) -> None:
    for package in packages:
        check_call([executable, '-m', 'pip', 'install', '--no-cache-dir', package])


if __name__ == '__main__':
    install(common)
    if platform == 'windows':
        install(windows)
    elif platform == 'darwin':
        install(darwin)
    elif platform == 'linux':
        install(linux)
