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


class CustomFieldContextDefaultValueDate(BaseModel):
    type: str = Field(alias='type')

    # The default date in ISO format. Ignored if `useCurrent` is true.
    date: typing.Optional[str] = Field(None, alias='date')

    # Whether to use the current date.
    use_current: typing.Optional[bool] = Field(None, alias='useCurrent')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
