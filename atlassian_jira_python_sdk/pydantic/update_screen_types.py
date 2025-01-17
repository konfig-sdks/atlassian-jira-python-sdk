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


class UpdateScreenTypes(BaseModel):
    # The ID of the create screen. To remove the screen association, pass a null.
    create: typing.Optional[str] = Field(None, alias='create')

    # The ID of the default screen. When specified, must include a screen ID as a default screen is required.
    default: typing.Optional[str] = Field(None, alias='default')

    # The ID of the edit screen. To remove the screen association, pass a null.
    edit: typing.Optional[str] = Field(None, alias='edit')

    # The ID of the view screen. To remove the screen association, pass a null.
    view: typing.Optional[str] = Field(None, alias='view')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
