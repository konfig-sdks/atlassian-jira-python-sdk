# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_archive.post import ArchiveProject
from atlassian_jira_python_sdk.paths.rest_api_3_project.post import CreateProjectBasedOnTemplate
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_delete.post import DeleteProjectAsync
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key.delete import DeleteProjectByIdOrKey
from atlassian_jira_python_sdk.paths.rest_api_3_project.get import GetAll
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_hierarchy.get import GetIssueTypeHierarchy
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_key_or_id_notificationscheme.get import GetNotificationScheme
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key.get import GetProjectDetailsByIdOrKey
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_statuses.get import GetStatusesForProject
from atlassian_jira_python_sdk.paths.rest_api_3_project_recent.get import ListRecentProjects
from atlassian_jira_python_sdk.paths.rest_api_3_project_search.get import ListVisibleProjects
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key_restore.post import RestoreProject
from atlassian_jira_python_sdk.paths.rest_api_3_project_project_id_or_key.put import UpdateProjectDetails
from atlassian_jira_python_sdk.apis.tags.projects_api_raw import ProjectsApiRaw


class ProjectsApi(
    ArchiveProject,
    CreateProjectBasedOnTemplate,
    DeleteProjectAsync,
    DeleteProjectByIdOrKey,
    GetAll,
    GetIssueTypeHierarchy,
    GetNotificationScheme,
    GetProjectDetailsByIdOrKey,
    GetStatusesForProject,
    ListRecentProjects,
    ListVisibleProjects,
    RestoreProject,
    UpdateProjectDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectsApiRaw(api_client)
