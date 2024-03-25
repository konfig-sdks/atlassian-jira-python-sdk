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


class RequiredIssueTypeWorkflowMapping(TypedDict):
    pass

class OptionalIssueTypeWorkflowMapping(TypedDict, total=False):
    # The ID of the issue type. Not required if updating the issue type-workflow mapping.
    issueType: str

    # Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`. Only applicable when updating the workflow-issue types mapping.
    updateDraftIfNeeded: bool

    # The name of the workflow.
    workflow: str

class IssueTypeWorkflowMapping(RequiredIssueTypeWorkflowMapping, OptionalIssueTypeWorkflowMapping):
    pass