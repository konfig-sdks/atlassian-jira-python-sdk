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

from atlassian_jira_python_sdk.pydantic.json_type_bean_configuration import JsonTypeBeanConfiguration

class JsonTypeBean(BaseModel):
    # The data type of the field.
    type: str = Field(alias='type')

    configuration: typing.Optional[JsonTypeBeanConfiguration] = Field(None, alias='configuration')

    # If the field is a custom field, the URI of the field.
    custom: typing.Optional[str] = Field(None, alias='custom')

    # If the field is a custom field, the custom ID of the field.
    custom_id: typing.Optional[int] = Field(None, alias='customId')

    # When the data type is an array, the name of the field items within the array.
    items: typing.Optional[str] = Field(None, alias='items')

    # If the field is a system field, the name of the field.
    system: typing.Optional[str] = Field(None, alias='system')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )