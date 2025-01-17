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

from atlassian_jira_python_sdk.type.new_user_details_application_keys import NewUserDetailsApplicationKeys
from atlassian_jira_python_sdk.type.new_user_details_products import NewUserDetailsProducts

RequiredNewUserDetails = TypedDict("RequiredNewUserDetails", {
    # The email address for the user.
    "emailAddress": str,
    })

OptionalNewUserDetails = TypedDict("OptionalNewUserDetails", {
    "applicationKeys": NewUserDetailsApplicationKeys,

    # This property is no longer available. If the user has an Atlassian account, their display name is not changed. If the user does not have an Atlassian account, they are sent an email asking them set up an account.
    "displayName": str,

    # This property is no longer available. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    "key": str,

    # This property is no longer available. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    "name": str,

    # This property is no longer available. If the user has an Atlassian account, their password is not changed. If the user does not have an Atlassian account, they are sent an email asking them set up an account.
    "password": str,

    "products": NewUserDetailsProducts,

    # The URL of the user.
    "self": str,
    }, total=False)

class NewUserDetails(RequiredNewUserDetails, OptionalNewUserDetails):
    pass
