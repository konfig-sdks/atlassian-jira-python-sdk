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

from atlassian_jira_python_sdk.pydantic.time_tracking_configuration import TimeTrackingConfiguration

class Configuration(BaseModel):
    # Whether the ability to add attachments to issues is enabled.
    attachments_enabled: typing.Optional[bool] = Field(None, alias='attachmentsEnabled')

    # Whether the ability to link issues is enabled.
    issue_linking_enabled: typing.Optional[bool] = Field(None, alias='issueLinkingEnabled')

    # Whether the ability to create subtasks for issues is enabled.
    sub_tasks_enabled: typing.Optional[bool] = Field(None, alias='subTasksEnabled')

    # The configuration of time tracking.
    time_tracking_configuration: typing.Optional[TimeTrackingConfiguration] = Field(None, alias='timeTrackingConfiguration')

    # Whether the ability to track time is enabled. This property is deprecated.
    time_tracking_enabled: typing.Optional[bool] = Field(None, alias='timeTrackingEnabled')

    # Whether the ability to create unassigned issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.
    unassigned_issues_allowed: typing.Optional[bool] = Field(None, alias='unassignedIssuesAllowed')

    # Whether the ability for users to vote on issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.
    voting_enabled: typing.Optional[bool] = Field(None, alias='votingEnabled')

    # Whether the ability for users to watch issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.
    watching_enabled: typing.Optional[bool] = Field(None, alias='watchingEnabled')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
