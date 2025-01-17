# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_statuses.post import BulkCreateStatusesRaw
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.delete import BulkDeleteByIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.get import BulkGetStatusesRaw
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.put import BulkUpdateStatusesByIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_statuses_search.get import SearchPaginatedRaw


class StatusApiRaw(
    BulkCreateStatusesRaw,
    BulkDeleteByIdRaw,
    BulkGetStatusesRaw,
    BulkUpdateStatusesByIdRaw,
    SearchPaginatedRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
