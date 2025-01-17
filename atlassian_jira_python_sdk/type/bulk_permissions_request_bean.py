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

from atlassian_jira_python_sdk.type.bulk_permissions_request_bean_global_permissions import BulkPermissionsRequestBeanGlobalPermissions
from atlassian_jira_python_sdk.type.bulk_project_permissions import BulkProjectPermissions

class RequiredBulkPermissionsRequestBean(TypedDict):
    pass

class OptionalBulkPermissionsRequestBean(TypedDict, total=False):
    # The account ID of a user.
    accountId: str

    globalPermissions: BulkPermissionsRequestBeanGlobalPermissions

    # Project permissions with associated projects and issues to look up.
    projectPermissions: typing.List[BulkProjectPermissions]

class BulkPermissionsRequestBean(RequiredBulkPermissionsRequestBean, OptionalBulkPermissionsRequestBean):
    pass
