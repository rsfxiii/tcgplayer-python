from setuptools import config, setup

import os

confpath = f'{os.getcwd()}/setup.cfg'
config.read_configuration(confpath)
setup()
