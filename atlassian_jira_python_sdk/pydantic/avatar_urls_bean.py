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


class AvatarUrlsBean(BaseModel):
    # The URL of the item's 16x16 pixel avatar.
    16x16_: typing.Optional[str] = Field(None, alias='16x16')

    # The URL of the item's 24x24 pixel avatar.
    24x24_: typing.Optional[str] = Field(None, alias='24x24')

    # The URL of the item's 32x32 pixel avatar.
    32x32_: typing.Optional[str] = Field(None, alias='32x32')

    # The URL of the item's 48x48 pixel avatar.
    48x48_: typing.Optional[str] = Field(None, alias='48x48')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
