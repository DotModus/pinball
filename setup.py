#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pinball import __version__
from setuptools import setup


setup(
    name='pinball',
    version=__version__,
    description='Workflow manager and scheduler',
    author='Pawel Garbacki, Changshu Liu',
    author_email='pawel@pinterest.com, csliu@pinterest.com',
    url='https://github.com/pinterest/pinball',
    packages=[
        'pinball',
        'pinball.authentication',
        'pinball.common',
        'pinball.config',
        'pinball.master',
        'pinball.master.thrift_lib',
        'pinball.parser',
        'pinball.persistence',
        'pinball.scheduler',
        'pinball.tools',
        'pinball.ui',
        'pinball.workflow',
        'pinball_ext',
        'pinball_ext.common',
        'pinball_ext.examples',
        'pinball_ext.executor',
        'pinball_ext.job',
        'pinball_ext.workflow',
        'tests',
        'tests.pinball',
        'tests.pinball.authentication',
        'tests.pinball.config',
        'tests.pinball.master',
        'tests.pinball.parser',
        'tests.pinball.persistence',
        'tests.pinball.scheduler',
        'tests.pinball.tools',
        'tests.pinball.ui',
        'tests.pinball.workflow',
        'tests.pinball_ext',
        'tests.pinball_ext.executor',
        'tests.pinball_ext.job',
        'tests.pinball_ext.workflow',
    ],
    package_dir={'pinball': 'pinball'},
    include_package_data=True,
    install_requires=[
        'argparse>=1.2.1',
        'boto>=2.8.0',
        'Django>=1.5.4,<2.3.0',
        'guppy>=0.1.10',
        'mock>=0.8.0',
        'MySQL-python>=1.2.3',
        'oauth2client>=1.2',
        'pycrypto>=2.6',
        'pydot2>=1.0.33',
        'python-dateutil>=2.4',
        'PyTrie>=0.1',
        'pytz>=2013b',
        'pyyaml>=3.11',
        'qds_sdk>=1.9.0',
        'thrift>=0.8.0',
        'tox>=1.6.1',
    ],
    license="Apache 2.0",
    zip_safe=False,
    keywords='pinball, workflow manager, batch, job, hadoop, emr, qubole',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Distributed Computing',
    ],
    test_suite='tests',
)
