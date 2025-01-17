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


class CustomFieldContext(BaseModel):
    # The description of the context.
    description: str = Field(alias='description')

    # The ID of the context.
    id: str = Field(alias='id')

    # Whether the context apply to all issue types.
    is_any_issue_type: bool = Field(alias='isAnyIssueType')

    # Whether the context is global.
    is_global_context: bool = Field(alias='isGlobalContext')

    # The name of the context.
    name: str = Field(alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
