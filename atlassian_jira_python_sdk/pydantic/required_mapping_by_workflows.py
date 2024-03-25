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

from atlassian_jira_python_sdk.pydantic.required_mapping_by_workflows_status_ids import RequiredMappingByWorkflowsStatusIds

class RequiredMappingByWorkflows(BaseModel):
    # The ID of the source workflow.
    source_workflow_id: typing.Optional[str] = Field(None, alias='sourceWorkflowId')

    status_ids: typing.Optional[RequiredMappingByWorkflowsStatusIds] = Field(None, alias='statusIds')

    # The ID of the target workflow.
    target_workflow_id: typing.Optional[str] = Field(None, alias='targetWorkflowId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )