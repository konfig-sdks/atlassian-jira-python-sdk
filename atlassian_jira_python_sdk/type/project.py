# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from atlassian_jira_python_sdk.type.avatar_urls_bean import AvatarUrlsBean
from atlassian_jira_python_sdk.type.hierarchy import Hierarchy
from atlassian_jira_python_sdk.type.issue_type_details import IssueTypeDetails
from atlassian_jira_python_sdk.type.project_category import ProjectCategory
from atlassian_jira_python_sdk.type.project_component import ProjectComponent
from atlassian_jira_python_sdk.type.project_insight import ProjectInsight
from atlassian_jira_python_sdk.type.project_landing_page_info import ProjectLandingPageInfo
from atlassian_jira_python_sdk.type.project_permissions import ProjectPermissions
from atlassian_jira_python_sdk.type.project_properties import ProjectProperties
from atlassian_jira_python_sdk.type.project_roles import ProjectRoles
from atlassian_jira_python_sdk.type.user import User
from atlassian_jira_python_sdk.type.version import Version

RequiredProject = TypedDict("RequiredProject", {
    })

OptionalProject = TypedDict("OptionalProject", {
    # List of the components contained in the project.
    "components": typing.List[ProjectComponent],

    # A brief description of the project.
    "description": str,

    # Whether the project is archived.
    "archived": bool,

    # The user who archived the project.
    "archivedBy": User,

    # The date when the project was archived.
    "archivedDate": datetime,

    # The default assignee when creating issues for this project.
    "assigneeType": str,

    # The URLs of the project's avatars.
    "avatarUrls": AvatarUrlsBean,

    # Whether the project is marked as deleted.
    "deleted": bool,

    # The user who marked the project as deleted.
    "deletedBy": User,

    # The date when the project was marked as deleted.
    "deletedDate": datetime,

    # An email address associated with the project.
    "email": str,

    # Expand options that include additional project details in the response.
    "expand": str,

    # Whether the project is selected as a favorite.
    "favourite": bool,

    # The ID of the project.
    "id": str,

    # Insights about the project.
    "insight": ProjectInsight,

    # Whether the project is private from the user's perspective. This means the user can't see the project or any associated issues.
    "isPrivate": bool,

    # The issue type hierarchy for the project.
    "issueTypeHierarchy": Hierarchy,

    # List of the issue types available in the project.
    "issueTypes": typing.List[IssueTypeDetails],

    # The key of the project.
    "key": str,

    # The project landing page info.
    "landingPageInfo": ProjectLandingPageInfo,

    # The username of the project lead.
    "lead": User,

    # The name of the project.
    "name": str,

    # User permissions on the project
    "permissions": ProjectPermissions,

    # The category the project belongs to.
    "projectCategory": ProjectCategory,

    # The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project.
    "projectTypeKey": str,

    "properties": ProjectProperties,

    # The date when the project is deleted permanently.
    "retentionTillDate": datetime,

    "roles": ProjectRoles,

    # The URL of the project details.
    "self": str,

    # Whether the project is simplified.
    "simplified": bool,

    # The type of the project.
    "style": str,

    # A link to information about this project, such as project documentation.
    "url": str,

    # Unique ID for next-gen projects.
    "uuid": str,

    # The versions defined in the project. For more information, see [Create version](https://dac-static.atlassian.com).
    "versions": typing.List[Version],
    }, total=False)

class Project(RequiredProject, OptionalProject):
    pass
