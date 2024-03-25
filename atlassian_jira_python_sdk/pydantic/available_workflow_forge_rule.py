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


class AvailableWorkflowForgeRule(BaseModel):
    # The rule description.
    description: typing.Optional[str] = Field(None, alias='description')

    # The unique ARI of the forge rule type.
    id: typing.Optional[str] = Field(None, alias='id')

    # The rule name.
    name: typing.Optional[str] = Field(None, alias='name')

    # The rule key.
    rule_key: typing.Optional[str] = Field(None, alias='ruleKey')

    # The rule type.
    rule_type: typing.Optional[Literal["Condition", "Validator", "Function", "Screen"]] = Field(None, alias='ruleType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )