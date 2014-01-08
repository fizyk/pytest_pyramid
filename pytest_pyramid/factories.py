import pytest


from pyramid.config import Configurator
try:
    from ConfigParser import ConfigParser
except ImportError:  # py3
    from configparser import ConfigParser


def pyramid_config(settings=None, config_path=None):

    @pytest.fixture
    def pyramid_config(request):
        app_settings = settings
        if not app_settings:
            config_parser = ConfigParser()
            if not config_path:
                config_file = request.config.getvalue('pyramid_config')
                config_parser.read(config_file)
            else:
                config_parser.read(config_path)
            app_settings = {}
            for option, value in config_parser.items('app:main'):
                app_settings[option] = value

        return Configurator(settings=app_settings)

    return pyramid_config
