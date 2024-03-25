# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_application_properties_advanced_settings.get import GetAdvancedSettings
from atlassian_jira_python_sdk.paths.rest_api_3_application_properties.get import GetApplicationProperty
from atlassian_jira_python_sdk.paths.rest_api_3_configuration.get import GetGlobalSettings
from atlassian_jira_python_sdk.paths.rest_api_3_application_properties_id.put import SetApplicationProperty
from atlassian_jira_python_sdk.apis.tags.jira_settings_api_raw import JiraSettingsApiRaw


class JiraSettingsApi(
    GetAdvancedSettings,
    GetApplicationProperty,
    GetGlobalSettings,
    SetApplicationProperty,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JiraSettingsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JiraSettingsApiRaw(api_client)