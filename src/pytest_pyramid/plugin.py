# Copyright (c) 2013 by pytest_pyramid authors and contributors
#
# This module is part of pytest_pyramid and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
"""Plugin's definition and basic fixtures."""
from _pytest.config.argparsing import Parser

from pytest_pyramid import factories

_help_config = "Path to default config ini for tests"


def pytest_addoption(parser: Parser) -> None:
    """Pytest option configurator."""

    parser.addini(
        "pyramid_config",
        default=None,
        help=_help_config,
    )
    parser.addoption(
        "--pc",
        action="store",
        default=None,
        metavar="path",
        dest="pyramid_config",
        help=_help_config,
    )


# fixtures (made out of factories)
pyramid_config = factories.pyramid_config()
pyramid_app = factories.pyramid_app("pyramid_config")
