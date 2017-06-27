"""Define dummy app for tests."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """App configurator."""
    config = Configurator(settings)
    return config
