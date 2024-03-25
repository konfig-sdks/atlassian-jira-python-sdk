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

from atlassian_jira_python_sdk.type.share_permission import SharePermission

class RequiredDashboardDetails(TypedDict):
    # The edit permissions for the dashboard.
    editPermissions: typing.List[SharePermission]

    # The name of the dashboard.
    name: str

    # The share permissions for the dashboard.
    sharePermissions: typing.List[SharePermission]

class OptionalDashboardDetails(TypedDict, total=False):
    # The description of the dashboard.
    description: str

class DashboardDetails(RequiredDashboardDetails, OptionalDashboardDetails):
    pass
