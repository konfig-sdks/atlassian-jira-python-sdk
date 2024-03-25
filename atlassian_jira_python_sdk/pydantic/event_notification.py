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

from atlassian_jira_python_sdk.pydantic.field_details import FieldDetails
from atlassian_jira_python_sdk.pydantic.group_name import GroupName
from atlassian_jira_python_sdk.pydantic.project_role import ProjectRole
from atlassian_jira_python_sdk.pydantic.user_details import UserDetails

class EventNotification(BaseModel):
    # The email address.
    email_address: typing.Optional[str] = Field(None, alias='emailAddress')

    # Expand options that include additional event notification details in the response.
    expand: typing.Optional[str] = Field(None, alias='expand')

    # The custom user or group field.
    field: typing.Optional[FieldDetails] = Field(None, alias='field')

    # The specified group.
    group: typing.Optional[GroupName] = Field(None, alias='group')

    # The ID of the notification.
    id: typing.Optional[int] = Field(None, alias='id')

    # Identifies the recipients of the notification.
    notification_type: typing.Optional[Literal["CurrentAssignee", "Reporter", "CurrentUser", "ProjectLead", "ComponentLead", "User", "Group", "ProjectRole", "EmailAddress", "AllWatchers", "UserCustomField", "GroupCustomField"]] = Field(None, alias='notificationType')

    # As a group's name can change, use of `recipient` is recommended. The identifier associated with the `notificationType` value that defines the receiver of the notification, where the receiver isn't implied by `notificationType` value. So, when `notificationType` is:   *  `User` The `parameter` is the user account ID.  *  `Group` The `parameter` is the group name.  *  `ProjectRole` The `parameter` is the project role ID.  *  `UserCustomField` The `parameter` is the ID of the custom field.  *  `GroupCustomField` The `parameter` is the ID of the custom field.
    parameter: typing.Optional[str] = Field(None, alias='parameter')

    # The specified project role.
    project_role: typing.Optional[ProjectRole] = Field(None, alias='projectRole')

    # The identifier associated with the `notificationType` value that defines the receiver of the notification, where the receiver isn't implied by the `notificationType` value. So, when `notificationType` is:   *  `User`, `recipient` is the user account ID.  *  `Group`, `recipient` is the group ID.  *  `ProjectRole`, `recipient` is the project role ID.  *  `UserCustomField`, `recipient` is the ID of the custom field.  *  `GroupCustomField`, `recipient` is the ID of the custom field.
    recipient: typing.Optional[str] = Field(None, alias='recipient')

    # The specified user.
    user: typing.Optional[UserDetails] = Field(None, alias='user')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )