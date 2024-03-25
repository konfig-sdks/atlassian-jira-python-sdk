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

from atlassian_jira_python_sdk.pydantic.jira_expression_complexity import JiraExpressionComplexity
from atlassian_jira_python_sdk.pydantic.jira_expression_validation_error import JiraExpressionValidationError

class JiraExpressionAnalysis(BaseModel):
    # The analysed expression.
    expression: str = Field(alias='expression')

    # Whether the expression is valid and the interpreter will evaluate it. Note that the expression may fail at runtime (for example, if it executes too many expensive operations).
    valid: bool = Field(alias='valid')

    complexity: typing.Optional[JiraExpressionComplexity] = Field(None, alias='complexity')

    # A list of validation errors. Not included if the expression is valid.
    errors: typing.Optional[typing.List[JiraExpressionValidationError]] = Field(None, alias='errors')

    # EXPERIMENTAL. The inferred type of the expression.
    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
