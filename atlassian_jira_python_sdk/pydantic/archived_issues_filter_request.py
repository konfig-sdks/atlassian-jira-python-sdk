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

from atlassian_jira_python_sdk.pydantic.archived_issues_filter_request_archived_by import ArchivedIssuesFilterRequestArchivedBy
from atlassian_jira_python_sdk.pydantic.archived_issues_filter_request_issue_types import ArchivedIssuesFilterRequestIssueTypes
from atlassian_jira_python_sdk.pydantic.archived_issues_filter_request_projects import ArchivedIssuesFilterRequestProjects
from atlassian_jira_python_sdk.pydantic.archived_issues_filter_request_reporters import ArchivedIssuesFilterRequestReporters
from atlassian_jira_python_sdk.pydantic.date_range_filter_request import DateRangeFilterRequest

class ArchivedIssuesFilterRequest(BaseModel):
    archived_by: typing.Optional[ArchivedIssuesFilterRequestArchivedBy] = Field(None, alias='archivedBy')

    archived_date_range: typing.Optional[DateRangeFilterRequest] = Field(None, alias='archivedDateRange')

    issue_types: typing.Optional[ArchivedIssuesFilterRequestIssueTypes] = Field(None, alias='issueTypes')

    projects: typing.Optional[ArchivedIssuesFilterRequestProjects] = Field(None, alias='projects')

    reporters: typing.Optional[ArchivedIssuesFilterRequestReporters] = Field(None, alias='reporters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )