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


class Workflow(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a workflow.
    """


    class MetaOapg:
        required = {
            "description",
            "id",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['PublishedWorkflowId']:
                return PublishedWorkflowId
            created = schemas.DateTimeSchema
            hasDraftWorkflow = schemas.BoolSchema
            isDefault = schemas.BoolSchema
        
            @staticmethod
            def operations() -> typing.Type['WorkflowOperations']:
                return WorkflowOperations
            
            
            class projects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProjectDetails']:
                        return ProjectDetails
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ProjectDetails'], typing.List['ProjectDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProjectDetails':
                    return super().__getitem__(i)
            
            
            class schemes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowSchemeIdName']:
                        return WorkflowSchemeIdName
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowSchemeIdName'], typing.List['WorkflowSchemeIdName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schemes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowSchemeIdName':
                    return super().__getitem__(i)
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowStatus']:
                        return WorkflowStatus
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowStatus'], typing.List['WorkflowStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowStatus':
                    return super().__getitem__(i)
            
            
            class transitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Transition']:
                        return Transition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Transition'], typing.List['Transition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transitions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Transition':
                    return super().__getitem__(i)
            updated = schemas.DateTimeSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "created": created,
                "hasDraftWorkflow": hasDraftWorkflow,
                "isDefault": isDefault,
                "operations": operations,
                "projects": projects,
                "schemes": schemes,
                "statuses": statuses,
                "transitions": transitions,
                "updated": updated,
            }
    
    description: MetaOapg.properties.description
    id: 'PublishedWorkflowId'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'PublishedWorkflowId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasDraftWorkflow"]) -> MetaOapg.properties.hasDraftWorkflow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operations"]) -> 'WorkflowOperations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projects"]) -> MetaOapg.properties.projects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemes"]) -> MetaOapg.properties.schemes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transitions"]) -> MetaOapg.properties.transitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "created", "hasDraftWorkflow", "isDefault", "operations", "projects", "schemes", "statuses", "transitions", "updated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'PublishedWorkflowId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasDraftWorkflow"]) -> typing.Union[MetaOapg.properties.hasDraftWorkflow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operations"]) -> typing.Union['WorkflowOperations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projects"]) -> typing.Union[MetaOapg.properties.projects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemes"]) -> typing.Union[MetaOapg.properties.schemes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> typing.Union[MetaOapg.properties.statuses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transitions"]) -> typing.Union[MetaOapg.properties.transitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "created", "hasDraftWorkflow", "isDefault", "operations", "projects", "schemes", "statuses", "transitions", "updated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: 'PublishedWorkflowId',
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        hasDraftWorkflow: typing.Union[MetaOapg.properties.hasDraftWorkflow, bool, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        operations: typing.Union['WorkflowOperations', schemas.Unset] = schemas.unset,
        projects: typing.Union[MetaOapg.properties.projects, list, tuple, schemas.Unset] = schemas.unset,
        schemes: typing.Union[MetaOapg.properties.schemes, list, tuple, schemas.Unset] = schemas.unset,
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, schemas.Unset] = schemas.unset,
        transitions: typing.Union[MetaOapg.properties.transitions, list, tuple, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Workflow':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            created=created,
            hasDraftWorkflow=hasDraftWorkflow,
            isDefault=isDefault,
            operations=operations,
            projects=projects,
            schemes=schemes,
            statuses=statuses,
            transitions=transitions,
            updated=updated,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.project_details import ProjectDetails
from atlassian_jira_python_sdk.model.published_workflow_id import PublishedWorkflowId
from atlassian_jira_python_sdk.model.transition import Transition
from atlassian_jira_python_sdk.model.workflow_operations import WorkflowOperations
from atlassian_jira_python_sdk.model.workflow_scheme_id_name import WorkflowSchemeIdName
from atlassian_jira_python_sdk.model.workflow_status import WorkflowStatus
