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

from atlassian_jira_python_sdk.type.scope import Scope

class RequiredDeprecatedWorkflow(TypedDict):
    pass

class OptionalDeprecatedWorkflow(TypedDict, total=False):
    # The description of the workflow.
    description: str

    default: bool

    # The datetime the workflow was last modified.
    lastModifiedDate: str

    # This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    lastModifiedUser: str

    # The account ID of the user that last modified the workflow.
    lastModifiedUserAccountId: str

    # The name of the workflow.
    name: str

    # The scope where this workflow applies
    scope: Scope

    # The number of steps included in the workflow.
    steps: int

class DeprecatedWorkflow(RequiredDeprecatedWorkflow, OptionalDeprecatedWorkflow):
    pass
