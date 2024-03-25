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

from atlassian_jira_python_sdk.pydantic.application_role_default_groups import ApplicationRoleDefaultGroups
from atlassian_jira_python_sdk.pydantic.application_role_groups import ApplicationRoleGroups
from atlassian_jira_python_sdk.pydantic.group_name import GroupName

class ApplicationRole(BaseModel):
    default_groups: typing.Optional[ApplicationRoleDefaultGroups] = Field(None, alias='defaultGroups')

    # The groups that are granted default access for this application role.
    default_groups_details: typing.Optional[typing.List[GroupName]] = Field(None, alias='defaultGroupsDetails')

    # Deprecated.
    defined: typing.Optional[bool] = Field(None, alias='defined')

    # The groups associated with the application role.
    group_details: typing.Optional[typing.List[GroupName]] = Field(None, alias='groupDetails')

    groups: typing.Optional[ApplicationRoleGroups] = Field(None, alias='groups')

    has_unlimited_seats: typing.Optional[bool] = Field(None, alias='hasUnlimitedSeats')

    # The key of the application role.
    key: typing.Optional[str] = Field(None, alias='key')

    # The display name of the application role.
    name: typing.Optional[str] = Field(None, alias='name')

    # The maximum count of users on your license.
    number_of_seats: typing.Optional[int] = Field(None, alias='numberOfSeats')

    # Indicates if the application role belongs to Jira platform (`jira-core`).
    platform: typing.Optional[bool] = Field(None, alias='platform')

    # The count of users remaining on your license.
    remaining_seats: typing.Optional[int] = Field(None, alias='remainingSeats')

    # Determines whether this application role should be selected by default on user creation.
    selected_by_default: typing.Optional[bool] = Field(None, alias='selectedByDefault')

    # The number of users counting against your license.
    user_count: typing.Optional[int] = Field(None, alias='userCount')

    # The [type of users](https://confluence.atlassian.com/x/lRW3Ng) being counted against your license.
    user_count_description: typing.Optional[str] = Field(None, alias='userCountDescription')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )