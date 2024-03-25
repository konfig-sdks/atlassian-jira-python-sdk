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


class RequiredUpdatePriorityDetails(TypedDict):
    pass

class OptionalUpdatePriorityDetails(TypedDict, total=False):
    # The description of the priority.
    description: str

    # The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used.
    iconUrl: str

    # The name of the priority. Must be unique.
    name: str

    # The status color of the priority in 3-digit or 6-digit hexadecimal format.
    statusColor: str

class UpdatePriorityDetails(RequiredUpdatePriorityDetails, OptionalUpdatePriorityDetails):
    pass
