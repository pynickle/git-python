from setuptools import setup, find_packages
from setuptools.command.install import install                                      

class CustomInstall(install):                                                       
    def run(self):                                                                  
        install.run(self)                                                     
        
setup(
    name="git-python",
    version="1.0.3",
    description="combination and simplification of some useful git commands",
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
