#!/usr/bin/env python
# 

from yurt import __appname__, __version__
from setuptools import setup

long_description = ""

setup(
    name=__appname__,
    version=__version__,
    packages=['yurt',],

    author="Paul Tagliamonte",
    author_email="tag@pault.ag",

    long_description=long_description,
    description='such yurt',
    license="GPLv3",
    url="https://github.com/paultag/yurt",

    platforms=['any']
)
