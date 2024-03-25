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


class UpdatePriorityDetails(BaseModel):
    # The description of the priority.
    description: typing.Optional[str] = Field(None, alias='description')

    # The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used.
    icon_url: typing.Optional[Literal["/images/icons/priorities/blocker.png", "/images/icons/priorities/critical.png", "/images/icons/priorities/high.png", "/images/icons/priorities/highest.png", "/images/icons/priorities/low.png", "/images/icons/priorities/lowest.png", "/images/icons/priorities/major.png", "/images/icons/priorities/medium.png", "/images/icons/priorities/minor.png", "/images/icons/priorities/trivial.png"]] = Field(None, alias='iconUrl')

    # The name of the priority. Must be unique.
    name: typing.Optional[str] = Field(None, alias='name')

    # The status color of the priority in 3-digit or 6-digit hexadecimal format.
    status_color: typing.Optional[str] = Field(None, alias='statusColor')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
