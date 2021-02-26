# Copyright (c) 2013 by pytest_pyramid authors and contributors
#
# This module is part of pytest_pyramid and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
"""Pytest's fixture factories."""

import os
from typing import Dict, Any, Callable

import pytest
from _pytest.fixtures import FixtureRequest
from webtest import TestApp
from pyramid.config import Configurator

from configparser import ConfigParser


def _load_settings(cpath: str, io_settings: Dict[str, Any]) -> None:
    config_parser = ConfigParser()
    config_parser.read(cpath)

    use = config_parser.get("app:main", "use")
    if use and use.startswith("config:"):
        base = os.path.dirname(cpath)
        filename = use.replace("config:", "").strip()
        sub_path = os.path.join(base, filename)
        _load_settings(os.path.abspath(sub_path), io_settings)

    for option, value in config_parser.items("app:main"):
        io_settings[option] = value


def pyramid_config(
    config_path: str = None, settings: Dict[str, Any] = None
) -> Callable[[FixtureRequest], Configurator]:
    """
    Pyramid_config fixture factory.

    Used to create aditional fixtures returning pyramid's
    :class:`~pyramid.config.Configurator` object.

    :param dict settings: optional parameter delivering settings for building
        a Configurator object.
    :param str config_path: optional parameter delivering path to pyramid
        configuration file

    :returns: configuration
    :rtype: `pyramid.config.Configurator`
    """

    @pytest.fixture(scope="session")
    def pyramid_config(request: FixtureRequest) -> Configurator:

        # load the application settings
        app_settings: Dict[str, Any] = {}
        if cpath := config_path or request.config.getvalue("pyramid_config"):
            _load_settings(cpath, app_settings)

        app_settings.update(settings if settings else {})
        return Configurator(settings=app_settings)

    return pyramid_config


def pyramid_app(
    config_fixture_name: str, *additional_fixtures: str
) -> Callable[[FixtureRequest], TestApp]:
    """
    pyramid_app fixture factory.

    Creates a TestApp instance based on.

    :param str config_fixture_name: name of a fixture creating
        :class:`pyramid.config.Configurator`

    :param List[str] additional_fixtures: list of any additional
        fixture names that should be loaded before the pyramid_app fixture.

    :returns: TestApp based on pyramid's COnfigurator object as returned from
        fixture passed by  **config_fixture_name**
    :rtype: webtest.app.TestApp
    """

    @pytest.fixture
    def pyramid_app(request: FixtureRequest) -> TestApp:
        for additional_fixture in additional_fixtures:
            request.getfixturevalue(additional_fixture)
        config = request.getfixturevalue(config_fixture_name)

        return TestApp(config.make_wsgi_app())

    return pyramid_app
