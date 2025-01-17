# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_field.post import CreateCustomField
from atlassian_jira_python_sdk.paths.rest_api_3_field_id.delete import DeleteCustomField
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_contexts.get import GetContextsForField
from atlassian_jira_python_sdk.paths.rest_api_3_field_search.get import GetFieldsPaginated
from atlassian_jira_python_sdk.paths.rest_api_3_field.get import GetSystemAndCustomFields
from atlassian_jira_python_sdk.paths.rest_api_3_field_search_trashed.get import ListFieldsInTrashPaginated
from atlassian_jira_python_sdk.paths.rest_api_3_field_id_trash.post import MoveCustomFieldToTrash
from atlassian_jira_python_sdk.paths.rest_api_3_field_id_restore.post import RestoreCustomFieldFromTrash
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id.put import UpdateCustomField
from atlassian_jira_python_sdk.apis.tags.issue_fields_api_raw import IssueFieldsApiRaw


class IssueFieldsApi(
    CreateCustomField,
    DeleteCustomField,
    GetContextsForField,
    GetFieldsPaginated,
    GetSystemAndCustomFields,
    ListFieldsInTrashPaginated,
    MoveCustomFieldToTrash,
    RestoreCustomFieldFromTrash,
    UpdateCustomField,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueFieldsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueFieldsApiRaw(api_client)
