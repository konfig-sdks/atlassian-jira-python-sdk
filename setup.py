# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "atlassian-jira-python-sdk"
VERSION = "1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "certifi >= 2023.7.22",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.18",
    "cryptography ~= 42.0.5",
    "frozendict ~= 2.3.4",
    "aiohttp ~= 3.9.2",
    "pydantic ~= 2.4.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="The Jira Cloud platform REST API",
    author="Konfig",
    author_email="ecosystem@atlassian.com",
    url="https://github.com/konfig-sdks/atlassian-jira-python-sdk/tree/main/python",
    keywords=["Konfig", "The Jira Cloud platform REST API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
