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


class MappingsByWorkflow(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The status mappings by workflows. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.
    """


    class MetaOapg:
        required = {
            "newWorkflowId",
            "statusMappings",
            "oldWorkflowId",
        }
        
        class properties:
            newWorkflowId = schemas.StrSchema
            oldWorkflowId = schemas.StrSchema
            
            
            class statusMappings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowAssociationStatusMapping']:
                        return WorkflowAssociationStatusMapping
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowAssociationStatusMapping'], typing.List['WorkflowAssociationStatusMapping']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statusMappings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowAssociationStatusMapping':
                    return super().__getitem__(i)
            __annotations__ = {
                "newWorkflowId": newWorkflowId,
                "oldWorkflowId": oldWorkflowId,
                "statusMappings": statusMappings,
            }
    
    newWorkflowId: MetaOapg.properties.newWorkflowId
    statusMappings: MetaOapg.properties.statusMappings
    oldWorkflowId: MetaOapg.properties.oldWorkflowId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newWorkflowId"]) -> MetaOapg.properties.newWorkflowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oldWorkflowId"]) -> MetaOapg.properties.oldWorkflowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusMappings"]) -> MetaOapg.properties.statusMappings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["newWorkflowId", "oldWorkflowId", "statusMappings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newWorkflowId"]) -> MetaOapg.properties.newWorkflowId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oldWorkflowId"]) -> MetaOapg.properties.oldWorkflowId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusMappings"]) -> MetaOapg.properties.statusMappings: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["newWorkflowId", "oldWorkflowId", "statusMappings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        newWorkflowId: typing.Union[MetaOapg.properties.newWorkflowId, str, ],
        statusMappings: typing.Union[MetaOapg.properties.statusMappings, list, tuple, ],
        oldWorkflowId: typing.Union[MetaOapg.properties.oldWorkflowId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MappingsByWorkflow':
        return super().__new__(
            cls,
            *args,
            newWorkflowId=newWorkflowId,
            statusMappings=statusMappings,
            oldWorkflowId=oldWorkflowId,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_association_status_mapping import WorkflowAssociationStatusMapping