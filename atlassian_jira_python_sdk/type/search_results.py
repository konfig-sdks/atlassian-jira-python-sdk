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

from atlassian_jira_python_sdk.type.issue_bean import IssueBean
from atlassian_jira_python_sdk.type.search_results_names import SearchResultsNames
from atlassian_jira_python_sdk.type.search_results_schema import SearchResultsSchema
from atlassian_jira_python_sdk.type.search_results_warning_messages import SearchResultsWarningMessages

class RequiredSearchResults(TypedDict):
    pass

class OptionalSearchResults(TypedDict, total=False):
    # Expand options that include additional search result details in the response.
    expand: str

    # The list of issues found by the search.
    issues: typing.List[IssueBean]

    # The maximum number of results that could be on the page.
    maxResults: int

    names: SearchResultsNames

    schema: SearchResultsSchema

    # The index of the first item returned on the page.
    startAt: int

    # The number of results on the page.
    total: int

    warningMessages: SearchResultsWarningMessages

class SearchResults(RequiredSearchResults, OptionalSearchResults):
    pass
