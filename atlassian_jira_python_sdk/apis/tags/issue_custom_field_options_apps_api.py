# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option.post import CreateFieldOption
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_option_id.delete import DeleteOption
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_option_id_issue.delete import DeselectOptionFromIssues
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option.get import GetAllIssueFieldOptions
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_option_id.get import GetIssueFieldOption
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_suggestions_edit.get import GetSelectableIssueFieldOptions
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_suggestions_search.get import GetVisibleIssueFieldOptions
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_key_option_option_id.put import UpdateOptionById
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_options_apps_api_raw import IssueCustomFieldOptionsAppsApiRaw


class IssueCustomFieldOptionsAppsApi(
    CreateFieldOption,
    DeleteOption,
    DeselectOptionFromIssues,
    GetAllIssueFieldOptions,
    GetIssueFieldOption,
    GetSelectableIssueFieldOptions,
    GetVisibleIssueFieldOptions,
    UpdateOptionById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueCustomFieldOptionsAppsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueCustomFieldOptionsAppsApiRaw(api_client)
