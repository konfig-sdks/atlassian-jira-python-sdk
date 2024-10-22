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

from atlassian_jira_python_sdk.type.jql_query import JqlQuery
from atlassian_jira_python_sdk.type.parsed_jql_query_errors import ParsedJqlQueryErrors

class RequiredParsedJqlQuery(TypedDict):
    # The JQL query that was parsed and validated.
    query: str

class OptionalParsedJqlQuery(TypedDict, total=False):
    errors: ParsedJqlQueryErrors

    # The syntax tree of the query. Empty if the query was invalid.
    structure: JqlQuery

class ParsedJqlQuery(RequiredParsedJqlQuery, OptionalParsedJqlQuery):
    pass
