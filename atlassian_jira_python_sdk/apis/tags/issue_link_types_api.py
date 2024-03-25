# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type.post import CreateLinkType
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.delete import DeleteType
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type.get import GetAll
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.get import GetLinkType
from atlassian_jira_python_sdk.paths.rest_api_3_issue_link_type_issue_link_type_id.put import UpdateType
from atlassian_jira_python_sdk.apis.tags.issue_link_types_api_raw import IssueLinkTypesApiRaw


class IssueLinkTypesApi(
    CreateLinkType,
    DeleteType,
    GetAll,
    GetLinkType,
    UpdateType,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueLinkTypesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueLinkTypesApiRaw(api_client)
