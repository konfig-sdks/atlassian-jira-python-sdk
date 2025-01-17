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

from atlassian_jira_python_sdk.pydantic.user import User
from atlassian_jira_python_sdk.pydantic.workflow_scheme_issue_type_mappings import WorkflowSchemeIssueTypeMappings
from atlassian_jira_python_sdk.pydantic.workflow_scheme_issue_types import WorkflowSchemeIssueTypes
from atlassian_jira_python_sdk.pydantic.workflow_scheme_original_issue_type_mappings import WorkflowSchemeOriginalIssueTypeMappings

class WorkflowScheme(BaseModel):
    # The description of the workflow scheme.
    description: typing.Optional[str] = Field(None, alias='description')

    # The name of the default workflow for the workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a workflow scheme, it is set to *Jira Workflow (jira)*.
    default_workflow: typing.Optional[str] = Field(None, alias='defaultWorkflow')

    # Whether the workflow scheme is a draft or not.
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # The ID of the workflow scheme.
    id: typing.Optional[int] = Field(None, alias='id')

    issue_type_mappings: typing.Optional[WorkflowSchemeIssueTypeMappings] = Field(None, alias='issueTypeMappings')

    issue_types: typing.Optional[WorkflowSchemeIssueTypes] = Field(None, alias='issueTypes')

    # The date-time that the draft workflow scheme was last modified. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
    last_modified: typing.Optional[str] = Field(None, alias='lastModified')

    # The user that last modified the draft workflow scheme. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
    last_modified_user: typing.Optional[User] = Field(None, alias='lastModifiedUser')

    # The name of the workflow scheme. The name must be unique. The maximum length is 255 characters. Required when creating a workflow scheme.
    name: typing.Optional[str] = Field(None, alias='name')

    # For draft workflow schemes, this property is the name of the default workflow for the original workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira.
    original_default_workflow: typing.Optional[str] = Field(None, alias='originalDefaultWorkflow')

    original_issue_type_mappings: typing.Optional[WorkflowSchemeOriginalIssueTypeMappings] = Field(None, alias='originalIssueTypeMappings')

    self_: typing.Optional[str] = Field(None, alias='self')

    # Whether to create or update a draft workflow scheme when updating an active workflow scheme. An active workflow scheme is a workflow scheme that is used by at least one project. The following examples show how this property works:   *  Update an active workflow scheme with `updateDraftIfNeeded` set to `true`: If a draft workflow scheme exists, it is updated. Otherwise, a draft workflow scheme is created.  *  Update an active workflow scheme with `updateDraftIfNeeded` set to `false`: An error is returned, as active workflow schemes cannot be updated.  *  Update an inactive workflow scheme with `updateDraftIfNeeded` set to `true`: The workflow scheme is updated, as inactive workflow schemes do not require drafts to update.  Defaults to `false`.
    update_draft_if_needed: typing.Optional[bool] = Field(None, alias='updateDraftIfNeeded')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
