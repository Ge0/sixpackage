#!/usr/bin/env python3
from os.path import abspath, dirname, join

from pip.req import parse_requirements
from setuptools import find_packages, setup

CWD = dirname(abspath(__file__))


def requires():
    """Parse the requirements.txt file and generate a requirements list."""
    install_reqs = parse_requirements(join(CWD, 'requirements.txt'),
                                      session=False)
    return [str(ir.req) for ir in install_reqs]


setup(
    author='Geoffrey ROYER',
    author_email='geoffrey.royer@gmail.com',
    name='sixpackage',
    version="0.0.1",
    description='dumb package that should work on both python 2 and 3',
    url='https://github.com/Ge0/sixpackage',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=requires()
)
