# Copyright (c) 2013 by pytest_pyramid authors and contributors
# <see AUTHORS file>
#
# This module is part of pytest_pyramid and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
"""Plugin's definition and basic fixtures."""

from pytest_pyramid import factories


def pytest_addoption(parser):
    """Pytest option configurator."""
    parser.addoption(
        '--pc',
        action='store',
        default=None,
        metavar='path',
        dest='pyramid_config',
    )


# fixtures (made out of factories)
pyramid_config = factories.pyramid_config()
pyramid_app = factories.pyramid_app('pyramid_config')
