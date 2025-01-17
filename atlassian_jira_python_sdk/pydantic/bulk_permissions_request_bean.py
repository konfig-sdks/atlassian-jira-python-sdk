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

from atlassian_jira_python_sdk.pydantic.bulk_permissions_request_bean_global_permissions import BulkPermissionsRequestBeanGlobalPermissions
from atlassian_jira_python_sdk.pydantic.bulk_project_permissions import BulkProjectPermissions

class BulkPermissionsRequestBean(BaseModel):
    # The account ID of a user.
    account_id: typing.Optional[str] = Field(None, alias='accountId')

    global_permissions: typing.Optional[BulkPermissionsRequestBeanGlobalPermissions] = Field(None, alias='globalPermissions')

    # Project permissions with associated projects and issues to look up.
    project_permissions: typing.Optional[typing.List[BulkProjectPermissions]] = Field(None, alias='projectPermissions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
