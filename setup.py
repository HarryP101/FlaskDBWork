#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:58:32 2019

@author: Harry
"""

from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'requests'
]

setup(
    name='FlaskDBWork',
    version='0.0',
    description='A currency rate ingester built with Flask',
    author='Harry Prudden',
    author_email='htprudden@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)