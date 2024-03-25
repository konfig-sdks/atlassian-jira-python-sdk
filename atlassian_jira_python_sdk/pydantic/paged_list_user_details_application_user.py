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

from atlassian_jira_python_sdk.pydantic.user_details import UserDetails

class PagedListUserDetailsApplicationUser(BaseModel):
    # The index of the last item returned on the page.
    end-index_: typing.Optional[int] = Field(None, alias='end-index')

    # The list of items.
    items: typing.Optional[typing.List[UserDetails]] = Field(None, alias='items')

    # The maximum number of results that could be on the page.
    max-results_: typing.Optional[int] = Field(None, alias='max-results')

    # The number of items on the page.
    size: typing.Optional[int] = Field(None, alias='size')

    # The index of the first item returned on the page.
    start-index_: typing.Optional[int] = Field(None, alias='start-index')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )