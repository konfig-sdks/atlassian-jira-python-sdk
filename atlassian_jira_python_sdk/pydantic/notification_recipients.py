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

from atlassian_jira_python_sdk.pydantic.group_name import GroupName
from atlassian_jira_python_sdk.pydantic.notification_recipients_group_ids import NotificationRecipientsGroupIds
from atlassian_jira_python_sdk.pydantic.user_details import UserDetails

class NotificationRecipients(BaseModel):
    # Whether the notification should be sent to the issue's assignees.
    assignee: typing.Optional[bool] = Field(None, alias='assignee')

    group_ids: typing.Optional[NotificationRecipientsGroupIds] = Field(None, alias='groupIds')

    # List of groups to receive the notification.
    groups: typing.Optional[typing.List[GroupName]] = Field(None, alias='groups')

    # Whether the notification should be sent to the issue's reporter.
    reporter: typing.Optional[bool] = Field(None, alias='reporter')

    # List of users to receive the notification.
    users: typing.Optional[typing.List[UserDetails]] = Field(None, alias='users')

    # Whether the notification should be sent to the issue's voters.
    voters: typing.Optional[bool] = Field(None, alias='voters')

    # Whether the notification should be sent to the issue's watchers.
    watchers: typing.Optional[bool] = Field(None, alias='watchers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
