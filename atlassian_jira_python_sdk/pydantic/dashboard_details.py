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

from atlassian_jira_python_sdk.pydantic.share_permission import SharePermission

class DashboardDetails(BaseModel):
    # The edit permissions for the dashboard.
    edit_permissions: typing.List[SharePermission] = Field(alias='editPermissions')

    # The name of the dashboard.
    name: str = Field(alias='name')

    # The share permissions for the dashboard.
    share_permissions: typing.List[SharePermission] = Field(alias='sharePermissions')

    # The description of the dashboard.
    description: typing.Optional[str] = Field(None, alias='description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
