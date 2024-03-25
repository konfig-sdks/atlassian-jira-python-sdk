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


class RequiredProjectRoleGroup(TypedDict):
    pass

class OptionalProjectRoleGroup(TypedDict, total=False):
    # The display name of the group.
    displayName: str

    # The ID of the group.
    groupId: str

    # The name of the group. As a group's name can change, use of `groupId` is recommended to identify the group.
    name: str

class ProjectRoleGroup(RequiredProjectRoleGroup, OptionalProjectRoleGroup):
    pass
