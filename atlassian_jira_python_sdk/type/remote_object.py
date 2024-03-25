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

from atlassian_jira_python_sdk.type.icon import Icon
from atlassian_jira_python_sdk.type.status import Status

class RequiredRemoteObject(TypedDict):
    # The title of the item.
    title: str

    # The URL of the item.
    url: str

class OptionalRemoteObject(TypedDict, total=False):
    # The summary details of the item.
    summary: str

    icon: Icon

    status: Status

class RemoteObject(RequiredRemoteObject, OptionalRemoteObject):
    pass
