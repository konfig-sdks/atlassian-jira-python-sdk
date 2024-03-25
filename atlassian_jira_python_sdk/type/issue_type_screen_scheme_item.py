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


class RequiredIssueTypeScreenSchemeItem(TypedDict):
    # The ID of the issue type or *default*. Only issue types used in classic projects are accepted. When creating an issue screen scheme, an entry for *default* must be provided and defines the mapping for all issue types without a screen scheme. Otherwise, a *default* entry can't be provided.
    issueTypeId: str

    # The ID of the issue type screen scheme.
    issueTypeScreenSchemeId: str

    # The ID of the screen scheme.
    screenSchemeId: str

class OptionalIssueTypeScreenSchemeItem(TypedDict, total=False):
    pass

class IssueTypeScreenSchemeItem(RequiredIssueTypeScreenSchemeItem, OptionalIssueTypeScreenSchemeItem):
    pass
