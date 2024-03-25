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

from atlassian_jira_python_sdk.type.field_metadata_allowed_values import FieldMetadataAllowedValues
from atlassian_jira_python_sdk.type.field_metadata_configuration import FieldMetadataConfiguration
from atlassian_jira_python_sdk.type.field_metadata_operations import FieldMetadataOperations
from atlassian_jira_python_sdk.type.json_type_bean import JsonTypeBean

class RequiredFieldMetadata(TypedDict):
    # The key of the field.
    key: str

    # The name of the field.
    name: str

    operations: FieldMetadataOperations

    # Whether the field is required.
    required: bool

    # The data type of the field.
    schema: JsonTypeBean

class OptionalFieldMetadata(TypedDict, total=False):
    allowedValues: FieldMetadataAllowedValues

    # The URL that can be used to automatically complete the field.
    autoCompleteUrl: str

    configuration: FieldMetadataConfiguration

    # The default value of the field.
    defaultValue: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Whether the field has a default value.
    hasDefaultValue: bool

class FieldMetadata(RequiredFieldMetadata, OptionalFieldMetadata):
    pass