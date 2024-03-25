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

from atlassian_jira_python_sdk.pydantic.simple_link import SimpleLink

class LinkGroup(BaseModel):
    groups: typing.Optional['typing.List["LinkGroup"]'] = Field(None, alias='groups')

    header: typing.Optional[SimpleLink] = Field(None, alias='header')

    id: typing.Optional[str] = Field(None, alias='id')

    links: typing.Optional[typing.List[SimpleLink]] = Field(None, alias='links')

    style_class: typing.Optional[str] = Field(None, alias='styleClass')

    weight: typing.Optional[int] = Field(None, alias='weight')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )