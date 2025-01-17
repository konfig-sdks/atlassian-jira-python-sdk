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

from atlassian_jira_python_sdk.type.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata

class RequiredPageOfCreateMetaIssueTypes(TypedDict):
    pass

class OptionalPageOfCreateMetaIssueTypes(TypedDict, total=False):
    createMetaIssueType: typing.List[IssueTypeIssueCreateMetadata]

    # The list of CreateMetaIssueType.
    issueTypes: typing.List[IssueTypeIssueCreateMetadata]

    # The maximum number of items to return per page.
    maxResults: int

    # The index of the first item returned.
    startAt: int

    # The total number of items in all pages.
    total: int

class PageOfCreateMetaIssueTypes(RequiredPageOfCreateMetaIssueTypes, OptionalPageOfCreateMetaIssueTypes):
    pass
