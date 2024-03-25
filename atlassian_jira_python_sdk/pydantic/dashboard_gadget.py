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

from atlassian_jira_python_sdk.pydantic.dashboard_gadget_position import DashboardGadgetPosition

class DashboardGadget(BaseModel):
    # The title of the gadget.
    title: str = Field(alias='title')

    # The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`.
    color: Literal["blue", "red", "yellow", "green", "cyan", "purple", "gray", "white"] = Field(alias='color')

    # The ID of the gadget instance.
    id: int = Field(alias='id')

    # The position of the gadget.
    position: DashboardGadgetPosition = Field(alias='position')

    # The module key of the gadget type.
    module_key: typing.Optional[str] = Field(None, alias='moduleKey')

    # The URI of the gadget type.
    uri: typing.Optional[str] = Field(None, alias='uri')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
