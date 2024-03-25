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

from atlassian_jira_python_sdk.type.project_id import ProjectId
from atlassian_jira_python_sdk.type.project_issue_types_issue_types import ProjectIssueTypesIssueTypes

class RequiredProjectIssueTypes(TypedDict):
    pass

class OptionalProjectIssueTypes(TypedDict, total=False):
    issueTypes: typing.Optional[ProjectIssueTypesIssueTypes]

    project: typing.Optional[ProjectId]

class ProjectIssueTypes(RequiredProjectIssueTypes, OptionalProjectIssueTypes):
    pass
