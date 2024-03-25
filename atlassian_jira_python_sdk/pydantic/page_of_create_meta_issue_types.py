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

from atlassian_jira_python_sdk.pydantic.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata

class PageOfCreateMetaIssueTypes(BaseModel):
    create_meta_issue_type: typing.Optional[typing.List[IssueTypeIssueCreateMetadata]] = Field(None, alias='createMetaIssueType')

    # The list of CreateMetaIssueType.
    issue_types: typing.Optional[typing.List[IssueTypeIssueCreateMetadata]] = Field(None, alias='issueTypes')

    # The maximum number of items to return per page.
    max_results: typing.Optional[int] = Field(None, alias='maxResults')

    # The index of the first item returned.
    start_at: typing.Optional[int] = Field(None, alias='startAt')

    # The total number of items in all pages.
    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
