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

from atlassian_jira_python_sdk.type.field_details_clause_names import FieldDetailsClauseNames
from atlassian_jira_python_sdk.type.json_type_bean import JsonTypeBean
from atlassian_jira_python_sdk.type.scope import Scope

class RequiredFieldDetails(TypedDict):
    pass

class OptionalFieldDetails(TypedDict, total=False):
    clauseNames: FieldDetailsClauseNames

    # Whether the field is a custom field.
    custom: bool

    # The ID of the field.
    id: str

    # The key of the field.
    key: str

    # The name of the field.
    name: str

    # Whether the field can be used as a column on the issue navigator.
    navigable: bool

    # Whether the content of the field can be used to order lists.
    orderable: bool

    # The data schema for the field.
    schema: JsonTypeBean

    # The scope of the field.
    scope: Scope

    # Whether the content of the field can be searched.
    searchable: bool

class FieldDetails(RequiredFieldDetails, OptionalFieldDetails):
    pass
