# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_project.put import AssignFieldConfigurationSchemeToProjectRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_id_mapping.put import AssignIssueTypesToFieldConfigurationSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration.post import CreateFieldConfigurationRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme.post import CreateFieldConfigurationSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration_id.delete import DeleteFieldConfigurationRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_id.delete import DeleteSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration.get import GetAllFieldConfigurationsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration_id_fields.get import GetConfigurationItemsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_mapping.get import GetConfigurationSchemeMappingRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_project.get import GetFieldConfigurationSchemesForProjectsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme.get import ListFieldConfigurationSchemesRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_id_mapping_delete.post import RemoveIssueTypesFromFieldConfigSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration_id_fields.put import UpdateFieldConfigItemsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfiguration_id.put import UpdateFieldConfigurationRaw
from atlassian_jira_python_sdk.paths.rest_api_3_fieldconfigurationscheme_id.put import UpdateSchemeRaw


class IssueFieldConfigurationsApiRaw(
    AssignFieldConfigurationSchemeToProjectRaw,
    AssignIssueTypesToFieldConfigurationSchemeRaw,
    CreateFieldConfigurationRaw,
    CreateFieldConfigurationSchemeRaw,
    DeleteFieldConfigurationRaw,
    DeleteSchemeRaw,
    GetAllFieldConfigurationsRaw,
    GetConfigurationItemsRaw,
    GetConfigurationSchemeMappingRaw,
    GetFieldConfigurationSchemesForProjectsRaw,
    ListFieldConfigurationSchemesRaw,
    RemoveIssueTypesFromFieldConfigSchemeRaw,
    UpdateFieldConfigItemsRaw,
    UpdateFieldConfigurationRaw,
    UpdateSchemeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
