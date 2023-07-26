from pathlib import Path

from New_make_f import new_make_file
from Task_hw import rename_file
from Make_f import make_file

if __name__ == '__main__':
    rename_file(5, 'bin', 'txt', 2, 4, 'master')

    make_file('bin', count=10)

    data = {
        'txt': 7,
        'zip': 2,
    }

    new_make_file(data)