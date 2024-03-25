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

from atlassian_jira_python_sdk.type.issue_context_variable import IssueContextVariable
from atlassian_jira_python_sdk.type.json_context_variable import JsonContextVariable
from atlassian_jira_python_sdk.type.user_context_variable import UserContextVariable

class RequiredCustomContextVariable(TypedDict):
    # Type of custom context variable.
    type: str

class OptionalCustomContextVariable(TypedDict, total=False):
    pass

class CustomContextVariable(RequiredCustomContextVariable, OptionalCustomContextVariable):
    pass
CustomContextVariable = typing.Union[UserContextVariable,IssueContextVariable,JsonContextVariable]
