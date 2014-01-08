from pytest_pyramid import factories


def pytest_addoption(parser):
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


# 5. make it also a factory
# 6. accept config file or settings dict.
