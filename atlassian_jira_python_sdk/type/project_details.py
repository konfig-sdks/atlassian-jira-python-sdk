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
from atlassian_jira_python_sdk.type.updated_project_category import UpdatedProjectCategory

RequiredProjectDetails = TypedDict("RequiredProjectDetails", {
    })

OptionalProjectDetails = TypedDict("OptionalProjectDetails", {
    # The URLs of the project's avatars.
    "avatarUrls": AvatarUrlsBean,

    # The ID of the project.
    "id": str,

    # The key of the project.
    "key": str,

    # The name of the project.
    "name": str,

    # The category the project belongs to.
    "projectCategory": UpdatedProjectCategory,

    # The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project.
    "projectTypeKey": str,

    # The URL of the project details.
    "self": str,

    # Whether or not the project is simplified.
    "simplified": bool,
    }, total=False)

class ProjectDetails(RequiredProjectDetails, OptionalProjectDetails):
    pass
