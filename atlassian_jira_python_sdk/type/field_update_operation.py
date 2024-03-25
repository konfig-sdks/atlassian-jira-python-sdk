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


class RequiredFieldUpdateOperation(TypedDict):
    pass

class OptionalFieldUpdateOperation(TypedDict, total=False):
    # The value to add to the field.
    add: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The field value to copy from another issue.
    copy: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The value to edit in the field.
    edit: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The value to removed from the field.
    remove: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The value to set in the field.
    set: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class FieldUpdateOperation(RequiredFieldUpdateOperation, OptionalFieldUpdateOperation):
    pass