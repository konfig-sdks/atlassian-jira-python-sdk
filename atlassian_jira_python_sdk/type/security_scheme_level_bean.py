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

from atlassian_jira_python_sdk.type.security_scheme_level_member_bean import SecuritySchemeLevelMemberBean

class RequiredSecuritySchemeLevelBean(TypedDict):
    # The name of the issue security scheme level. Must be unique.
    name: str

class OptionalSecuritySchemeLevelBean(TypedDict, total=False):
    # The description of the issue security scheme level.
    description: str

    # Specifies whether the level is the default level. False by default.
    isDefault: bool

    # The list of level members which should be added to the issue security scheme level.
    members: typing.List[SecuritySchemeLevelMemberBean]

class SecuritySchemeLevelBean(RequiredSecuritySchemeLevelBean, OptionalSecuritySchemeLevelBean):
    pass
