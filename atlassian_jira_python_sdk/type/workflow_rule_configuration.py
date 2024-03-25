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

from atlassian_jira_python_sdk.type.workflow_rule_configuration_parameters import WorkflowRuleConfigurationParameters

class RequiredWorkflowRuleConfiguration(TypedDict):
    # The rule key of the rule.
    ruleKey: str

class OptionalWorkflowRuleConfiguration(TypedDict, total=False):
    parameters: WorkflowRuleConfigurationParameters

    # The ID of the rule.
    id: typing.Optional[str]

class WorkflowRuleConfiguration(RequiredWorkflowRuleConfiguration, OptionalWorkflowRuleConfiguration):
    pass
