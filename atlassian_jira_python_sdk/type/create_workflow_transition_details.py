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

from atlassian_jira_python_sdk.type.create_workflow_transition_details_from import CreateWorkflowTransitionDetailsFrom
from atlassian_jira_python_sdk.type.create_workflow_transition_details_properties import CreateWorkflowTransitionDetailsProperties
from atlassian_jira_python_sdk.type.create_workflow_transition_rules_details import CreateWorkflowTransitionRulesDetails
from atlassian_jira_python_sdk.type.create_workflow_transition_screen_details import CreateWorkflowTransitionScreenDetails

RequiredCreateWorkflowTransitionDetails = TypedDict("RequiredCreateWorkflowTransitionDetails", {
    # The name of the transition. The maximum length is 60 characters.
    "name": str,

    # The status the transition goes to.
    "to": str,

    # The type of the transition.
    "type": str,
    })

OptionalCreateWorkflowTransitionDetails = TypedDict("OptionalCreateWorkflowTransitionDetails", {
    # The description of the transition. The maximum length is 1000 characters.
    "description": str,

    "from": CreateWorkflowTransitionDetailsFrom,

    "properties": CreateWorkflowTransitionDetailsProperties,

    # The rules of the transition.
    "rules": CreateWorkflowTransitionRulesDetails,

    # The screen of the transition.
    "screen": CreateWorkflowTransitionScreenDetails,
    }, total=False)

class CreateWorkflowTransitionDetails(RequiredCreateWorkflowTransitionDetails, OptionalCreateWorkflowTransitionDetails):
    pass
