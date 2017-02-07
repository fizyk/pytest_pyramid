"""pytest_pyramid's installation file."""

import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


def read(fname):
    """Read file into string."""
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
    version='0.3.0',
    description='pytest pyramid providing basic fixtures for testing ' +
    'pyramid applications with pytest test suite',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
