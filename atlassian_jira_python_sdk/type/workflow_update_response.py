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

from atlassian_jira_python_sdk.type.jira_workflow import JiraWorkflow
from atlassian_jira_python_sdk.type.jira_workflow_status import JiraWorkflowStatus

class RequiredWorkflowUpdateResponse(TypedDict):
    pass

class OptionalWorkflowUpdateResponse(TypedDict, total=False):
    # List of updated statuses.
    statuses: typing.List[JiraWorkflowStatus]

    # If there is a [asynchronous task](https://dac-static.atlassian.com) operation, as a result of this update.
    taskId: typing.Optional[str]

    # List of updated workflows.
    workflows: typing.List[JiraWorkflow]

class WorkflowUpdateResponse(RequiredWorkflowUpdateResponse, OptionalWorkflowUpdateResponse):
    pass
