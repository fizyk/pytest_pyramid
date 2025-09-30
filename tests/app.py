"""Define a dummy app for tests."""

from typing import Any

from pyramid.config import Configurator


def main(global_config: dict[str, Any], **settings: dict[str, Any]) -> Configurator:
    """App configurator."""
    return Configurator(settings)
