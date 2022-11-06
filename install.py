from typing import List
from sys import platform
import pip

common = [
    'numpy',
    'pandas',
    'jupyter',
    'matplotlib',
]

windows = [
    # add any windows specific packages here
]

darwin = [
    # add any macOS specific packages here
]

linux = [
    # add any linux specific packages here
]


def install(packages: List[str]) -> None:
    for package in packages:
        pip.main(['install', package])


if __name__ == '__main__':
    install(common)
    if platform == 'windows':
        install(windows)
    elif platform == 'darwin':
        install(darwin)
    elif platform == 'linux':
        install(linux)
