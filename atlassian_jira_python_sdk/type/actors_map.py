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

from atlassian_jira_python_sdk.type.actors_map_group import ActorsMapGroup
from atlassian_jira_python_sdk.type.actors_map_group_id import ActorsMapGroupId
from atlassian_jira_python_sdk.type.actors_map_user import ActorsMapUser

class RequiredActorsMap(TypedDict):
    pass

class OptionalActorsMap(TypedDict, total=False):
    group: ActorsMapGroup

    groupId: ActorsMapGroupId

    user: ActorsMapUser

class ActorsMap(RequiredActorsMap, OptionalActorsMap):
    pass
