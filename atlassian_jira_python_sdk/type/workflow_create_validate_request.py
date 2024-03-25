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

from atlassian_jira_python_sdk.type.validation_options_for_create import ValidationOptionsForCreate
from atlassian_jira_python_sdk.type.workflow_create_request import WorkflowCreateRequest

class RequiredWorkflowCreateValidateRequest(TypedDict):
    payload: WorkflowCreateRequest

class OptionalWorkflowCreateValidateRequest(TypedDict, total=False):
    validationOptions: ValidationOptionsForCreate

class WorkflowCreateValidateRequest(RequiredWorkflowCreateValidateRequest, OptionalWorkflowCreateValidateRequest):
    pass