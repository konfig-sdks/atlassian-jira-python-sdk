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

from atlassian_jira_python_sdk.pydantic.field_last_used import FieldLastUsed
from atlassian_jira_python_sdk.pydantic.json_type_bean import JsonTypeBean

class Field(BaseModel):
    # The ID of the field.
    id: str = Field(alias='id')

    # The name of the field.
    name: str = Field(alias='name')

    schema: JsonTypeBean = Field(alias='schema')

    # The description of the field.
    description: typing.Optional[str] = Field(None, alias='description')

    # Number of contexts where the field is used.
    contexts_count: typing.Optional[int] = Field(None, alias='contextsCount')

    # Whether the field is locked.
    is_locked: typing.Optional[bool] = Field(None, alias='isLocked')

    # Whether the field is shown on screen or not.
    is_unscreenable: typing.Optional[bool] = Field(None, alias='isUnscreenable')

    # The key of the field.
    key: typing.Optional[str] = Field(None, alias='key')

    last_used: typing.Optional[FieldLastUsed] = Field(None, alias='lastUsed')

    # Number of projects where the field is used.
    projects_count: typing.Optional[int] = Field(None, alias='projectsCount')

    # Number of screens where the field is used.
    screens_count: typing.Optional[int] = Field(None, alias='screensCount')

    # The searcher key of the field. Returned for custom fields.
    searcher_key: typing.Optional[str] = Field(None, alias='searcherKey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
