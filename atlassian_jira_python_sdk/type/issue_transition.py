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

from atlassian_jira_python_sdk.type.issue_transition_fields import IssueTransitionFields
from atlassian_jira_python_sdk.type.status_details import StatusDetails

class RequiredIssueTransition(TypedDict):
    pass

class OptionalIssueTransition(TypedDict, total=False):
    # Expand options that include additional transition details in the response.
    expand: str

    fields: IssueTransitionFields

    # Whether there is a screen associated with the issue transition.
    hasScreen: bool

    # The ID of the issue transition. Required when specifying a transition to undertake.
    id: str

    # Whether the transition is available to be performed.
    isAvailable: bool

    # Whether the issue has to meet criteria before the issue transition is applied.
    isConditional: bool

    # Whether the issue transition is global, that is, the transition is applied to issues regardless of their status.
    isGlobal: bool

    # Whether this is the initial issue transition for the workflow.
    isInitial: bool

    looped: bool

    # The name of the issue transition.
    name: str

    to: StatusDetails

class IssueTransition(RequiredIssueTransition, OptionalIssueTransition):
    pass