#!/usr/bin/env python
# yapf

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

test_requires = {
    'altered-states==1.0.9',
    'hypothesis==4.24.3',
    'mock==2.0.0',
    'pytest-cov==2.5.1',
    'pytest==4.3.1',
}  # yapf: disable

setup(
    name='determinist',
    version="0.1.0",
    description="Finite state machines nicely expressed using decorators.",
    package=('determinist', ),
    author='Jacob Oscarson',
    author_email='jacob@414soft.com',
    licence='Apache Software Licence 2.0',
    extras_require={'test': test_requires},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
