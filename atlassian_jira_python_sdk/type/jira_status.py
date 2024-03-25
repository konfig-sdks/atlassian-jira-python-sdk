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

from atlassian_jira_python_sdk.type.project_issue_types import ProjectIssueTypes
from atlassian_jira_python_sdk.type.status_scope import StatusScope
from atlassian_jira_python_sdk.type.workflow_usages import WorkflowUsages

class RequiredJiraStatus(TypedDict):
    pass

class OptionalJiraStatus(TypedDict, total=False):
    # The description of the status.
    description: str

    # The ID of the status.
    id: str

    # The name of the status.
    name: str

    scope: StatusScope

    # The category of the status.
    statusCategory: str

    # Projects and issue types where the status is used. Only available if the `usages` expand is requested.
    usages: typing.List[ProjectIssueTypes]

    # The workflows that use this status. Only available if the `workflowUsages` expand is requested.
    workflowUsages: typing.List[WorkflowUsages]

class JiraStatus(RequiredJiraStatus, OptionalJiraStatus):
    pass
