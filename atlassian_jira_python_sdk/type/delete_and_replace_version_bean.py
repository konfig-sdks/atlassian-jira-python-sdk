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

from atlassian_jira_python_sdk.type.custom_field_replacement import CustomFieldReplacement

class RequiredDeleteAndReplaceVersionBean(TypedDict):
    pass

class OptionalDeleteAndReplaceVersionBean(TypedDict, total=False):
    # An array of custom field IDs (`customFieldId`) and version IDs (`moveTo`) to update when the fields contain the deleted version.
    customFieldReplacementList: typing.List[CustomFieldReplacement]

    # The ID of the version to update `affectedVersion` to when the field contains the deleted version.
    moveAffectedIssuesTo: int

    # The ID of the version to update `fixVersion` to when the field contains the deleted version.
    moveFixIssuesTo: int

class DeleteAndReplaceVersionBean(RequiredDeleteAndReplaceVersionBean, OptionalDeleteAndReplaceVersionBean):
    pass
