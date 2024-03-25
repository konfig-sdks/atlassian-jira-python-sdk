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

from atlassian_jira_python_sdk.type.application import Application
from atlassian_jira_python_sdk.type.remote_object import RemoteObject

RequiredRemoteIssueLink = TypedDict("RequiredRemoteIssueLink", {
    })

OptionalRemoteIssueLink = TypedDict("OptionalRemoteIssueLink", {
    # Details of the remote application the linked item is in.
    "application": Application,

    # The global ID of the link, such as the ID of the item on the remote system.
    "globalId": str,

    # The ID of the link.
    "id": int,

    # Details of the item linked to.
    "object": RemoteObject,

    # Description of the relationship between the issue and the linked item.
    "relationship": str,

    # The URL of the link.
    "self": str,
    }, total=False)

class RemoteIssueLink(RequiredRemoteIssueLink, OptionalRemoteIssueLink):
    pass
