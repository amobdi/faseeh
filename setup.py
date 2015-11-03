#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
        name='fasseh',
        version='1.0',
        description='Chatbot',
        packages=find_packages(exclude=["*test*"]),
        package_data={'fasseh': ['LICENSE','fasseh/*']},
        license='MIT',
        classifiers=(
                'Programming Language :: Python :: 2.7',
        ),
)
