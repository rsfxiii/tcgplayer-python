from setuptools import config, setup

import os

if __name__ == '__main__':
    confpath = f'{os.getcwd()}/setup.cfg'
    config.read_configuration(confpath)
    setup()
