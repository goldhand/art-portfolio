# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import art-portfolio
version = art-portfolio.__version__

setup(
    name='art-portfolio',
    version=version,
    author='',
    author_email='will@django.nu',
    packages=[
        'art-portfolio',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['art-portfolio/manage.py'],
)