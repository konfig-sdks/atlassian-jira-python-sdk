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

from atlassian_jira_python_sdk.pydantic.dashboard import Dashboard

class PageOfDashboards(BaseModel):
    # List of dashboards.
    dashboards: typing.Optional[typing.List[Dashboard]] = Field(None, alias='dashboards')

    # The maximum number of results that could be on the page.
    max_results: typing.Optional[int] = Field(None, alias='maxResults')

    # The URL of the next page of results, if any.
    next: typing.Optional[str] = Field(None, alias='next')

    # The URL of the previous page of results, if any.
    prev: typing.Optional[str] = Field(None, alias='prev')

    # The index of the first item returned on the page.
    start_at: typing.Optional[int] = Field(None, alias='startAt')

    # The number of results on the page.
    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
