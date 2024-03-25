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

from atlassian_jira_python_sdk.pydantic.issues_meta_bean import IssuesMetaBean
from atlassian_jira_python_sdk.pydantic.jira_expressions_complexity_bean import JiraExpressionsComplexityBean

class JiraExpressionEvaluationMetaDataBean(BaseModel):
    # Contains information about the expression complexity. For example, the number of steps it took to evaluate the expression.
    complexity: typing.Optional[JiraExpressionsComplexityBean] = Field(None, alias='complexity')

    # Contains information about the `issues` variable in the context. For example, is the issues were loaded with JQL, information about the page will be included here.
    issues: typing.Optional[IssuesMetaBean] = Field(None, alias='issues')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
