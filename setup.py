# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages

here = os.path.dirname(__file__)
with open(os.path.join(here, 'pytest_pyramid', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


def read(fname):
    return open(os.path.join(here, fname)).read()

requirements = [
    'pytest',
    'pyramid',
    'webtest'
]

tests_require = [
    'pytest-cov'
]

extras_require = {
    'docs': ['sphinx'],
    'tests': tests_require
}

setup(
    name='pytest_pyramid',
    version=package_version,
    description='pytest pyramid providing basic fixtures for testing ' +
    'pyramid applications with pytest test suite',
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
    ),
    keywords='pyramid pytest testing',
    author='Grzegorz Sliwinski',
    author_email='fizyk@fizyk.net.pl',
    url='https://github.com/fizyk/pytest_pyramid',
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    packages=find_packages(),
    install_requires=requirements,
    tests_require=tests_require,
    test_suite='tests',
    entry_points={
        'pytest11': [
            'pytest_pyramid = pytest_pyramid.plugin'
        ]},
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
)
