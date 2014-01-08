
from webtest import TestApp
from pyramid.config import Configurator
from pytest_pyramid import factories


def test_pyramid_app(pyramid_app):
    '''
    Simple test to make sure we have everything needed for pyramid integration tests running
    '''

    assert isinstance(pyramid_app, TestApp)

    res = pyramid_app.get('/', status=404)
    assert res.status_code == 404


pyramid_config_path = factories.pyramid_config(config_path='tests/pyramid.test.ini')
pyramid_config_settings = factories.pyramid_config(settings={'env': 'pytest'})


def test_pyramid_config(pyramid_config, pyramid_config_path):
    '''
    Test whether both fixtures are generated correctly
    '''
    assert isinstance(pyramid_config, Configurator)
    assert isinstance(pyramid_config_path, Configurator)
    assert pyramid_config_path != pyramid_config
    assert pyramid_config_path.registry.settings == pyramid_config.registry.settings


def test_pyramid_config_settings(pyramid_config_settings):
    '''
    Test checking creating Configurator based on settings
    '''
    assert isinstance(pyramid_config_settings, Configurator)
    assert 'env' in pyramid_config_settings.registry.settings
    assert pyramid_config_settings.registry.settings['env'] == 'pytest'
