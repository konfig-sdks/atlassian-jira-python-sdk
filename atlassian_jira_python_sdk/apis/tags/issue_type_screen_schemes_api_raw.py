# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id_mapping.put import AppendMappingsToSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_project.put import AssignSchemeToProjectRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme.post import CreateSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id.delete import DeleteSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id_project.get import GetScreenSchemeProjectsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_project.get import GetScreenSchemesForProjectRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_mapping.get import ListSchemeMappingsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme.get import ListScreenSchemesRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id_mapping_remove.post import RemoveMappingsRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id_mapping_default.put import UpdateDefaultScreenSchemeRaw
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescreenscheme_issue_type_screen_scheme_id.put import UpdateScreenSchemeRaw


class IssueTypeScreenSchemesApiRaw(
    AppendMappingsToSchemeRaw,
    AssignSchemeToProjectRaw,
    CreateSchemeRaw,
    DeleteSchemeRaw,
    GetScreenSchemeProjectsRaw,
    GetScreenSchemesForProjectRaw,
    ListSchemeMappingsRaw,
    ListScreenSchemesRaw,
    RemoveMappingsRaw,
    UpdateDefaultScreenSchemeRaw,
    UpdateScreenSchemeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
