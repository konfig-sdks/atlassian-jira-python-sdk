# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_version.post import CreateProjectVersion
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_relatedwork.post import CreateRelatedWork
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_remove_and_swap.post import DeleteAndReplaceVersion
from atlassian_jira_python_sdk.paths.rest_api_3_version_id.delete import DeleteProjectVersion
from atlassian_jira_python_sdk.paths.rest_api_3_version_version_id_relatedwork_related_work_id.delete import DeleteRelatedWork
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_versions.get import GetAllProjectVersions
from atlassian_jira_python_sdk.paths.rest_api_3_version_id.get import GetProjectVersion
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_related_issue_counts.get import GetRelatedIssueCounts
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_relatedwork.get import GetRelatedWorkItems
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_unresolved_issue_count.get import GetUnresolvedIssueCount
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_version.get import ListPaginated
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_mergeto_move_issues_to.put import MergeVersions
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_relatedwork.put import UpdateRelatedWork
from atlassian_jira_python_sdk.paths.rest_api_3_version_id_move.post import UpdateSequenceWithinProject
from atlassian_jira_python_sdk.paths.rest_api_3_version_id.put import UpdateVersion
from atlassian_jira_python_sdk.apis.tags.project_versions_api_raw import ProjectVersionsApiRaw


class ProjectVersionsApi(
    CreateProjectVersion,
    CreateRelatedWork,
    DeleteAndReplaceVersion,
    DeleteProjectVersion,
    DeleteRelatedWork,
    GetAllProjectVersions,
    GetProjectVersion,
    GetRelatedIssueCounts,
    GetRelatedWorkItems,
    GetUnresolvedIssueCount,
    ListPaginated,
    MergeVersions,
    UpdateRelatedWork,
    UpdateSequenceWithinProject,
    UpdateVersion,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectVersionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectVersionsApiRaw(api_client)
