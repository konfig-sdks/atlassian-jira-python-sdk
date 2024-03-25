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

from atlassian_jira_python_sdk.type.jira_expression_complexity import JiraExpressionComplexity
from atlassian_jira_python_sdk.type.jira_expression_validation_error import JiraExpressionValidationError

class RequiredJiraExpressionAnalysis(TypedDict):
    # The analysed expression.
    expression: str

    # Whether the expression is valid and the interpreter will evaluate it. Note that the expression may fail at runtime (for example, if it executes too many expensive operations).
    valid: bool

class OptionalJiraExpressionAnalysis(TypedDict, total=False):
    complexity: JiraExpressionComplexity

    # A list of validation errors. Not included if the expression is valid.
    errors: typing.List[JiraExpressionValidationError]

    # EXPERIMENTAL. The inferred type of the expression.
    type: str

class JiraExpressionAnalysis(RequiredJiraExpressionAnalysis, OptionalJiraExpressionAnalysis):
    pass
