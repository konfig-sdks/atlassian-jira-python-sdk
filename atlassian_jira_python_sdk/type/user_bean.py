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

from atlassian_jira_python_sdk.type.user_bean_avatar_urls import UserBeanAvatarUrls

RequiredUserBean = TypedDict("RequiredUserBean", {
    })

OptionalUserBean = TypedDict("OptionalUserBean", {
    # The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    "accountId": str,

    # Whether the user is active.
    "active": bool,

    # The avatars of the user.
    "avatarUrls": UserBeanAvatarUrls,

    # The display name of the user. Depending on the user’s privacy setting, this may return an alternative value.
    "displayName": str,

    # This property is deprecated in favor of `accountId` because of privacy changes. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.   The key of the user.
    "key": str,

    # This property is deprecated in favor of `accountId` because of privacy changes. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.   The username of the user.
    "name": str,

    # The URL of the user.
    "self": str,
    }, total=False)

class UserBean(RequiredUserBean, OptionalUserBean):
    pass
