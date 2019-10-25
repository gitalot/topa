#!/usr/bin/env python
# coding: utf-8
import pathlib

from setuptools import setup
from topa import VERSION

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='topa',
    version=VERSION,
    author='JIANG Wenjian',
    author_email='wenjian.jiang@foxmail.com',
    url='https://github.com/jwenjian/topa',
    description=README,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    packages=['topa'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'topa=topa:main'
        ]
    }
)
