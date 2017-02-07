# Copyright (c) 2013 by pytest_pyramid authors and contributors
# <see AUTHORS file>
#
# This module is part of pytest_pyramid and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
"""Pytest's fixture factories."""

import os
import pytest
from webtest import TestApp
from pyramid.config import Configurator
try:
    from ConfigParser import ConfigParser
except ImportError:  # py3
    from configparser import ConfigParser


def pyramid_config(settings=None, config_path=None):
    """
    A pyramid_config fixture factory.

    Used to create aditional fixtures returning pyramid's
    :class:`~pyramid.config.Configurator` object.

    :param dict settings: optional parameter delivering settings for building
        a Configurator object.
    :param str config_path: optional parameter delivering path to pyramid
        configuration file

    :returns: configuration
    :rtype: `pyramid.config.Configurator`
    """
    @pytest.fixture(scope='session')
    def pyramid_config(request):
        app_settings = settings
        if app_settings is None:

            def load_settings(cpath, io_settings):
                config_parser = ConfigParser()
                config_parser.read(cpath)

                use = config_parser.get('app:main', 'use')
                if use and use.startswith('config:'):
                    base = os.path.dirname(cpath)
                    filename = use.replace('config:', '').strip()
                    sub_path = os.path.join(base, filename)
                    load_settings(os.path.abspath(sub_path), io_settings)

                for option, value in config_parser.items('app:main'):
                    io_settings[option] = value

            # load the application settings
            app_settings = {}
            cpath = config_path or request.config.getvalue('pyramid_config')
            load_settings(cpath, app_settings)

        return Configurator(settings=app_settings)

    return pyramid_config


def pyramid_app(config_fixture_name):
    """
    pyramid_app fixture factory.

    Creates a TestApp instance based on.

    :param str config_fixture_name: name of a fixture creating
        :class:`pyramid.config.Configurator`

    :returns: TestApp based on pyramid's COnfigurator object as returned from
        fixture passed by  **config_fixture_name**
    :rtype: webtest.app.TestApp
    """
    @pytest.fixture
    def pyramid_app(request):
        config = request.getfuncargvalue(config_fixture_name)

        app = TestApp(config.make_wsgi_app())

        return app

    return pyramid_app
