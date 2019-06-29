#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='locate-darkness',
    version='1.0',
    description="Locate image file that have already been processed and move them to a directory.",
    author="Visgean",
    author_email='visgean@gmail.com',
    url='https://github.com/visgean/locate-darkness',
    packages=[
        'darkness',
    ],
    package_dir={'locate-darkness': 'locate-darkness'},
    license="MIT",
    keywords='image processing',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'locate-darkness = darkness.main:main'
        ]
    },
)