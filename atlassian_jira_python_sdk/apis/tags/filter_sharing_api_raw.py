# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_permission.post import AddSharePermissionRaw
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_permission_permission_id.delete import DeleteSharePermissionRaw
from atlassian_jira_python_sdk.paths.rest_api_3_filter_default_share_scope.get import GetDefaultShareScopeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_permission_permission_id.get import GetSharePermissionRaw
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_permission.get import GetSharePermissionsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_filter_default_share_scope.put import SetDefaultShareScopeRaw


class FilterSharingApiRaw(
    AddSharePermissionRaw,
    DeleteSharePermissionRaw,
    GetDefaultShareScopeRaw,
    GetSharePermissionRaw,
    GetSharePermissionsRaw,
    SetDefaultShareScopeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
