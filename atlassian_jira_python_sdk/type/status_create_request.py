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

from atlassian_jira_python_sdk.type.status_create import StatusCreate
from atlassian_jira_python_sdk.type.status_scope import StatusScope

class RequiredStatusCreateRequest(TypedDict):
    scope: StatusScope

    # Details of the statuses being created.
    statuses: typing.List[StatusCreate]

class OptionalStatusCreateRequest(TypedDict, total=False):
    pass

class StatusCreateRequest(RequiredStatusCreateRequest, OptionalStatusCreateRequest):
    pass