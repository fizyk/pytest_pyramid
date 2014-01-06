
from webtest import TestApp
from pyramid.config import Configurator


def test_pyramid_app(pyramid_app):
    '''
    Simple test to make sure we have everything needed for pyramid integration tests running
    '''

    app = pyramid_app.app
    config = pyramid_app.config

    assert isinstance(app, TestApp)
    assert isinstance(config, Configurator)

    res = pyramid_app.app.get('/', status=404)
    assert res.status_code == 404
