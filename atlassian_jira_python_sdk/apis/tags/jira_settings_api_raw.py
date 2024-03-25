# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_application_properties_advanced_settings.get import GetAdvancedSettingsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_application_properties.get import GetApplicationPropertyRaw
from atlassian_jira_python_sdk.paths.rest_api_3_configuration.get import GetGlobalSettingsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_application_properties_id.put import SetApplicationPropertyRaw


class JiraSettingsApiRaw(
    GetAdvancedSettingsRaw,
    GetApplicationPropertyRaw,
    GetGlobalSettingsRaw,
    SetApplicationPropertyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
