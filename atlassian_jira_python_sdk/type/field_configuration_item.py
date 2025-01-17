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


class RequiredFieldConfigurationItem(TypedDict):
    # The ID of the field within the field configuration.
    id: str

class OptionalFieldConfigurationItem(TypedDict, total=False):
    # The description of the field within the field configuration.
    description: str

    # Whether the field is hidden in the field configuration.
    isHidden: bool

    # Whether the field is required in the field configuration.
    isRequired: bool

    # The renderer type for the field within the field configuration.
    renderer: str

class FieldConfigurationItem(RequiredFieldConfigurationItem, OptionalFieldConfigurationItem):
    pass
