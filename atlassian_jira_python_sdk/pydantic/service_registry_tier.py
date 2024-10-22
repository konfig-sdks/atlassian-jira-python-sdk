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


class ServiceRegistryTier(BaseModel):
    # tier description
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    # tier ID
    id: typing.Optional[str] = Field(None, alias='id')

    # tier level
    level: typing.Optional[int] = Field(None, alias='level')

    # tier name
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    # name key of the tier
    name_key: typing.Optional[str] = Field(None, alias='nameKey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
