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

from atlassian_jira_python_sdk.type.function_operand_arguments import FunctionOperandArguments

class RequiredFunctionOperand(TypedDict):
    arguments: FunctionOperandArguments

    # The name of the function.
    function: str

class OptionalFunctionOperand(TypedDict, total=False):
    # Encoded operand, which can be used directly in a JQL query.
    encodedOperand: str

class FunctionOperand(RequiredFunctionOperand, OptionalFunctionOperand):
    pass