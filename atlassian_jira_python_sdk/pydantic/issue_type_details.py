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

from atlassian_jira_python_sdk.pydantic.scope import Scope

class IssueTypeDetails(BaseModel):
    # The description of the issue type.
    description: typing.Optional[str] = Field(None, alias='description')

    # The ID of the issue type's avatar.
    avatar_id: typing.Optional[int] = Field(None, alias='avatarId')

    # Unique ID for next-gen projects.
    entity_id: typing.Optional[str] = Field(None, alias='entityId')

    # Hierarchy level of the issue type.
    hierarchy_level: typing.Optional[int] = Field(None, alias='hierarchyLevel')

    # The URL of the issue type's avatar.
    icon_url: typing.Optional[str] = Field(None, alias='iconUrl')

    # The ID of the issue type.
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of the issue type.
    name: typing.Optional[str] = Field(None, alias='name')

    # Details of the next-gen projects the issue type is available in.
    scope: typing.Optional[Scope] = Field(None, alias='scope')

    # The URL of these issue type details.
    self_: typing.Optional[str] = Field(None, alias='self')

    # Whether this issue type is used to create subtasks.
    subtask: typing.Optional[bool] = Field(None, alias='subtask')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
