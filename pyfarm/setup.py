#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from setuptools import setup, find_packages
import sys
import os

try:
    from pip.req import parse_requirements
except ImportError:
    print("You must install the pip package before installing pyfarm")


version = '0.0.1'

setup(
    name='pyfarm',
    version=version,
    description="Simple tiled roguelike farm management game",
    long_description="""\
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
        'Programming Language :: Python :: 3.4',
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='dwarffortress roguelike game',
    author='seth wolfwood',
    author_email='seth@sethish.com',
    url='seth.wolfwood.is',
    license='GPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=parse_requirements('./requirements.txt'),
    entry_points={'console_scripts': [
        'pyfarm=pyfarm:main',
    ], }
)
