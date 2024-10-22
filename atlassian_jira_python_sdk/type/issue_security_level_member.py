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

from atlassian_jira_python_sdk.type.permission_holder import PermissionHolder

class RequiredIssueSecurityLevelMember(TypedDict):
    # The user or group being granted the permission. It consists of a `type` and a type-dependent `parameter`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information.
    holder: PermissionHolder

    # The ID of the issue security level member.
    id: int

    # The ID of the issue security level.
    issueSecurityLevelId: int

class OptionalIssueSecurityLevelMember(TypedDict, total=False):
    managed: bool

class IssueSecurityLevelMember(RequiredIssueSecurityLevelMember, OptionalIssueSecurityLevelMember):
    pass
