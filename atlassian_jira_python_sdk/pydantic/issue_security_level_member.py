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

from atlassian_jira_python_sdk.pydantic.permission_holder import PermissionHolder

class IssueSecurityLevelMember(BaseModel):
    # The user or group being granted the permission. It consists of a `type` and a type-dependent `parameter`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information.
    holder: PermissionHolder = Field(alias='holder')

    # The ID of the issue security level member.
    id: int = Field(alias='id')

    # The ID of the issue security level.
    issue_security_level_id: int = Field(alias='issueSecurityLevelId')

    managed: typing.Optional[bool] = Field(None, alias='managed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
