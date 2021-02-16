"""pytest_pyramid's installation file."""
from setuptools import setup


setup(
    entry_points={"pytest11": ["pytest_pyramid = pytest_pyramid.plugin"]},
)
