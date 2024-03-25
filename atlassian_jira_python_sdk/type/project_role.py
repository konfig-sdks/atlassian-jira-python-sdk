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

from atlassian_jira_python_sdk.type.role_actor import RoleActor
from atlassian_jira_python_sdk.type.scope import Scope

RequiredProjectRole = TypedDict("RequiredProjectRole", {
    })

OptionalProjectRole = TypedDict("OptionalProjectRole", {
    # The description of the project role.
    "description": str,

    # The list of users who act in this role.
    "actors": typing.List[RoleActor],

    # Whether this role is the admin role for the project.
    "admin": bool,

    # Whether the calling user is part of this role.
    "currentUserRole": bool,

    # Whether this role is the default role for the project
    "default": bool,

    # The ID of the project role.
    "id": int,

    # The name of the project role.
    "name": str,

    # Whether the roles are configurable for this project.
    "roleConfigurable": bool,

    # The scope of the role. Indicated for roles associated with [next-gen projects](https://confluence.atlassian.com/x/loMyO).
    "scope": Scope,

    # The URL the project role details.
    "self": str,

    # The translated name of the project role.
    "translatedName": str,
    }, total=False)

class ProjectRole(RequiredProjectRole, OptionalProjectRole):
    pass
