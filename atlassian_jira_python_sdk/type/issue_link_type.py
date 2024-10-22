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


RequiredIssueLinkType = TypedDict("RequiredIssueLinkType", {
    })

OptionalIssueLinkType = TypedDict("OptionalIssueLinkType", {
    # The ID of the issue link type and is used as follows:   *  In the [issueLink](https://dac-static.atlassian.com) resource it is the type of issue link. Required on create when `name` isn't provided. Otherwise, read only.  *  In the [issueLinkType](https://dac-static.atlassian.com) resource it is read only.
    "id": str,

    # The description of the issue link type inward link and is used as follows:   *  In the [issueLink](https://dac-static.atlassian.com) resource it is read only.  *  In the [issueLinkType](https://dac-static.atlassian.com) resource it is required on create and optional on update. Otherwise, read only.
    "inward": str,

    # The name of the issue link type and is used as follows:   *  In the [issueLink](https://dac-static.atlassian.com) resource it is the type of issue link. Required on create when `id` isn't provided. Otherwise, read only.  *  In the [issueLinkType](https://dac-static.atlassian.com) resource it is required on create and optional on update. Otherwise, read only.
    "name": str,

    # The description of the issue link type outward link and is used as follows:   *  In the [issueLink](https://dac-static.atlassian.com) resource it is read only.  *  In the [issueLinkType](https://dac-static.atlassian.com) resource it is required on create and optional on update. Otherwise, read only.
    "outward": str,

    # The URL of the issue link type. Read only.
    "self": str,
    }, total=False)

class IssueLinkType(RequiredIssueLinkType, OptionalIssueLinkType):
    pass
