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

from atlassian_jira_python_sdk.type.app_workflow_transition_rule import AppWorkflowTransitionRule
from atlassian_jira_python_sdk.type.workflow_id import WorkflowId

class RequiredWorkflowTransitionRules(TypedDict):
    workflowId: WorkflowId

class OptionalWorkflowTransitionRules(TypedDict, total=False):
    # The list of conditions within the workflow.
    conditions: typing.List[AppWorkflowTransitionRule]

    # The list of post functions within the workflow.
    postFunctions: typing.List[AppWorkflowTransitionRule]

    # The list of validators within the workflow.
    validators: typing.List[AppWorkflowTransitionRule]

class WorkflowTransitionRules(RequiredWorkflowTransitionRules, OptionalWorkflowTransitionRules):
    pass
