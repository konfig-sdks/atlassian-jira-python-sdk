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


class RequiredCustomFieldReplacement(TypedDict):
    pass

class OptionalCustomFieldReplacement(TypedDict, total=False):
    # The ID of the custom field in which to replace the version number.
    customFieldId: int

    # The version number to use as a replacement for the deleted version.
    moveTo: int

class CustomFieldReplacement(RequiredCustomFieldReplacement, OptionalCustomFieldReplacement):
    pass
