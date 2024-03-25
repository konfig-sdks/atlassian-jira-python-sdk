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

from atlassian_jira_python_sdk.pydantic.issues_jql_meta_data_bean_validation_warnings import IssuesJqlMetaDataBeanValidationWarnings

class IssuesJqlMetaDataBean(BaseModel):
    # The number of issues that were loaded in this evaluation.
    count: int = Field(alias='count')

    # The maximum number of issues that could be loaded in this evaluation.
    max_results: int = Field(alias='maxResults')

    # The index of the first issue.
    start_at: int = Field(alias='startAt')

    # The total number of issues the JQL returned.
    total_count: int = Field(alias='totalCount')

    validation_warnings: typing.Optional[IssuesJqlMetaDataBeanValidationWarnings] = Field(None, alias='validationWarnings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
