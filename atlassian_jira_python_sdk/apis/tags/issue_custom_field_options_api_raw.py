# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.post import CreateCustomFieldOptionRaw
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_option_id.delete import DeleteCustomFieldOptionRaw
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.get import GetContextOptionsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_custom_field_option_id.get import GetOptionByIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_move.put import ReorderCustomFieldOptionsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option_option_id_issue.delete import ReplaceOptionsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_option.put import UpdateContextOptionRaw


class IssueCustomFieldOptionsApiRaw(
    CreateCustomFieldOptionRaw,
    DeleteCustomFieldOptionRaw,
    GetContextOptionsRaw,
    GetOptionByIdRaw,
    ReorderCustomFieldOptionsRaw,
    ReplaceOptionsRaw,
    UpdateContextOptionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass