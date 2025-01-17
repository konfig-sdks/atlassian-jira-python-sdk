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

from atlassian_jira_python_sdk.type.issue_field_option_configuration import IssueFieldOptionConfiguration
from atlassian_jira_python_sdk.type.issue_field_option_properties import IssueFieldOptionProperties

class RequiredIssueFieldOption(TypedDict):
    # The unique identifier for the option. This is only unique within the select field's set of options.
    id: int

    # The option's name, which is displayed in Jira.
    value: str

class OptionalIssueFieldOption(TypedDict, total=False):
    config: IssueFieldOptionConfiguration

    properties: IssueFieldOptionProperties

class IssueFieldOption(RequiredIssueFieldOption, OptionalIssueFieldOption):
    pass
