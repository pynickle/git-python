import os
from setuptools import setup, find_packages
        

setup(
    name="git-python",
    version="1.1.2",
    description="combination and simplification of some useful git commands",
    long_description = open("README.rst").read(),
    author='code-nick-python',
    author_email='2330458484@qq.com',
    url="https://github.com/pynickle/git-python",
    packages=find_packages(),
    platforms="any",
    py_modules=['main'],
    install_requires=[
        'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'gp = main:parser_gp',
        ],
    }
)
