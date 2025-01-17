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

from atlassian_jira_python_sdk.pydantic.filter_subscriptions_list import FilterSubscriptionsList
from atlassian_jira_python_sdk.pydantic.share_permission import SharePermission
from atlassian_jira_python_sdk.pydantic.user import User
from atlassian_jira_python_sdk.pydantic.user_list import UserList

class Filter(BaseModel):
    # The name of the filter. Must be unique.
    name: str = Field(alias='name')

    # A description of the filter.
    description: typing.Optional[str] = Field(None, alias='description')

    # \\[Experimental\\] Approximate last used time. Returns the date and time when the filter was last used. Returns `null` if the filter hasn't been used after tracking was enabled. For performance reasons, timestamps aren't updated in real time and therefore may not be exactly accurate.
    approximate_last_used: typing.Optional[datetime] = Field(None, alias='approximateLastUsed')

    # The groups and projects that can edit the filter.
    edit_permissions: typing.Optional[typing.List[SharePermission]] = Field(None, alias='editPermissions')

    # Whether the filter is selected as a favorite.
    favourite: typing.Optional[bool] = Field(None, alias='favourite')

    # The count of how many users have selected this filter as a favorite, including the filter owner.
    favourited_count: typing.Optional[int] = Field(None, alias='favouritedCount')

    # The unique identifier for the filter.
    id: typing.Optional[str] = Field(None, alias='id')

    # The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*.
    jql: typing.Optional[str] = Field(None, alias='jql')

    # The user who owns the filter. This is defaulted to the creator of the filter, however Jira administrators can change the owner of a shared filter in the admin settings.
    owner: typing.Optional[User] = Field(None, alias='owner')

    # A URL to view the filter results in Jira, using the [Search for issues using JQL](https://dac-static.atlassian.com) operation with the filter's JQL string to return the filter results. For example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.
    search_url: typing.Optional[str] = Field(None, alias='searchUrl')

    # The URL of the filter.
    self_: typing.Optional[str] = Field(None, alias='self')

    # The groups and projects that the filter is shared with.
    share_permissions: typing.Optional[typing.List[SharePermission]] = Field(None, alias='sharePermissions')

    # A paginated list of the users that the filter is shared with. This includes users that are members of the groups or can browse the projects that the filter is shared with.
    shared_users: typing.Optional[UserList] = Field(None, alias='sharedUsers')

    # A paginated list of the users that are subscribed to the filter.
    subscriptions: typing.Optional[FilterSubscriptionsList] = Field(None, alias='subscriptions')

    # A URL to view the filter results in Jira, using the ID of the filter. For example, *https://your-domain.atlassian.net/issues/?filter=10100*.
    view_url: typing.Optional[str] = Field(None, alias='viewUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
