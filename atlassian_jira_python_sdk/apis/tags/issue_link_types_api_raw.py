# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type.post import CreateLinkTypeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.delete import DeleteTypeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type.get import GetAllRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.get import GetLinkTypeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.put import UpdateTypeRaw


class IssueLinkTypesApiRaw(
    CreateLinkTypeRaw,
    DeleteTypeRaw,
    GetAllRaw,
    GetLinkTypeRaw,
    UpdateTypeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
