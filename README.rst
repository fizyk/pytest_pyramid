pytest_pyramid
==============

.. image:: https://travis-ci.org/fizyk/pytest_pyramid.png?branch=master
    :target: https://travis-ci.org/fizyk/pytest_pyramid
    :alt: Tests for RandomWords

.. image:: https://coveralls.io/repos/fizyk/pytest_pyramid/badge.png?branch=master
    :target: https://coveralls.io/r/fizyk/pytest_pyramid?branch=master
    :alt: Coverage Status

pytest_pyramid provides basic fixtures for testing pyramid applications with pytest test suite

TODO
====

There's a simple TODO list, providing goals to achieve before releasing this code to PyPI

# provide a config fixture that will read config from file
# provide a config factory, that will accept settings dict, a file path, or by default read config from pytest.options
# documentation

This goal should make it in to 1.0 major release.

# provide a pyramid_proc fixture that will start pyramid app process using summon_process


Tests
=====

To run tests run this command:

`py.test --pc tests/pyramid.test.ini`
