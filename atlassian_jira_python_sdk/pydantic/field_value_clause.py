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

from atlassian_jira_python_sdk.pydantic.jql_query_clause_operand import JqlQueryClauseOperand
from atlassian_jira_python_sdk.pydantic.jql_query_field import JqlQueryField

class FieldValueClause(BaseModel):
    field: JqlQueryField = Field(alias='field')

    operand: JqlQueryClauseOperand = Field(alias='operand')

    # The operator between the field and operand.
    operator: Literal["=", "!=", ">", "<", ">=", "<=", "in", "not in", "~", "~=", "is", "is not"] = Field(alias='operator')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
