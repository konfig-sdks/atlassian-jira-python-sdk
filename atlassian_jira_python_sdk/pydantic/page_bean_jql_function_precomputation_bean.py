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

from atlassian_jira_python_sdk.pydantic.jql_function_precomputation_bean import JqlFunctionPrecomputationBean

class PageBeanJqlFunctionPrecomputationBean(BaseModel):
    # Whether this is the last page.
    is_last: typing.Optional[bool] = Field(None, alias='isLast')

    # The maximum number of items that could be returned.
    max_results: typing.Optional[int] = Field(None, alias='maxResults')

    # If there is another page of results, the URL of the next page.
    next_page: typing.Optional[str] = Field(None, alias='nextPage')

    # The URL of the page.
    self_: typing.Optional[str] = Field(None, alias='self')

    # The index of the first item returned.
    start_at: typing.Optional[int] = Field(None, alias='startAt')

    # The number of items returned.
    total: typing.Optional[int] = Field(None, alias='total')

    # The list of items.
    values: typing.Optional[typing.List[JqlFunctionPrecomputationBean]] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
