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

from atlassian_jira_python_sdk.type.user_details import UserDetails

RequiredWatchers = TypedDict("RequiredWatchers", {
    })

OptionalWatchers = TypedDict("OptionalWatchers", {
    # Whether the calling user is watching this issue.
    "isWatching": bool,

    # The URL of these issue watcher details.
    "self": str,

    # The number of users watching this issue.
    "watchCount": int,

    # Details of the users watching this issue.
    "watchers": typing.List[UserDetails],
    }, total=False)

class Watchers(RequiredWatchers, OptionalWatchers):
    pass