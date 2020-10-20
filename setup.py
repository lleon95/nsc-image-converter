# Copyright 2020 - NanoSciTracker
# Author: Luis G. Leon Vega <luis@luisleon.me>

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nscy_img_converter",
    version="0.1.0",
    author="Luis G. Leon-Vega",
    author_email="luis@luisleon.me",
    description="12-bit tiff to 8-bit png image converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mhpc/nanoscitracker-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'opencv-python',
          'Sphinx',
          'rinohtype',
          'recommonmark'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.8',
)
