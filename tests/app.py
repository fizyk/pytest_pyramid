"""Define dummy app for tests."""

from typing import Any, Dict

from pyramid.config import Configurator


def main(global_config: Dict[str, Any], **settings: Dict[str, Any]) -> Configurator:
    """App configurator."""
    return Configurator(settings)
