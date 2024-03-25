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

from atlassian_jira_python_sdk.type.workflow_id import WorkflowId
from atlassian_jira_python_sdk.type.workflow_transition_rules_update_error_details_rule_update_errors import WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
from atlassian_jira_python_sdk.type.workflow_transition_rules_update_error_details_update_errors import WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors

class RequiredWorkflowTransitionRulesUpdateErrorDetails(TypedDict):
    ruleUpdateErrors: WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors

    updateErrors: WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors

    workflowId: WorkflowId

class OptionalWorkflowTransitionRulesUpdateErrorDetails(TypedDict, total=False):
    pass

class WorkflowTransitionRulesUpdateErrorDetails(RequiredWorkflowTransitionRulesUpdateErrorDetails, OptionalWorkflowTransitionRulesUpdateErrorDetails):
    pass