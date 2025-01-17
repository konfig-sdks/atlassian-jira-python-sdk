# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences_locale.delete import DeleteUserLocaleRaw
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.delete import DeleteUserPreferenceRaw
from atlassian_jira_python_sdk.paths.rest_api_3_myself.get import GetCurrentUserDetailsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.get import GetPreferenceValueRaw
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences_locale.get import GetUserLocaleRaw
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences_locale.put import SetUserLocaleRaw
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.put import UpdatePreferenceValueRaw


class MyselfApiRaw(
    DeleteUserLocaleRaw,
    DeleteUserPreferenceRaw,
    GetCurrentUserDetailsRaw,
    GetPreferenceValueRaw,
    GetUserLocaleRaw,
    SetUserLocaleRaw,
    UpdatePreferenceValueRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
