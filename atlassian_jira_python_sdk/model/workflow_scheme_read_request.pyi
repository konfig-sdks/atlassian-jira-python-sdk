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


class WorkflowSchemeReadRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The workflow scheme read request body.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def projectIds() -> typing.Type['WorkflowSchemeReadRequestProjectIds']:
                return WorkflowSchemeReadRequestProjectIds
        
            @staticmethod
            def workflowSchemeIds() -> typing.Type['WorkflowSchemeReadRequestWorkflowSchemeIds']:
                return WorkflowSchemeReadRequestWorkflowSchemeIds
            __annotations__ = {
                "projectIds": projectIds,
                "workflowSchemeIds": workflowSchemeIds,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectIds"]) -> 'WorkflowSchemeReadRequestProjectIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowSchemeIds"]) -> 'WorkflowSchemeReadRequestWorkflowSchemeIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["projectIds", "workflowSchemeIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectIds"]) -> typing.Union['WorkflowSchemeReadRequestProjectIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowSchemeIds"]) -> typing.Union['WorkflowSchemeReadRequestWorkflowSchemeIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["projectIds", "workflowSchemeIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        projectIds: typing.Union['WorkflowSchemeReadRequestProjectIds', schemas.Unset] = schemas.unset,
        workflowSchemeIds: typing.Union['WorkflowSchemeReadRequestWorkflowSchemeIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowSchemeReadRequest':
        return super().__new__(
            cls,
            *args,
            projectIds=projectIds,
            workflowSchemeIds=workflowSchemeIds,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_scheme_read_request_project_ids import WorkflowSchemeReadRequestProjectIds
from atlassian_jira_python_sdk.model.workflow_scheme_read_request_workflow_scheme_ids import WorkflowSchemeReadRequestWorkflowSchemeIds
