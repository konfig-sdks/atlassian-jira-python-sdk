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


class RequiredVisibility(TypedDict):
    pass

class OptionalVisibility(TypedDict, total=False):
    # The ID of the group or the name of the role that visibility of this item is restricted to.
    identifier: typing.Optional[str]

    # Whether visibility of this item is restricted to a group or role.
    type: str

    # The name of the group or role that visibility of this item is restricted to. Please note that the name of a group is mutable, to reliably identify a group use `identifier`.
    value: str

class Visibility(RequiredVisibility, OptionalVisibility):
    pass
