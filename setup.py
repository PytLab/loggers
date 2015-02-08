#!/usr/bin/env python
'''A Python library for automatic logging in some websites with other functions'''

from distutils.core import setup
from loggers import __version__ as version

maintainer = 'ShaoZhengjiang'
maintainer_email = 'shaozhengjiang@gmail.com'
author = maintainer
author_email = maintainer_email
long_description = file('README.txt').read()
name='python-loggers'
packages = [
           'loggers',
           'loggers/ecust_logger',
           'loggers/emuch_logger'
           ]
platforms = ['linux', 'windows']

setup(
      author=author,
      author_email=author_email,
      long_description=long_description,
      maintainer=maintainer,
      maintainer_email=maintainer_email,
      name=name,
      packages=packages,
      platforms=platforms,
      version=version,
      )
