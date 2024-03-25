# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from atlassian_jira_python_sdk import AtlassianJira

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        atlassianjira = AtlassianJira(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD'
        )
        self.assertIsNotNone(atlassianjira)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()