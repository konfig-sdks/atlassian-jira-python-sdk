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


class RequiredStatusCreate(TypedDict):
    # The name of the status.
    name: str

    # The category of the status.
    statusCategory: str

class OptionalStatusCreate(TypedDict, total=False):
    # The description of the status.
    description: str

class StatusCreate(RequiredStatusCreate, OptionalStatusCreate):
    pass