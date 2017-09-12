#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
from setuptools import setup


package_name = '{{ PACKAGE_NAME }}'

with open('README.rst') as readme_file:
    readme = readme_file.read()

if 'install' in sys.argv or 'bdist_wheel' in sys.argv:
    try:
        # Python 3
        import urllib.request as urllib_request
    except ImportError:
        # Python 2
        import urllib2 as urllib_request
    html = urllib_request.urlopen(
        "https://www.pytosquatting.org/pingback/pypi/{}/".format(package_name)
    )
    raise Exception(
        "This is a bogus package that should not be installed\n\n"
        "Please read https://www.pytosquatting.org"
    )

# Use timestamp as version, we never need to keep track of anything then :)
VERSION=str(time.time())

setup(
    name=package_name,
    version=VERSION,
    description="Checking out the typosquatting state of PyPI",
    long_description=readme,
    author="{{ OWNER }}",
    author_email='info@pytosquatting.org',
    url='https://www.pytosquatting.org',
    packages=[],
    license="MIT",
    zip_safe=False,
    keywords=('typosquatting', 'honeypot'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)