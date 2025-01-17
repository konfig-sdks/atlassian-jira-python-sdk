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

from atlassian_jira_python_sdk.pydantic.field_metadata_allowed_values import FieldMetadataAllowedValues
from atlassian_jira_python_sdk.pydantic.field_metadata_configuration import FieldMetadataConfiguration
from atlassian_jira_python_sdk.pydantic.field_metadata_operations import FieldMetadataOperations
from atlassian_jira_python_sdk.pydantic.json_type_bean import JsonTypeBean

class FieldMetadata(BaseModel):
    # The key of the field.
    key: str = Field(alias='key')

    # The name of the field.
    name: str = Field(alias='name')

    operations: FieldMetadataOperations = Field(alias='operations')

    # Whether the field is required.
    required: bool = Field(alias='required')

    # The data type of the field.
    schema: JsonTypeBean = Field(alias='schema')

    allowed_values: typing.Optional[FieldMetadataAllowedValues] = Field(None, alias='allowedValues')

    # The URL that can be used to automatically complete the field.
    auto_complete_url: typing.Optional[str] = Field(None, alias='autoCompleteUrl')

    configuration: typing.Optional[FieldMetadataConfiguration] = Field(None, alias='configuration')

    # The default value of the field.
    default_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='defaultValue')

    # Whether the field has a default value.
    has_default_value: typing.Optional[bool] = Field(None, alias='hasDefaultValue')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
