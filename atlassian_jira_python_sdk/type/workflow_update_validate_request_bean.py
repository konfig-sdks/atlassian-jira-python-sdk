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

from atlassian_jira_python_sdk.type.validation_options_for_update import ValidationOptionsForUpdate
from atlassian_jira_python_sdk.type.workflow_update_request import WorkflowUpdateRequest

class RequiredWorkflowUpdateValidateRequestBean(TypedDict):
    payload: WorkflowUpdateRequest

class OptionalWorkflowUpdateValidateRequestBean(TypedDict, total=False):
    validationOptions: ValidationOptionsForUpdate

class WorkflowUpdateValidateRequestBean(RequiredWorkflowUpdateValidateRequestBean, OptionalWorkflowUpdateValidateRequestBean):
    pass