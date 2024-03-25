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


class VersionIssuesStatus(BaseModel):
    # Count of issues with status *done*.
    done: typing.Optional[int] = Field(None, alias='done')

    # Count of issues with status *in progress*.
    in_progress: typing.Optional[int] = Field(None, alias='inProgress')

    # Count of issues with status *to do*.
    to_do: typing.Optional[int] = Field(None, alias='toDo')

    # Count of issues with a status other than *to do*, *in progress*, and *done*.
    unmapped: typing.Optional[int] = Field(None, alias='unmapped')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )