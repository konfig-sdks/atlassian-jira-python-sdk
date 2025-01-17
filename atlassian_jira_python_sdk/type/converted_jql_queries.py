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

from atlassian_jira_python_sdk.type.converted_jql_queries_query_strings import ConvertedJQLQueriesQueryStrings
from atlassian_jira_python_sdk.type.jql_query_with_unknown_users import JQLQueryWithUnknownUsers

class RequiredConvertedJQLQueries(TypedDict):
    pass

class OptionalConvertedJQLQueries(TypedDict, total=False):
    # List of queries containing user information that could not be mapped to an existing user
    queriesWithUnknownUsers: typing.List[JQLQueryWithUnknownUsers]

    queryStrings: ConvertedJQLQueriesQueryStrings

class ConvertedJQLQueries(RequiredConvertedJQLQueries, OptionalConvertedJQLQueries):
    pass
