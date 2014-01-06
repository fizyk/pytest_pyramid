import pytest
from pyramid.config import Configurator
from webtest import TestApp
try:
    from ConfigParser import ConfigParser
except ImportError:  # py3
    from configparser import ConfigParser


def pytest_addoption(parser):
    parser.addoption(
        '--pc',
        action='store',
        default=None,
        metavar='path',
        dest='pyramid_config',
    )


class App(object):

    def __init__(self, app, config):
        self.app = app
        self.config = config


@pytest.fixture
def pyramid_app(request):
    config_file = request.config.getvalue('pyramid_config')
    config = ConfigParser()
    config.read(config_file)
    settings = {}
    for option, value in config.items('app:main'):
        settings[option] = value

    config = Configurator(settings=settings)
    app = TestApp(config.make_wsgi_app())

    return App(app, config)


# 5. make it also a factory
# 6. accept config file or settings dict.
