"""Testing fixtures."""

import pytest
from _pytest.fixtures import FixtureRequest
from pyramid.config import Configurator
from webtest import TestApp

from pytest_pyramid import factories

TestApp.__test__ = False


def test_pyramid_app(pyramid_app: TestApp) -> None:
    """Make sure we have everything needed for pyramid integration tests running.

    Check if:
    - app is an instance of TestApp
    - we get proper status code from a not defined route
    """
    assert isinstance(pyramid_app, TestApp)

    res = pyramid_app.get("/", status=404)
    assert res.status_code == 404


pyramid_config_path = factories.pyramid_config(config_path="tests/pyramid.test.ini")
pyramid_config_inheritance = factories.pyramid_config(config_path="tests/pyramid.use.test.ini")

pyramid_config_settings = factories.pyramid_config(settings={"env": "pytest"})


def test_pyramid_config(pyramid_config: Configurator, pyramid_config_path: Configurator) -> None:
    """Test whether both fixtures are generated correctly."""
    assert isinstance(pyramid_config, Configurator)
    assert isinstance(pyramid_config_path, Configurator)
    assert pyramid_config_path != pyramid_config
    assert pyramid_config_path.registry.settings == pyramid_config.registry.settings


def test_pyramid_config_settings(pyramid_config_settings: Configurator) -> None:
    """Test checking creating Configurator based on settings."""
    assert isinstance(pyramid_config_settings, Configurator)
    assert "env" in pyramid_config_settings.registry.settings
    assert pyramid_config_settings.registry.settings["env"] == "pytest"


def test_pyramid_inheritance_config(
    pyramid_config_path: Configurator, pyramid_config_inheritance: Configurator
) -> None:
    """Test reading inheriting config through pytest_pyramid.

    Given:
        - that one config inherits the other,
    When:
        - having an additional config option defined,
        and it is different from the inherited config defined
    Then:
        The final config will contain sum of cconfig options defined
        in both config, with the inheriting config having the highest
        priority values.
    """
    assert isinstance(pyramid_config_inheritance, Configurator)
    assert isinstance(pyramid_config_path, Configurator)

    assert (
        pyramid_config_inheritance.registry.settings["inheriting"] == "I do not really set anything"
    )
    assert "inheriting" not in pyramid_config_path.registry.settings

    assert (
        pyramid_config_inheritance.registry.settings["use"]
        != pyramid_config_path.registry.settings["use"]
    )

    assert (
        len(pyramid_config_inheritance.registry.settings)
        == len(pyramid_config_path.registry.settings) + 1
    )

    assert pyramid_config_inheritance.registry.settings["one_value"] == "1"


@pytest.fixture()
def dummy_fixture() -> None:
    """Return a dummy fixture that does nothing."""


pyramid_app_with_additional_fixtures = factories.pyramid_app("pyramid_config_path", "dummy_fixture")


def test_pyramid_app_with_additional_fixtures(
    pyramid_app_with_additional_fixtures: TestApp, request: FixtureRequest
) -> None:
    """Test that pyramid_app factory works with additional_fixtures.

    It checks if additional_fixtures are loaded for the test.
    """
    assert set(request.fixturenames) == {
        "pyramid_app_with_additional_fixtures",
        "request",
        "pyramid_config_path",
        "dummy_fixture",
    }
