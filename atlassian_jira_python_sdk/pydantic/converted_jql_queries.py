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

from atlassian_jira_python_sdk.pydantic.converted_jql_queries_query_strings import ConvertedJQLQueriesQueryStrings
from atlassian_jira_python_sdk.pydantic.jql_query_with_unknown_users import JQLQueryWithUnknownUsers

class ConvertedJQLQueries(BaseModel):
    # List of queries containing user information that could not be mapped to an existing user
    queries_with_unknown_users: typing.Optional[typing.List[JQLQueryWithUnknownUsers]] = Field(None, alias='queriesWithUnknownUsers')

    query_strings: typing.Optional[ConvertedJQLQueriesQueryStrings] = Field(None, alias='queryStrings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
