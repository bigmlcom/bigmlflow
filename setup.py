#!/usr/bin/env python
#
# Copyright 2022 BigML, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import re

from setuptools import setup

# Get the path to this project
project_path = os.path.dirname(__file__)

# Read the version from bigml.__version__ without importing the package
version_py_path = os.path.join(project_path, "bigmlflow", "version.py")
version = re.search('__version__ = "([^"]+)"', open(version_py_path).read()).group(1)

# Concatenate files into the long description
file_contents = []
for file_name in ("README.md", "HISTORY.md"):
    path = os.path.join(os.path.dirname(__file__), file_name)
    file_contents.append(open(path).read())
long_description = "\n\n".join(file_contents)


setup(
    name="bigmlflow",
    description="An open source library to add BigML models to the MLFlow API",
    long_description_content_type="text/markdown",
    long_description=long_description,
    version=version,
    author="The BigML Team",
    author_email="bigml@bigml.com",
    url="https://bigml.com/",
    download_url="https://github.com/bigmlcom/bigmlflow",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    python_requires=">=3.7",
    install_requires=["requests>=2.28.0", "mlflow>=2.0.1", "bigml"],
    extras_require={"test": ["pytest"]},
    packages=["bigmlflow"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="tests",
)
