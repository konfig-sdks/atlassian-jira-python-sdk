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


class RequiredUpdateScreenTypes(TypedDict):
    pass

class OptionalUpdateScreenTypes(TypedDict, total=False):
    # The ID of the create screen. To remove the screen association, pass a null.
    create: str

    # The ID of the default screen. When specified, must include a screen ID as a default screen is required.
    default: str

    # The ID of the edit screen. To remove the screen association, pass a null.
    edit: str

    # The ID of the view screen. To remove the screen association, pass a null.
    view: str

class UpdateScreenTypes(RequiredUpdateScreenTypes, OptionalUpdateScreenTypes):
    pass