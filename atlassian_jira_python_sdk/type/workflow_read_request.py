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

from atlassian_jira_python_sdk.type.project_and_issue_type_pair import ProjectAndIssueTypePair
from atlassian_jira_python_sdk.type.workflow_read_request_workflow_ids import WorkflowReadRequestWorkflowIds
from atlassian_jira_python_sdk.type.workflow_read_request_workflow_names import WorkflowReadRequestWorkflowNames

class RequiredWorkflowReadRequest(TypedDict):
    pass

class OptionalWorkflowReadRequest(TypedDict, total=False):
    # The list of projects and issue types to query.
    projectAndIssueTypes: typing.List[ProjectAndIssueTypePair]

    workflowIds: WorkflowReadRequestWorkflowIds

    workflowNames: WorkflowReadRequestWorkflowNames

class WorkflowReadRequest(RequiredWorkflowReadRequest, OptionalWorkflowReadRequest):
    pass