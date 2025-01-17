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

from atlassian_jira_python_sdk.type.user import User

RequiredUserList = TypedDict("RequiredUserList", {
    })

OptionalUserList = TypedDict("OptionalUserList", {
    # The index of the last item returned on the page.
    "end-index": int,

    # The list of items.
    "items": typing.List[User],

    # The maximum number of results that could be on the page.
    "max-results": int,

    # The number of items on the page.
    "size": int,

    # The index of the first item returned on the page.
    "start-index": int,
    }, total=False)

class UserList(RequiredUserList, OptionalUserList):
    pass
