CHANGES
=======

.. towncrier release notes start

pytest-pyramid 1.1.1 (2026-09-05)
=================================

Miscellaneous
-------------

- Update pytest configuration to toml-native (`#632 <https://github.com/fizyk/pytest_pyramid/issues/632>`_)
- Add zizmor to pre-commit and address its findings. (`#731 <https://github.com/fizyk/pytest_pyramid/issues/731>`_)
- Add pyproject-fmt formatter to the pre-commit config. (`#732 <https://github.com/fizyk/pytest_pyramid/issues/732>`_)
- Migrate development environment to uv (`#733 <https://github.com/fizyk/pytest_pyramid/issues/733>`_)
- Add Python 3.15 to CI (`#734 <https://github.com/fizyk/pytest_pyramid/issues/734>`_)
- Enable `flake8-boolean-trap` linter (`#735 <https://github.com/fizyk/pytest_pyramid/issues/735>`_)
- Enable `tryceratops` linter (`#738 <https://github.com/fizyk/pytest_pyramid/issues/738>`_)
- Add release-schedule workflow. (`#739 <https://github.com/fizyk/pytest_pyramid/issues/739>`_)
- Enable `flake8-pytest-style` linter (`#740 <https://github.com/fizyk/pytest_pyramid/issues/740>`_)
- Migrated the Automerge workflow to `fizyk/actions-reuse` version 5.4.1. (`#744 <https://github.com/fizyk/pytest_pyramid/issues/744>`_)
- Configure Dependabot to update pre-commit dependencies. (`#748 <https://github.com/fizyk/pytest_pyramid/issues/748>`_)
- Improve test coverage by running tests through coverage module, not coverage as part of tests. (`#753 <https://github.com/fizyk/pytest_pyramid/issues/753>`_)


pytest_pyramid 1.1.0 (2025-09-30)
=================================

Breaking changes
----------------

- Drop support for Python 3.9


Features
--------

- Add support for Python 3.14


Miscellaneus
------------

- Adjust workflows for actions-reuse 3
- Migrate from black to ruff-format
- Use pre-commit for maintaining code style and linting


1.0.4 (2024-10-24)
==================

Breaking changes
----------------

- Drop support for Python 3.8 (Reached EOL)


Features
--------

- Add support for Python 3.13


Miscellaneus
------------

- `#422 <https://github.com/fizyk/pytest_pyramid/issues/422>`_
- Do not install black on python versions older than 3.12


1.0.3 (2023-10-11)
==================

Features
--------

- Add support for Python 3.12 (`#388 <https://github.com/fizyk/pytest_pyramid/issues/388>`_)


Miscellaneus
------------

- `#339 <https://github.com/fizyk/pytest_pyramid/issues/339>`_, `#357 <https://github.com/fizyk/pytest_pyramid/issues/357>`_, `#359 <https://github.com/fizyk/pytest_pyramid/issues/359>`_, `#385 <https://github.com/fizyk/pytest_pyramid/issues/385>`_


1.0.2 (2022-12-13)
==================

Bugfixes
--------

- Fixed issue where pyramid_config option wasn't being properly read from ini file. (`#314 <https://github.com/fizyk/pytest_pyramid/issues/314>`_)


Features
--------

- Add Python 3.11 to the list of supported python versions. (`#309 <https://github.com/fizyk/pytest_pyramid/issues/309>`_)


Miscellaneus
------------

- Added project urls to display on pypi page (`#305 <https://github.com/fizyk/pytest_pyramid/issues/305>`_)
- Use towncrier to manage news fragments and changelog (`#307 <https://github.com/fizyk/pytest_pyramid/issues/307>`_)
- Migrate dependency management into pipenv (`#308 <https://github.com/fizyk/pytest_pyramid/issues/308>`_)
- Migrate versioning tool to tbump (`#311 <https://github.com/fizyk/pytest_pyramid/issues/311>`_)
- Migrate automerge action to a shared workflow (`#312 <https://github.com/fizyk/pytest_pyramid/issues/312>`_)
- Changed project structure. Moved package out of src into root.

  This will help testing and running code under pipenv/pipfile
  which has problems installing package placed in subdirectory,
  while having package definition on the same place as pipfile. (`#314 <https://github.com/fizyk/pytest_pyramid/issues/314>`_)
- Migrate project configuration from setup.cfg to pyproject.toml, dropped setup.py (`#315 <https://github.com/fizyk/pytest_pyramid/issues/315>`_)


1.0.1
----------

- [packaging] Defined entrypoint in setup.cfg

1.0.0
----------

- [breaking] Changed order of the fixture factory parameters
- [breaking] Now, if config_path is given, it'll always be loaded,
  with settings extending it's configuration further.
- [breaking] Support only python 3.8 and up
- [enhancement] Updated packaging configuration
- [enhancement] Typed all the code

0.3.3
----------

- add additiona_fixtures to factories.pyramid_app

0.3.2
----------

- add pyramid_config ini option

0.3.1
----------

- fixed pytest deprecation warning

0.3.0
----------

- [feature] changed pyramid_config fixture scope to session.

0.2.0
----------

- [feature] support pyramid's config inheritance with use = config:other.file.ini - Thanks Eric Hulser
- [feature] dropped support for python 3.2, added support for python 3.4 and 3.5

0.1.1
-----
- make factories condition to check parameters against None

0.1.0
-----
- initial release
- pyramid_config fixture factory and default fixture
- pyramid_app fixture factory and default fixture
- documentation
