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

from atlassian_jira_python_sdk.type.detailed_error_collection_details import DetailedErrorCollectionDetails
from atlassian_jira_python_sdk.type.detailed_error_collection_error_messages import DetailedErrorCollectionErrorMessages
from atlassian_jira_python_sdk.type.detailed_error_collection_errors import DetailedErrorCollectionErrors

class RequiredDetailedErrorCollection(TypedDict):
    pass

class OptionalDetailedErrorCollection(TypedDict, total=False):
    details: DetailedErrorCollectionDetails

    errorMessages: DetailedErrorCollectionErrorMessages

    errors: DetailedErrorCollectionErrors

class DetailedErrorCollection(RequiredDetailedErrorCollection, OptionalDetailedErrorCollection):
    pass
