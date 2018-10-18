import os
import io
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()

setup(
    name='traitlets_paths',
    version='0.1.1',
    author='Zach Sailer',
    author_email='zachsailer@gmail.com',
    description='Traitlets module for pathlib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zsailer/traitlets_paths',
    packages=find_packages(exclude=('tests',)),
    install_requires=['traitlets'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
