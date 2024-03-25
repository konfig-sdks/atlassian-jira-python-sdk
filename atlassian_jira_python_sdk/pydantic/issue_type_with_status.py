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

from atlassian_jira_python_sdk.pydantic.status_details import StatusDetails

class IssueTypeWithStatus(BaseModel):
    # The ID of the issue type.
    id: str = Field(alias='id')

    # The name of the issue type.
    name: str = Field(alias='name')

    # The URL of the issue type's status details.
    self_: str = Field(alias='self')

    # List of status details for the issue type.
    statuses: typing.List[StatusDetails] = Field(alias='statuses')

    # Whether this issue type represents subtasks.
    subtask: bool = Field(alias='subtask')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )