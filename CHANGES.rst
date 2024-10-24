CHANGES
=======

.. towncrier release notes start

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

- `#422 <https://https://github.com/fizyk/pytest_pyramid/issues/422>`_
- Do not install black on python versions older than 3.12


1.0.3 (2023-10-11)
==================

Features
--------

- Add support for Python 3.12 (`#388 <https://https://github.com/fizyk/pytest_pyramid/issues/388>`_)


Miscellaneus
------------

- `#339 <https://https://github.com/fizyk/pytest_pyramid/issues/339>`_, `#357 <https://https://github.com/fizyk/pytest_pyramid/issues/357>`_, `#359 <https://https://github.com/fizyk/pytest_pyramid/issues/359>`_, `#385 <https://https://github.com/fizyk/pytest_pyramid/issues/385>`_


1.0.2 (2022-12-13)
==================

Bugfixes
--------

- Fixed issue where pyramid_config option wasn't being properly read from ini file. (`#314 <https://https://github.com/fizyk/pytest_pyramid/issues/314>`_)


Features
--------

- Add Python 3.11 to the list of supported python versions. (`#309 <https://https://github.com/fizyk/pytest_pyramid/issues/309>`_)


Miscellaneus
------------

- Added project urls to display on pypi page (`#305 <https://https://github.com/fizyk/pytest_pyramid/issues/305>`_)
- Use towncrier to manage news fragments and changelog (`#307 <https://https://github.com/fizyk/pytest_pyramid/issues/307>`_)
- Migrate dependency management into pipenv (`#308 <https://https://github.com/fizyk/pytest_pyramid/issues/308>`_)
- Migrate versioning tool to tbump (`#311 <https://https://github.com/fizyk/pytest_pyramid/issues/311>`_)
- Migrate automerge action to a shared workflow (`#312 <https://https://github.com/fizyk/pytest_pyramid/issues/312>`_)
- Changed project structure. Moved package out of src into root.

  This will help testing and running code under pipenv/pipfile
  which has problems installing package placed in subdirectory,
  while having package definition on the same place as pipfile. (`#314 <https://https://github.com/fizyk/pytest_pyramid/issues/314>`_)
- Migrate project configuration from setup.cfg to pyproject.toml, dropped setup.py (`#315 <https://https://github.com/fizyk/pytest_pyramid/issues/315>`_)


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
