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

from atlassian_jira_python_sdk.type.status_layout_update import StatusLayoutUpdate
from atlassian_jira_python_sdk.type.transition_update_dto import TransitionUpdateDTO
from atlassian_jira_python_sdk.type.workflow_layout import WorkflowLayout

class RequiredWorkflowCreate(TypedDict):
    # The name of the workflow to create.
    name: str

    # The statuses associated with this workflow.
    statuses: typing.List[StatusLayoutUpdate]

    # The transitions of this workflow.
    transitions: typing.List[TransitionUpdateDTO]

class OptionalWorkflowCreate(TypedDict, total=False):
    # The description of the workflow to create.
    description: str

    startPointLayout: typing.Optional[WorkflowLayout]

class WorkflowCreate(RequiredWorkflowCreate, OptionalWorkflowCreate):
    pass