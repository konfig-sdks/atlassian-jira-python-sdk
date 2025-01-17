# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_issuetype.put import AddIssueTypesToContext
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_project.put import AssignContextsToProjects
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context.post import CreateCustomFieldContext
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id.delete import DeleteCustomFieldContext
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_mapping.post import GetCustomFieldContextsForProjectsAndIssueTypes
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_default_value.get import GetDefaultValues
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_issuetypemapping.get import GetIssueTypeMappingsForContexts
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_projectmapping.get import GetProjectContextMapping
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context.get import ListCustomFieldContexts
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_project_remove.post import RemoveCustomFieldContextFromProjects
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id_issuetype_remove.post import RemoveIssueTypesFromContext
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_default_value.put import SetDefaultValues
from atlassian_jira_python_sdk.paths.rest_api_3_field_field_id_context_context_id.put import UpdateCustomFieldContext
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_contexts_api_raw import IssueCustomFieldContextsApiRaw


class IssueCustomFieldContextsApi(
    AddIssueTypesToContext,
    AssignContextsToProjects,
    CreateCustomFieldContext,
    DeleteCustomFieldContext,
    GetCustomFieldContextsForProjectsAndIssueTypes,
    GetDefaultValues,
    GetIssueTypeMappingsForContexts,
    GetProjectContextMapping,
    ListCustomFieldContexts,
    RemoveCustomFieldContextFromProjects,
    RemoveIssueTypesFromContext,
    SetDefaultValues,
    UpdateCustomFieldContext,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueCustomFieldContextsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueCustomFieldContextsApiRaw(api_client)
