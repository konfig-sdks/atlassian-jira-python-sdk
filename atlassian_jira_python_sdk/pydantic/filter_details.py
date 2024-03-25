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

from atlassian_jira_python_sdk.pydantic.filter_subscription import FilterSubscription
from atlassian_jira_python_sdk.pydantic.share_permission import SharePermission
from atlassian_jira_python_sdk.pydantic.user import User

class FilterDetails(BaseModel):
    # The name of the filter.
    name: str = Field(alias='name')

    # The description of the filter.
    description: typing.Optional[str] = Field(None, alias='description')

    # \\[Experimental\\] Approximate last used time. Returns the date and time when the filter was last used. Returns `null` if the filter hasn't been used after tracking was enabled. For performance reasons, timestamps aren't updated in real time and therefore may not be exactly accurate.
    approximate_last_used: typing.Optional[datetime] = Field(None, alias='approximateLastUsed')

    # The groups and projects that can edit the filter. This can be specified when updating a filter, but not when creating a filter.
    edit_permissions: typing.Optional[typing.List[SharePermission]] = Field(None, alias='editPermissions')

    # Expand options that include additional filter details in the response.
    expand: typing.Optional[str] = Field(None, alias='expand')

    # Whether the filter is selected as a favorite by any users, not including the filter owner.
    favourite: typing.Optional[bool] = Field(None, alias='favourite')

    # The count of how many users have selected this filter as a favorite, including the filter owner.
    favourited_count: typing.Optional[int] = Field(None, alias='favouritedCount')

    # The unique identifier for the filter.
    id: typing.Optional[str] = Field(None, alias='id')

    # The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*.
    jql: typing.Optional[str] = Field(None, alias='jql')

    # The user who owns the filter. Defaults to the creator of the filter, however, Jira administrators can change the owner of a shared filter in the admin settings.
    owner: typing.Optional[User] = Field(None, alias='owner')

    # A URL to view the filter results in Jira, using the [Search for issues using JQL](https://dac-static.atlassian.com) operation with the filter's JQL string to return the filter results. For example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.
    search_url: typing.Optional[str] = Field(None, alias='searchUrl')

    # The URL of the filter.
    self_: typing.Optional[str] = Field(None, alias='self')

    # The groups and projects that the filter is shared with. This can be specified when updating a filter, but not when creating a filter.
    share_permissions: typing.Optional[typing.List[SharePermission]] = Field(None, alias='sharePermissions')

    # The users that are subscribed to the filter.
    subscriptions: typing.Optional[typing.List[FilterSubscription]] = Field(None, alias='subscriptions')

    # A URL to view the filter results in Jira, using the ID of the filter. For example, *https://your-domain.atlassian.net/issues/?filter=10100*.
    view_url: typing.Optional[str] = Field(None, alias='viewUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
