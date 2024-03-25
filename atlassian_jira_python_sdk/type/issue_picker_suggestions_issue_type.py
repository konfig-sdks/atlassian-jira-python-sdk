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

from atlassian_jira_python_sdk.type.suggested_issue import SuggestedIssue

class RequiredIssuePickerSuggestionsIssueType(TypedDict):
    pass

class OptionalIssuePickerSuggestionsIssueType(TypedDict, total=False):
    # The ID of the type of issues suggested for use in auto-completion.
    id: str

    # A list of issues suggested for use in auto-completion.
    issues: typing.List[SuggestedIssue]

    # The label of the type of issues suggested for use in auto-completion.
    label: str

    # If no issue suggestions are found, returns a message indicating no suggestions were found,
    msg: str

    # If issue suggestions are found, returns a message indicating the number of issues suggestions found and returned.
    sub: str

class IssuePickerSuggestionsIssueType(RequiredIssuePickerSuggestionsIssueType, OptionalIssuePickerSuggestionsIssueType):
    pass