"""Define dummy app for tests."""
from typing import Dict, Any

from pyramid.config import Configurator


def main(
    global_config: Dict[str, Any], **settings: Dict[str, Any]
) -> Configurator:
    """App configurator."""
    return Configurator(settings)
