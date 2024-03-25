# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlassian_jira_python_sdk import schemas  # noqa: F401


class WorkflowMetadataAndIssueTypeRestModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The workflow metadata and issue type IDs which use this workflow.
    """


    class MetaOapg:
        required = {
            "workflow",
            "issueTypeIds",
        }
        
        class properties:
        
            @staticmethod
            def issueTypeIds() -> typing.Type['WorkflowMetadataAndIssueTypeRestModelIssueTypeIds']:
                return WorkflowMetadataAndIssueTypeRestModelIssueTypeIds
        
            @staticmethod
            def workflow() -> typing.Type['WorkflowMetadataRestModel']:
                return WorkflowMetadataRestModel
            __annotations__ = {
                "issueTypeIds": issueTypeIds,
                "workflow": workflow,
            }
    
    workflow: 'WorkflowMetadataRestModel'
    issueTypeIds: 'WorkflowMetadataAndIssueTypeRestModelIssueTypeIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueTypeIds"]) -> 'WorkflowMetadataAndIssueTypeRestModelIssueTypeIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflow"]) -> 'WorkflowMetadataRestModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["issueTypeIds", "workflow", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueTypeIds"]) -> 'WorkflowMetadataAndIssueTypeRestModelIssueTypeIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflow"]) -> 'WorkflowMetadataRestModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["issueTypeIds", "workflow", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workflow: 'WorkflowMetadataRestModel',
        issueTypeIds: 'WorkflowMetadataAndIssueTypeRestModelIssueTypeIds',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowMetadataAndIssueTypeRestModel':
        return super().__new__(
            cls,
            *args,
            workflow=workflow,
            issueTypeIds=issueTypeIds,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_metadata_and_issue_type_rest_model_issue_type_ids import WorkflowMetadataAndIssueTypeRestModelIssueTypeIds
from atlassian_jira_python_sdk.model.workflow_metadata_rest_model import WorkflowMetadataRestModel
