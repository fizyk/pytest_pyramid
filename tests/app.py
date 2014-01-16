
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings)
    return config
