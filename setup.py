from setuptools import setup, find_packages

setup(
    name='traitlets_paths',
    version='0.1.0',
    author='Zach Sailer',
    author_email='zachsailer@gmail.com',
    description='Traitlets module for pathlib.',
    packages=find_packages(exclude=('tests',)),
    install_requires=['traitlets'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)