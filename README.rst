.. image:: https://raw.githubusercontent.com/fizyk/pytest_pyramid/master/logo.png
    :width: 100px
    :height: 100px

pytest_pyramid
==============

.. image:: https://img.shields.io/pypi/v/pytest_pyramid.svg
    :target: https://pypi.python.org/pypi/pytest_pyramid/
    :alt: Latest PyPI version

.. image:: https://readthedocs.io/projects/pytest_pyramid/badge/?version=v1.0.1
    :target: http://pytest_pyramid.readthedocs.io/en/v1.0.1/
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

pytest_pyramid provides basic fixtures for testing pyramid applications with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config, which creates configurator based on config.ini file, and pyramid_app, which creates TestApp based on Configurator returned by pyramid_config.

Command line options
--------------------

* **--pc** - pyramid configuration file based on which pytest_pyramid will create test app

Usage
=====

For the most basic usage, pytest_pyramid provides pyramid_app and pyramid_config fixtures,
that can be used to test your pyramid app.
Simply pass your pyramid config ***.ini** file to **--pc** command-line option,
and include *pytest_app* fixture into your test suite to be able to use it for
integration tests.

Fixtures
--------

pytest_pyramid provides two fixtures to be used in pytest tests:

* **pyramid_config** - fixture providing pyramid's Configurator instance as
  defined in pyramid config's file
* **pyramid_app** - pyramid application for testing - a **webtest.app.TestApp**

Both of these fixtures depend on the Config file passed in the command line.


Fixture factories
-----------------

If you're developing a module, package meant to extend functionalities of other
applications, it's not necessary to create a full-blown application to test
functionalities provided in packages. To do this, **pytest_pyramid** provides
you with fixture **pytest_pyramid.factories**.

There are two factories:

* **pytest_pyramid.factories.pyramid_config** provides you with Configuration object based on either settings, config_file argument, or by --pc command-line option config file.
* **pytest_pyramid.factories.pyramid_app** creates a **webtest.app.TestApp** based on Configurator class instance as returned from fixture passed by name to it. It also accepts additional fixtures that should be loaded before the `pyramid_app`. See the example with `postgresql` below.

.. code-block:: python

    from pytest_postgresql.plugin import postgresql
    from pytest_pyramid import factories

    app_config = factories.pyramid_config(config_path="development.ini")
    app_with_postgres = factories.pyramid_app("app_config", "postgresql")

    def test_pyramid_app(app_with_postgres):
        res = app_with_postgres.get('/', status=404)
        assert res.status_code == 404


TODO
----

#. provide a pyramid_proc fixture that will start pyramid app process using summon_process


Tests
-----

To run tests run this command:

`pytest --pc tests/pyramid.test.ini`
