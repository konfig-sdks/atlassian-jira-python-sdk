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

from atlassian_jira_python_sdk.type.user import User
from atlassian_jira_python_sdk.type.workflow_scheme_issue_type_mappings import WorkflowSchemeIssueTypeMappings
from atlassian_jira_python_sdk.type.workflow_scheme_issue_types import WorkflowSchemeIssueTypes
from atlassian_jira_python_sdk.type.workflow_scheme_original_issue_type_mappings import WorkflowSchemeOriginalIssueTypeMappings

RequiredWorkflowScheme = TypedDict("RequiredWorkflowScheme", {
    })

OptionalWorkflowScheme = TypedDict("OptionalWorkflowScheme", {
    # The description of the workflow scheme.
    "description": str,

    # The name of the default workflow for the workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a workflow scheme, it is set to *Jira Workflow (jira)*.
    "defaultWorkflow": str,

    # Whether the workflow scheme is a draft or not.
    "draft": bool,

    # The ID of the workflow scheme.
    "id": int,

    "issueTypeMappings": WorkflowSchemeIssueTypeMappings,

    "issueTypes": WorkflowSchemeIssueTypes,

    # The date-time that the draft workflow scheme was last modified. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
    "lastModified": str,

    # The user that last modified the draft workflow scheme. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
    "lastModifiedUser": User,

    # The name of the workflow scheme. The name must be unique. The maximum length is 255 characters. Required when creating a workflow scheme.
    "name": str,

    # For draft workflow schemes, this property is the name of the default workflow for the original workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira.
    "originalDefaultWorkflow": str,

    "originalIssueTypeMappings": WorkflowSchemeOriginalIssueTypeMappings,

    "self": str,

    # Whether to create or update a draft workflow scheme when updating an active workflow scheme. An active workflow scheme is a workflow scheme that is used by at least one project. The following examples show how this property works:   *  Update an active workflow scheme with `updateDraftIfNeeded` set to `true`: If a draft workflow scheme exists, it is updated. Otherwise, a draft workflow scheme is created.  *  Update an active workflow scheme with `updateDraftIfNeeded` set to `false`: An error is returned, as active workflow schemes cannot be updated.  *  Update an inactive workflow scheme with `updateDraftIfNeeded` set to `true`: The workflow scheme is updated, as inactive workflow schemes do not require drafts to update.  Defaults to `false`.
    "updateDraftIfNeeded": bool,
    }, total=False)

class WorkflowScheme(RequiredWorkflowScheme, OptionalWorkflowScheme):
    pass
