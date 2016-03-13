"""Setup."""
from setuptools import setup, find_packages
import sys
import os
import re


def read(fname):
    """read - read the named file and return it's content."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """get_version - return package version from in `__init__.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

requirements = map(str.strip, open("requirements.txt").readlines())

version = get_version('touchwood')

setup(name='touchwood',
      version=version,
      description="Python Touchwood REST API interface",
      long_description="",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
            'Programming Language :: Python',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
      ],
      keywords='Touchwood wrapper REST API',
      author='F. Brekeveld',
      license='GPLv3',
      packages=find_packages(exclude=['examples', 'tests']),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
