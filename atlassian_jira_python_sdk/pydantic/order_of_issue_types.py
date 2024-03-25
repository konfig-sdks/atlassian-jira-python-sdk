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

from atlassian_jira_python_sdk.pydantic.order_of_issue_types_issue_type_ids import OrderOfIssueTypesIssueTypeIds

class OrderOfIssueTypes(BaseModel):
    issue_type_ids: OrderOfIssueTypesIssueTypeIds = Field(alias='issueTypeIds')

    # The ID of the issue type to place the moved issue types after. Required if `position` isn't provided.
    after: typing.Optional[str] = Field(None, alias='after')

    # The position the issue types should be moved to. Required if `after` isn't provided.
    position: typing.Optional[Literal["First", "Last"]] = Field(None, alias='position')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )