CHANGES
=======

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
