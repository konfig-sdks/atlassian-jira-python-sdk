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


class RequiredWorkflowId(TypedDict):
    # Whether the workflow is in the draft state.
    draft: bool

    # The name of the workflow.
    name: str

class OptionalWorkflowId(TypedDict, total=False):
    pass

class WorkflowId(RequiredWorkflowId, OptionalWorkflowId):
    pass
