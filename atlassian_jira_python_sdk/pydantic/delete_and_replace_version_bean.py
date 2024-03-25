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

from atlassian_jira_python_sdk.pydantic.custom_field_replacement import CustomFieldReplacement

class DeleteAndReplaceVersionBean(BaseModel):
    # An array of custom field IDs (`customFieldId`) and version IDs (`moveTo`) to update when the fields contain the deleted version.
    custom_field_replacement_list: typing.Optional[typing.List[CustomFieldReplacement]] = Field(None, alias='customFieldReplacementList')

    # The ID of the version to update `affectedVersion` to when the field contains the deleted version.
    move_affected_issues_to: typing.Optional[int] = Field(None, alias='moveAffectedIssuesTo')

    # The ID of the version to update `fixVersion` to when the field contains the deleted version.
    move_fix_issues_to: typing.Optional[int] = Field(None, alias='moveFixIssuesTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
