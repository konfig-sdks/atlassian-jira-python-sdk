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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from atlassian_jira_python_sdk.pydantic.permission_grant import PermissionGrant
from atlassian_jira_python_sdk.pydantic.scope import Scope

class PermissionScheme(BaseModel):
    # The name of the permission scheme. Must be unique.
    name: str = Field(alias='name')

    # A description for the permission scheme.
    description: typing.Optional[str] = Field(None, alias='description')

    # The expand options available for the permission scheme.
    expand: typing.Optional[str] = Field(None, alias='expand')

    # The ID of the permission scheme.
    id: typing.Optional[int] = Field(None, alias='id')

    # The permission scheme to create or update. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more information.
    permissions: typing.Optional[typing.List[PermissionGrant]] = Field(None, alias='permissions')

    scope: typing.Optional[Scope] = Field(None, alias='scope')

    # The URL of the permission scheme.
    self_: typing.Optional[str] = Field(None, alias='self')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
