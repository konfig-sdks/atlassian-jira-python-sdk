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

from atlassian_jira_python_sdk.pydantic.create_workflow_status_details import CreateWorkflowStatusDetails
from atlassian_jira_python_sdk.pydantic.create_workflow_transition_details import CreateWorkflowTransitionDetails

class CreateWorkflowDetails(BaseModel):
    # The name of the workflow. The name must be unique. The maximum length is 255 characters. Characters can be separated by a whitespace but the name cannot start or end with a whitespace.
    name: str = Field(alias='name')

    # The statuses of the workflow. Any status that does not include a transition is added to the workflow without a transition.
    statuses: typing.List[CreateWorkflowStatusDetails] = Field(alias='statuses')

    # The transitions of the workflow. For the request to be valid, these transitions must:   *  include one *initial* transition.  *  not use the same name for a *global* and *directed* transition.  *  have a unique name for each *global* transition.  *  have a unique 'to' status for each *global* transition.  *  have unique names for each transition from a status.  *  not have a 'from' status on *initial* and *global* transitions.  *  have a 'from' status on *directed* transitions.  All the transition statuses must be included in `statuses`.
    transitions: typing.List[CreateWorkflowTransitionDetails] = Field(alias='transitions')

    # The description of the workflow. The maximum length is 1000 characters.
    description: typing.Optional[str] = Field(None, alias='description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
