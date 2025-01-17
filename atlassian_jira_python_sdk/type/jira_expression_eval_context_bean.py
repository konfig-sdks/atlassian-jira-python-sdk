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

from atlassian_jira_python_sdk.type.custom_context_variable import CustomContextVariable
from atlassian_jira_python_sdk.type.id_or_key_bean import IdOrKeyBean
from atlassian_jira_python_sdk.type.jexp_issues import JexpIssues

class RequiredJiraExpressionEvalContextBean(TypedDict):
    pass

class OptionalJiraExpressionEvalContextBean(TypedDict, total=False):
    # The ID of the board that is available under the `board` variable when evaluating the expression.
    board: int

    # Custom context variables and their types. These variable types are available for use in a custom context:   *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.  *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.  *  `json`: A JSON object containing custom content.  *  `list`: A JSON list of `user`, `issue`, or `json` variable types.
    custom: typing.List[CustomContextVariable]

    # The ID of the customer request that is available under the `customerRequest` variable when evaluating the expression. This is the same as the ID of the underlying Jira issue, but the customer request context variable will have a different type.
    customerRequest: int

    # The issue that is available under the `issue` variable when evaluating the expression.
    issue: IdOrKeyBean

    # The collection of issues that is available under the `issues` variable when evaluating the expression.
    issues: JexpIssues

    # The project that is available under the `project` variable when evaluating the expression.
    project: IdOrKeyBean

    # The ID of the service desk that is available under the `serviceDesk` variable when evaluating the expression.
    serviceDesk: int

    # The ID of the sprint that is available under the `sprint` variable when evaluating the expression.
    sprint: int

class JiraExpressionEvalContextBean(RequiredJiraExpressionEvalContextBean, OptionalJiraExpressionEvalContextBean):
    pass
