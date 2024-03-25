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


class Resource(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    file: typing.Optional[typing.IO] = Field(None, alias='file')

    filename: typing.Optional[str] = Field(None, alias='filename')

    input_stream: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='inputStream')

    open: typing.Optional[bool] = Field(None, alias='open')

    readable: typing.Optional[bool] = Field(None, alias='readable')

    uri: typing.Optional[str] = Field(None, alias='uri')

    url: typing.Optional[str] = Field(None, alias='url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
