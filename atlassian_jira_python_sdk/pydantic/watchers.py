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

class Watchers(BaseModel):
    # Whether the calling user is watching this issue.
    is_watching: typing.Optional[bool] = Field(None, alias='isWatching')

    # The URL of these issue watcher details.
    self_: typing.Optional[str] = Field(None, alias='self')

    # The number of users watching this issue.
    watch_count: typing.Optional[int] = Field(None, alias='watchCount')

    # Details of the users watching this issue.
    watchers: typing.Optional[typing.List[UserDetails]] = Field(None, alias='watchers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )