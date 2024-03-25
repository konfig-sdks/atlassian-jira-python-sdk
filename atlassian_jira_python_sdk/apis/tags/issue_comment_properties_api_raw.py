# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_comment_comment_id_properties_property_key.delete import DeleteCommentPropertyRaw
from atlassian_jira_python_sdk.paths.rest_api_3_comment_comment_id_properties.get import GetKeysRaw
from atlassian_jira_python_sdk.paths.rest_api_3_comment_comment_id_properties_property_key.get import GetPropertyValueRaw
from atlassian_jira_python_sdk.paths.rest_api_3_comment_comment_id_properties_property_key.put import SetPropertyValueRaw


class IssueCommentPropertiesApiRaw(
    DeleteCommentPropertyRaw,
    GetKeysRaw,
    GetPropertyValueRaw,
    SetPropertyValueRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
