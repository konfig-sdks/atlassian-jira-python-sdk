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


RequiredProjectCategory = TypedDict("RequiredProjectCategory", {
    })

OptionalProjectCategory = TypedDict("OptionalProjectCategory", {
    # The description of the project category.
    "description": str,

    # The ID of the project category.
    "id": str,

    # The name of the project category. Required on create, optional on update.
    "name": str,

    # The URL of the project category.
    "self": str,
    }, total=False)

class ProjectCategory(RequiredProjectCategory, OptionalProjectCategory):
    pass
