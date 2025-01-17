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

from atlassian_jira_python_sdk.type.issue_type_issue_create_metadata_fields import IssueTypeIssueCreateMetadataFields
from atlassian_jira_python_sdk.type.scope import Scope

RequiredIssueTypeIssueCreateMetadata = TypedDict("RequiredIssueTypeIssueCreateMetadata", {
    })

OptionalIssueTypeIssueCreateMetadata = TypedDict("OptionalIssueTypeIssueCreateMetadata", {
    # The description of the issue type.
    "description": str,

    # The ID of the issue type's avatar.
    "avatarId": int,

    # Unique ID for next-gen projects.
    "entityId": str,

    # Expand options that include additional issue type metadata details in the response.
    "expand": str,

    "fields": IssueTypeIssueCreateMetadataFields,

    # Hierarchy level of the issue type.
    "hierarchyLevel": int,

    # The URL of the issue type's avatar.
    "iconUrl": str,

    # The ID of the issue type.
    "id": str,

    # The name of the issue type.
    "name": str,

    # Details of the next-gen projects the issue type is available in.
    "scope": Scope,

    # The URL of these issue type details.
    "self": str,

    # Whether this issue type is used to create subtasks.
    "subtask": bool,
    }, total=False)

class IssueTypeIssueCreateMetadata(RequiredIssueTypeIssueCreateMetadata, OptionalIssueTypeIssueCreateMetadata):
    pass
