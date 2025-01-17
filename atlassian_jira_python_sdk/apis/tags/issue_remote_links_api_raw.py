# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink.post import CreateOrUpdateRemoteIssueLinkRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink.delete import DeleteByGlobalIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink_link_id.delete import DeleteByIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink.get import GetAllRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink_link_id.get import GetByLinkIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_remotelink_link_id.put import UpdateByIdRaw


class IssueRemoteLinksApiRaw(
    CreateOrUpdateRemoteIssueLinkRaw,
    DeleteByGlobalIdRaw,
    DeleteByIdRaw,
    GetAllRaw,
    GetByLinkIdRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
