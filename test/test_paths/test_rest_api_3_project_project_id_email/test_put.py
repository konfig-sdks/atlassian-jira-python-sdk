# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import atlassian_jira_python_sdk
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_email import put
from atlassian_jira_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRestApi3ProjectProjectIdEmail(ApiTestMixin, unittest.TestCase):
    """
    RestApi3ProjectProjectIdEmail unit test stubs
        Set project's sender email
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204






if __name__ == '__main__':
    unittest.main()
