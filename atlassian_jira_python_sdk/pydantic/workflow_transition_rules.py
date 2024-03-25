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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from atlassian_jira_python_sdk.pydantic.app_workflow_transition_rule import AppWorkflowTransitionRule
from atlassian_jira_python_sdk.pydantic.workflow_id import WorkflowId

class WorkflowTransitionRules(BaseModel):
    workflow_id: WorkflowId = Field(alias='workflowId')

    # The list of conditions within the workflow.
    conditions: typing.Optional[typing.List[AppWorkflowTransitionRule]] = Field(None, alias='conditions')

    # The list of post functions within the workflow.
    post_functions: typing.Optional[typing.List[AppWorkflowTransitionRule]] = Field(None, alias='postFunctions')

    # The list of validators within the workflow.
    validators: typing.Optional[typing.List[AppWorkflowTransitionRule]] = Field(None, alias='validators')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )