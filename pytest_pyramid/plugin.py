import pytest
from pytest_pyramid.compat import configparser


def pytest_addoption(parser):
    parser.addoption(
        '--pc',
        action='store',
        default=None,
        metavar='path',
        dest='pyramid_config',
    )


@pytest.fixture
def pyramid_app(request):
    config_file = request.config.getvalue('pyramid_config')
    # TODO
    # 1. Read man section of config file
    # 2. Get the settings dict
    # 3. Get the app setting and discover main entrypoint
    # 4. Run it as main include


# 5. make it also a factory
# 6. accept config file or settings dict.
