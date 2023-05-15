from setuptools import setup, find_packages
import os



VERSION = '0.0.1'
DESCRIPTION = 'INI Initialization File'
LONG_DESCRIPTION = 'A package that allows to build simple class that operate over INI Files'

# Setting up
setup(
    name="ConfigFile",
    version=VERSION,
    author="SIMAO Nedved",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'INI', 'Files', 'Config Files'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
