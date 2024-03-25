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
from atlassian_jira_python_sdk.pydantic.workflow_metadata_and_issue_type_rest_model import WorkflowMetadataAndIssueTypeRestModel
from atlassian_jira_python_sdk.pydantic.workflow_metadata_rest_model import WorkflowMetadataRestModel
from atlassian_jira_python_sdk.pydantic.workflow_scheme_read_response_project_ids_using_scheme import WorkflowSchemeReadResponseProjectIdsUsingScheme
from atlassian_jira_python_sdk.pydantic.workflow_scope import WorkflowScope

class WorkflowSchemeReadResponse(BaseModel):
    version: DocumentVersion = Field(alias='version')

    # The ID of the workflow scheme.
    id: str = Field(alias='id')

    # The name of the workflow scheme.
    name: str = Field(alias='name')

    project_ids_using_scheme: WorkflowSchemeReadResponseProjectIdsUsingScheme = Field(alias='projectIdsUsingScheme')

    scope: WorkflowScope = Field(alias='scope')

    # Mappings from workflows to issue types.
    workflows_for_issue_types: typing.List[WorkflowMetadataAndIssueTypeRestModel] = Field(alias='workflowsForIssueTypes')

    # The description of the workflow scheme.
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    default_workflow: typing.Optional[WorkflowMetadataRestModel] = Field(None, alias='defaultWorkflow')

    # Indicates if there's an [asynchronous task](https://dac-static.atlassian.com) for this workflow scheme.
    task_id: typing.Optional[typing.Optional[str]] = Field(None, alias='taskId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
