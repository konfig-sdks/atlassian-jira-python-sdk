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

from atlassian_jira_python_sdk.type.user_picker_user import UserPickerUser

class RequiredFoundUsers(TypedDict):
    pass

class OptionalFoundUsers(TypedDict, total=False):
    # Header text indicating the number of users in the response and the total number of users found in the search.
    header: str

    # The total number of users found in the search.
    total: int

    users: typing.List[UserPickerUser]

class FoundUsers(RequiredFoundUsers, OptionalFoundUsers):
    pass