#! python
from setuptools import setup, find_packages

setup(
    name = "trowl",
    version = "0.0.1",
    package_dir = {'': 'src'},
    packages = ["trowl"],
    
    author = "David Schoonover",
    author_email = "dsc@less.ly",
    description = "trowl",
    long_description = """ A python web scraper framework. """,
    url = "http://github.com/dsc/trowl",
    
    zip_safe = False,
    
    classifiers = [],
)

