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


class CustomFieldContextProjectMapping(BaseModel):
    # The ID of the context.
    context_id: str = Field(alias='contextId')

    # Whether context is global.
    is_global_context: typing.Optional[bool] = Field(None, alias='isGlobalContext')

    # The ID of the project.
    project_id: typing.Optional[str] = Field(None, alias='projectId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )