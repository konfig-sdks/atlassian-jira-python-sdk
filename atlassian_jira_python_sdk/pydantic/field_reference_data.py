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

from atlassian_jira_python_sdk.pydantic.field_reference_data_operators import FieldReferenceDataOperators
from atlassian_jira_python_sdk.pydantic.field_reference_data_types import FieldReferenceDataTypes

class FieldReferenceData(BaseModel):
    # Whether the field provide auto-complete suggestions.
    auto: typing.Optional[Literal["true", "false"]] = Field(None, alias='auto')

    # If the item is a custom field, the ID of the custom field.
    cfid: typing.Optional[str] = Field(None, alias='cfid')

    # Whether this field has been deprecated.
    deprecated: typing.Optional[Literal["true", "false"]] = Field(None, alias='deprecated')

    # The searcher key of the field, only passed when the field is deprecated.
    deprecated_searcher_key: typing.Optional[str] = Field(None, alias='deprecatedSearcherKey')

    # The display name contains the following:   *  for system fields, the field name. For example, `Summary`.  *  for collapsed custom fields, the field name followed by a hyphen and then the field name and field type. For example, `Component - Component[Dropdown]`.  *  for other custom fields, the field name followed by a hyphen and then the custom field ID. For example, `Component - cf[10061]`.
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    operators: typing.Optional[FieldReferenceDataOperators] = Field(None, alias='operators')

    # Whether the field can be used in a query's `ORDER BY` clause.
    orderable: typing.Optional[Literal["true", "false"]] = Field(None, alias='orderable')

    # Whether the content of this field can be searched.
    searchable: typing.Optional[Literal["true", "false"]] = Field(None, alias='searchable')

    types: typing.Optional[FieldReferenceDataTypes] = Field(None, alias='types')

    # The field identifier.
    value: typing.Optional[str] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )