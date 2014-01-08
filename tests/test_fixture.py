
from webtest import TestApp
from pyramid.config import Configurator


def test_pyramid_app(pyramid_app):
    '''
    Simple test to make sure we have everything needed for pyramid integration tests running
    '''

    assert isinstance(pyramid_app, TestApp)

    res = pyramid_app.get('/', status=404)
    assert res.status_code == 404


def test_pyramid_config(pyramid_config):
    assert isinstance(pyramid_config, Configurator)
