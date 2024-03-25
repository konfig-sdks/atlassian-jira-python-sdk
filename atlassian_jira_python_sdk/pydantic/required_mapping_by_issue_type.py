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

from atlassian_jira_python_sdk.pydantic.required_mapping_by_issue_type_status_ids import RequiredMappingByIssueTypeStatusIds

class RequiredMappingByIssueType(BaseModel):
    # The ID of the issue type.
    issue_type_id: typing.Optional[str] = Field(None, alias='issueTypeId')

    status_ids: typing.Optional[RequiredMappingByIssueTypeStatusIds] = Field(None, alias='statusIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )