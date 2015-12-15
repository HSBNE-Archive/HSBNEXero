#!/usr/bin/env python3
import io
import re
from setuptools import setup

# Python's cryptography builds a binary from C using libffi-dev
#sudo apt-get install build-essential libssl-dev libffi-dev python-dev
setup(
    name='HSBNEXero',
    version='0.1.0',
    description='Reporting tool from Xero for HSBNE.org.',
    author='Brendan Carmichael',
    author_email='brendancarmichael@gmail.com',
    url='',
    install_requires=[
        'PyCrypto',
        'pyxero>=0.7.0',
        'PyJWT',
    ],

)


