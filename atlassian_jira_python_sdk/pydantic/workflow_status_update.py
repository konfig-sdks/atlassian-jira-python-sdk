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


class WorkflowStatusUpdate(BaseModel):
    # The name of the status.
    name: str = Field(alias='name')

    # The category of the status.
    status_category: Literal["TODO", "IN_PROGRESS", "DONE"] = Field(alias='statusCategory')

    # The reference of the status.
    status_reference: str = Field(alias='statusReference')

    # The description of the status.
    description: typing.Optional[str] = Field(None, alias='description')

    # The ID of the status.
    id: typing.Optional[str] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
