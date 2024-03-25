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
from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs_tab_id_fields_id import delete
from atlassian_jira_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRestApi3ScreensScreenIdTabsTabIdFieldsId(ApiTestMixin, unittest.TestCase):
    """
    RestApi3ScreensScreenIdTabsTabIdFieldsId unit test stubs
        Remove screen tab field
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
