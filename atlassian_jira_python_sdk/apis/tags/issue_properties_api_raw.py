# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issue_properties_property_key.delete import BulkDeleteIssuePropertyByFilterRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_properties_property_key.put import BulkSetIssuePropertyByListRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_properties_multi.post import BulkSetPropertiesByIssueRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_properties.post import BulkSetPropertiesByListRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_properties_property_key.delete import DeletePropertyRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_properties_property_key.get import GetByKeyAndValueRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_properties.get import GetKeysRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key_properties_property_key.put import SetIssuePropertyRaw


class IssuePropertiesApiRaw(
    BulkDeleteIssuePropertyByFilterRaw,
    BulkSetIssuePropertyByListRaw,
    BulkSetPropertiesByIssueRaw,
    BulkSetPropertiesByListRaw,
    DeletePropertyRaw,
    GetByKeyAndValueRaw,
    GetKeysRaw,
    SetIssuePropertyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass