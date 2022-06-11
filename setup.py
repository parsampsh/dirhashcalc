#!/usr/bin/env python3

import setuptools
from dirhashcalc import VERSION

readme_f = open('README.md', 'r')
long_description = readme_f.read()
readme_f.close()

setuptools.setup(
    name="dirhashcalc",
    version=VERSION,
    author="Parsa Shahmaleki",
    author_email="parsampsh@gmail.com",
    description="Calculate directory hash",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parsampsh/dirhashcalc",
    packages=setuptools.find_packages(),
    scripts=['bin/dirhashcalc'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
