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


class RequiredTimeTrackingProvider(TypedDict):
    # The key for the time tracking provider. For example, *JIRA*.
    key: str

class OptionalTimeTrackingProvider(TypedDict, total=False):
    # The name of the time tracking provider. For example, *JIRA provided time tracking*.
    name: str

    # The URL of the configuration page for the time tracking provider app. For example, */example/config/url*. This property is only returned if the `adminPageKey` property is set in the module descriptor of the time tracking provider app.
    url: str

class TimeTrackingProvider(RequiredTimeTrackingProvider, OptionalTimeTrackingProvider):
    pass
