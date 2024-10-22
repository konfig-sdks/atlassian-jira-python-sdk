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

from atlassian_jira_python_sdk.pydantic.available_workflow_system_rule_incompatible_rule_keys import AvailableWorkflowSystemRuleIncompatibleRuleKeys

class AvailableWorkflowSystemRule(BaseModel):
    # The rule description.
    description: str = Field(alias='description')

    incompatible_rule_keys: AvailableWorkflowSystemRuleIncompatibleRuleKeys = Field(alias='incompatibleRuleKeys')

    # Whether the rule can be added added to an initial transition.
    is_available_for_initial_transition: bool = Field(alias='isAvailableForInitialTransition')

    # Whether the rule is visible.
    is_visible: bool = Field(alias='isVisible')

    # The rule name.
    name: str = Field(alias='name')

    # The rule key.
    rule_key: str = Field(alias='ruleKey')

    # The rule type.
    rule_type: Literal["Condition", "Validator", "Function", "Screen"] = Field(alias='ruleType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
