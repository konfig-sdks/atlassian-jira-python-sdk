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


class ProjectType(BaseModel):
    # The color of the project type.
    color: typing.Optional[str] = Field(None, alias='color')

    # The key of the project type's description.
    description_i18n_key: typing.Optional[str] = Field(None, alias='descriptionI18nKey')

    # The formatted key of the project type.
    formatted_key: typing.Optional[str] = Field(None, alias='formattedKey')

    # The icon of the project type.
    icon: typing.Optional[str] = Field(None, alias='icon')

    # The key of the project type.
    key: typing.Optional[str] = Field(None, alias='key')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
