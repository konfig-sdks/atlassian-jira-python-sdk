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

from atlassian_jira_python_sdk.pydantic.bulk_change_owner_details import BulkChangeOwnerDetails
from atlassian_jira_python_sdk.pydantic.bulk_edit_shareable_entity_request_entity_ids import BulkEditShareableEntityRequestEntityIds
from atlassian_jira_python_sdk.pydantic.permission_details import PermissionDetails

class BulkEditShareableEntityRequest(BaseModel):
    # Allowed action for bulk edit shareable entity
    action: Literal["changeOwner", "changePermission", "addPermission", "removePermission"] = Field(alias='action')

    entity_ids: BulkEditShareableEntityRequestEntityIds = Field(alias='entityIds')

    # The details of change owner action.
    change_owner_details: typing.Optional[BulkChangeOwnerDetails] = Field(None, alias='changeOwnerDetails')

    # Whether the actions are executed by users with Administer Jira global permission.
    extend_admin_permissions: typing.Optional[bool] = Field(None, alias='extendAdminPermissions')

    # The permission details to be changed.
    permission_details: typing.Optional[PermissionDetails] = Field(None, alias='permissionDetails')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
