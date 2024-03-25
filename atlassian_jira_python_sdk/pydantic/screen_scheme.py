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

from atlassian_jira_python_sdk.pydantic.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
from atlassian_jira_python_sdk.pydantic.screen_types import ScreenTypes

class ScreenScheme(BaseModel):
    # The description of the screen scheme.
    description: typing.Optional[str] = Field(None, alias='description')

    # The ID of the screen scheme.
    id: typing.Optional[int] = Field(None, alias='id')

    # Details of the issue type screen schemes associated with the screen scheme.
    issue_type_screen_schemes: typing.Optional[PageBeanIssueTypeScreenScheme] = Field(None, alias='issueTypeScreenSchemes')

    # The name of the screen scheme.
    name: typing.Optional[str] = Field(None, alias='name')

    # The IDs of the screens for the screen types of the screen scheme.
    screens: typing.Optional[ScreenTypes] = Field(None, alias='screens')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )