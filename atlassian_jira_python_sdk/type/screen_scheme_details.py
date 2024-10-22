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

from atlassian_jira_python_sdk.type.screen_types import ScreenTypes

class RequiredScreenSchemeDetails(TypedDict):
    # The name of the screen scheme. The name must be unique. The maximum length is 255 characters.
    name: str

    # The IDs of the screens for the screen types of the screen scheme. Only screens used in classic projects are accepted.
    screens: ScreenTypes

class OptionalScreenSchemeDetails(TypedDict, total=False):
    # The description of the screen scheme. The maximum length is 255 characters.
    description: str

class ScreenSchemeDetails(RequiredScreenSchemeDetails, OptionalScreenSchemeDetails):
    pass
