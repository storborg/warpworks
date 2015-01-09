from __future__ import print_function

import os
import sys
from setuptools import setup, find_packages


PY3 = sys.version_info[0] > 2

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyramid>=1.4.5',
    'SQLAlchemy>=0.8.2',
    'alembic>=0.6.7',
    'transaction>=1.4.3',
    'pyramid_tm>=0.7',
    'pyramid_debugtoolbar>=2.2',
    'pyramid_frontend>=0.4.1',
    'pyramid_uniform>=0.3',
    'pyramid_es>=0.3.0',
    'pyramid_mailer>=0.13',
    'pyramid_exclog>=0.7',
    'pyramid_cron>=0.1',

    'zope.sqlalchemy>=0.7.3',
    'waitress>=0.8.7',
    'webhelpers2>=2.0b5',
    'cryptacular>=1.4.1',
    'pymysql>=0.6.2',
    'premailer>=1.13',
    'gimlet>=0.5',
    'requests>=2.3.0',
    'lxml>=3.2.3',
    'Markdown>=2.5.2',

    # Keep repoze.sendmail pinned at 4.1 to deal with this bug:
    # https://github.com/repoze/repoze.sendmail/issues/31
    'repoze.sendmail==4.1',

    'pyweaving',
]


if not PY3:
    # Needed for uwsgi deployment with ini-paste-logged.
    requires.append('PasteScript>=1.7.5')
    requires.append('FormEncode>=1.2')
else:
    requires.append('FormEncode>=1.3.0a1')


setup(name='warpworks',
      version='0.0',
      description='A Browser Based Weaving Draft Editor',
      long_description='',
      classifier=[
          'Development Status :: 2 - Pre-Alpha'
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          # 'Programming Language :: Python :: 3',
          # 'Programming Language :: Python :: 3.3',
          # 'Programming Language :: Python :: 3.4',
          'Framework :: Pyramid',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Multimedia :: Graphics',
      ],
      url='http://github.com/storborg/warpworks',
      keywords='',
      author='Scott Torborg',
      author_email='storborg@gmail.com',
      install_requires=requires,
      license='MIT',
      packages=find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [paste.app_factory]
      main = warpworks.main:main
      [console_scripts]
      initialize_warpworks_db = warpworks.scripts.initializedb:main
      """,
      )
