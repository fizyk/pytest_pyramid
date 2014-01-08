import pytest
from webtest import TestApp


from pytest_pyramid import factories


def pytest_addoption(parser):
    parser.addoption(
        '--pc',
        action='store',
        default=None,
        metavar='path',
        dest='pyramid_config',
    )


pyramid_config = factories.pyramid_config()


@pytest.fixture
def pyramid_app(pyramid_config):

    app = TestApp(pyramid_config.make_wsgi_app())

    return app


# 5. make it also a factory
# 6. accept config file or settings dict.
