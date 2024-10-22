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
from atlassian_jira_python_sdk.type.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata

RequiredProjectIssueCreateMetadata = TypedDict("RequiredProjectIssueCreateMetadata", {
    })

OptionalProjectIssueCreateMetadata = TypedDict("OptionalProjectIssueCreateMetadata", {
    # List of the project's avatars, returning the avatar size and associated URL.
    "avatarUrls": AvatarUrlsBean,

    # Expand options that include additional project issue create metadata details in the response.
    "expand": str,

    # The ID of the project.
    "id": str,

    # List of the issue types supported by the project.
    "issuetypes": typing.List[IssueTypeIssueCreateMetadata],

    # The key of the project.
    "key": str,

    # The name of the project.
    "name": str,

    # The URL of the project.
    "self": str,
    }, total=False)

class ProjectIssueCreateMetadata(RequiredProjectIssueCreateMetadata, OptionalProjectIssueCreateMetadata):
    pass
