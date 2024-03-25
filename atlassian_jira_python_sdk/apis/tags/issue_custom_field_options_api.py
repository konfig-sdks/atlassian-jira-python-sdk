# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.post import CreateCustomFieldOption
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_option_id.delete import DeleteCustomFieldOption
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.get import GetContextOptions
from atlassian_jira_python_sdk.paths.rest_api_3_custom_field_option_id.get import GetOptionById
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_move.put import ReorderCustomFieldOptions
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_option_id_issue.delete import ReplaceOptions
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.put import UpdateContextOption
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_options_api_raw import IssueCustomFieldOptionsApiRaw


class IssueCustomFieldOptionsApi(
    CreateCustomFieldOption,
    DeleteCustomFieldOption,
    GetContextOptions,
    GetOptionById,
    ReorderCustomFieldOptions,
    ReplaceOptions,
    UpdateContextOption,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueCustomFieldOptionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueCustomFieldOptionsApiRaw(api_client)