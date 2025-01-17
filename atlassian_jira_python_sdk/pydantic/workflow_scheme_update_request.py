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

from atlassian_jira_python_sdk.pydantic.document_version import DocumentVersion
from atlassian_jira_python_sdk.pydantic.mappings_by_issue_type_override import MappingsByIssueTypeOverride
from atlassian_jira_python_sdk.pydantic.mappings_by_workflow import MappingsByWorkflow
from atlassian_jira_python_sdk.pydantic.workflow_scheme_association import WorkflowSchemeAssociation

class WorkflowSchemeUpdateRequest(BaseModel):
    # The new description for this workflow scheme.
    description: str = Field(alias='description')

    version: DocumentVersion = Field(alias='version')

    # The ID of this workflow scheme.
    id: str = Field(alias='id')

    # The new name for this workflow scheme.
    name: str = Field(alias='name')

    # The ID of the workflow for issue types without having a mapping defined in this workflow scheme. Only used in global-scoped workflow schemes. If the `defaultWorkflowId` isn't specified, this is set to *Jira Workflow (jira)*.
    default_workflow_id: typing.Optional[str] = Field(None, alias='defaultWorkflowId')

    # Overrides, for the selected issue types, any status mappings provided in `statusMappingsByWorkflows`. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.
    status_mappings_by_issue_type_override: typing.Optional[typing.List[MappingsByIssueTypeOverride]] = Field(None, alias='statusMappingsByIssueTypeOverride')

    # The status mappings by workflows. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.
    status_mappings_by_workflows: typing.Optional[typing.List[MappingsByWorkflow]] = Field(None, alias='statusMappingsByWorkflows')

    # Mappings from workflows to issue types.
    workflows_for_issue_types: typing.Optional[typing.List[WorkflowSchemeAssociation]] = Field(None, alias='workflowsForIssueTypes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
