pytest_pyramid
==============

.. image:: https://img.shields.io/pypi/v/pytest_pyramid.svg
    :target: https://pypi.python.org/pypi/pytest_pyramid/
    :alt: Latest PyPI version

.. image:: https://readthedocs.io/projects/pytest_pyramid/badge/?version=v0.3.0
    :target: http://pytest_pyramid.readthedocs.io/en/v0.3.0/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/wheel/pytest_pyramid.svg
    :target: https://pypi.python.org/pypi/pytest_pyramid/
    :alt: Wheel Status

.. image:: https://img.shields.io/pypi/pyversions/pytest_pyramid.svg
    :target: https://pypi.python.org/pypi/pytest_pyramid/
    :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/pytest_pyramid.svg
    :target: https://pypi.python.org/pypi/pytest_pyramid/
    :alt: License

Package status
--------------

.. image:: https://travis-ci.org/fizyk/pytest_pyramid.svg?branch=v0.3.0
    :target: https://travis-ci.org/fizyk/pytest_pyramid
    :alt: Tests

.. image:: https://coveralls.io/repos/fizyk/pytest_pyramid/badge.png?branch=v0.3.0
    :target: https://coveralls.io/r/fizyk/pytest_pyramid?branch=v0.3.0
    :alt: Coverage Status

.. image:: https://requires.io/github/fizyk/pytest_pyramid/requirements.svg?tag=v0.3.0
     :target: https://requires.io/github/fizyk/pytest_pyramid/requirements/?tag=v0.3.0
     :alt: Requirements Status

pytest_pyramid provides basic fixtures for testing pyramid applications with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config, which creates configurator based on config.ini file, and pyramid_app, which creates TestApp based on Configurator returned by pyramid_config.

Command line options
--------------------

* **--pc** - pyramid configuration file based on which pytest_pyramid will create test app

Documentation
-------------

http://pytest-pyramid.readthedocs.io/en/latest/

TODO
----

This goal should make it in to 1.0 major release.

#. provide a pyramid_proc fixture that will start pyramid app process using summon_process


Tests
-----

To run tests run this command:

`py.test --pc tests/pyramid.test.ini`
