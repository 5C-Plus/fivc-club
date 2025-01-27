#!/usr/bin/env python

import os
import subprocess

if __name__ == '__main__':
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # install dependencies
    # subprocess.call([
    #     'pip',
    #     'install',
    #     '-r',
    #     'requirements-dev.txt',
    # ], cwd=cwd)

    # format code
    subprocess.call([
        'autopep8',
        '-r',
        '--in-place',
        '--aggressive',
        '--aggressive',
        '--max-line-length=79',
        'modules',
    ], cwd=cwd)
    # check code style
    subprocess.call(['flake8', 'modules'], cwd=cwd)
    subprocess.call(['flake8', 'launchers'], cwd=cwd)
    # subprocess.call(['flake8', 'common'], cwd=cwd)
    # subprocess.call(['flake8', 'services'], cwd=cwd)

    # start unittest
    # subprocess.call(['python', 'manage.py', 'makemigrations'], cwd=cwd)
    # subprocess.call(['python', 'manage.py', 'test'], cwd=cwd)
