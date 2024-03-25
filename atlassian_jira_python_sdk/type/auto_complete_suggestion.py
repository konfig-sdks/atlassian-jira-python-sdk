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


class RequiredAutoCompleteSuggestion(TypedDict):
    pass

class OptionalAutoCompleteSuggestion(TypedDict, total=False):
    # The display name of a suggested item. If `fieldValue` or `predicateValue` are provided, the matching text is highlighted with the HTML bold tag.
    displayName: str

    # The value of a suggested item.
    value: str

class AutoCompleteSuggestion(RequiredAutoCompleteSuggestion, OptionalAutoCompleteSuggestion):
    pass