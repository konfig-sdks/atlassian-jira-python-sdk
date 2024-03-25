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

from atlassian_jira_python_sdk.type.context_for_project_and_issue_type import ContextForProjectAndIssueType

RequiredPageBeanContextForProjectAndIssueType = TypedDict("RequiredPageBeanContextForProjectAndIssueType", {
    })

OptionalPageBeanContextForProjectAndIssueType = TypedDict("OptionalPageBeanContextForProjectAndIssueType", {
    # Whether this is the last page.
    "isLast": bool,

    # The maximum number of items that could be returned.
    "maxResults": int,

    # If there is another page of results, the URL of the next page.
    "nextPage": str,

    # The URL of the page.
    "self": str,

    # The index of the first item returned.
    "startAt": int,

    # The number of items returned.
    "total": int,

    # The list of items.
    "values": typing.List[ContextForProjectAndIssueType],
    }, total=False)

class PageBeanContextForProjectAndIssueType(RequiredPageBeanContextForProjectAndIssueType, OptionalPageBeanContextForProjectAndIssueType):
    pass
