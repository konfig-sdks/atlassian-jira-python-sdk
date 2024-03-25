# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_issue_type_scheme_id_issuetype.put import AddIssueTypesToScheme
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_project.put import AssignSchemeToProject
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_issue_type_scheme_id_issuetype_move.put import ChangeOrderOfIssueTypes
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme.post import CreateScheme
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_issue_type_scheme_id.delete import DeleteSchemeById
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme.get import GetAllSchemes
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_project.get import GetIssueTypeSchemeForProjects
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_mapping.get import GetSchemeMapping
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_issue_type_scheme_id_issuetype_issue_type_id.delete import RemoveIssueTypeSchemeMapping
from atlassian_jira_python_sdk.paths.rest_api_3_issuetypescheme_issue_type_scheme_id.put import UpdateScheme
from atlassian_jira_python_sdk.apis.tags.issue_type_schemes_api_raw import IssueTypeSchemesApiRaw


class IssueTypeSchemesApi(
    AddIssueTypesToScheme,
    AssignSchemeToProject,
    ChangeOrderOfIssueTypes,
    CreateScheme,
    DeleteSchemeById,
    GetAllSchemes,
    GetIssueTypeSchemeForProjects,
    GetSchemeMapping,
    RemoveIssueTypeSchemeMapping,
    UpdateScheme,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IssueTypeSchemesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IssueTypeSchemesApiRaw(api_client)