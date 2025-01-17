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

from atlassian_jira_python_sdk.pydantic.issue_picker_suggestions_issue_type import IssuePickerSuggestionsIssueType

class IssuePickerSuggestions(BaseModel):
    # A list of issues for an issue type suggested for use in auto-completion.
    sections: typing.Optional[typing.List[IssuePickerSuggestionsIssueType]] = Field(None, alias='sections')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
