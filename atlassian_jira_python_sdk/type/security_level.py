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


RequiredSecurityLevel = TypedDict("RequiredSecurityLevel", {
    })

OptionalSecurityLevel = TypedDict("OptionalSecurityLevel", {
    # The description of the issue level security item.
    "description": str,

    # The ID of the issue level security item.
    "id": str,

    # Whether the issue level security item is the default.
    "isDefault": bool,

    # The ID of the issue level security scheme.
    "issueSecuritySchemeId": str,

    # The name of the issue level security item.
    "name": str,

    # The URL of the issue level security item.
    "self": str,
    }, total=False)

class SecurityLevel(RequiredSecurityLevel, OptionalSecurityLevel):
    pass
