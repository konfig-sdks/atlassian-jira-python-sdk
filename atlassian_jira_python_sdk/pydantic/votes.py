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

from atlassian_jira_python_sdk.pydantic.user import User

class Votes(BaseModel):
    # Whether the user making this request has voted on the issue.
    has_voted: typing.Optional[bool] = Field(None, alias='hasVoted')

    # The URL of these issue vote details.
    self_: typing.Optional[str] = Field(None, alias='self')

    # List of the users who have voted on this issue. An empty list is returned when the calling user doesn't have the *View voters and watchers* project permission.
    voters: typing.Optional[typing.List[User]] = Field(None, alias='voters')

    # The number of votes on the issue.
    votes: typing.Optional[int] = Field(None, alias='votes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
