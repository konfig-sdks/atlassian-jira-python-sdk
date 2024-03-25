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

from atlassian_jira_python_sdk.type.workflow_create import WorkflowCreate
from atlassian_jira_python_sdk.type.workflow_scope import WorkflowScope
from atlassian_jira_python_sdk.type.workflow_status_update import WorkflowStatusUpdate

class RequiredWorkflowCreateRequest(TypedDict):
    scope: WorkflowScope

    # The statuses to associate with the workflows.
    statuses: typing.List[WorkflowStatusUpdate]

    # The details of the workflows to create.
    workflows: typing.List[WorkflowCreate]

class OptionalWorkflowCreateRequest(TypedDict, total=False):
    pass

class WorkflowCreateRequest(RequiredWorkflowCreateRequest, OptionalWorkflowCreateRequest):
    pass