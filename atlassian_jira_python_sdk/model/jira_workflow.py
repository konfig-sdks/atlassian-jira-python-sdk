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


class JiraWorkflow(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a workflow.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def version() -> typing.Type['DocumentVersion']:
                return DocumentVersion
            id = schemas.StrSchema
            isEditable = schemas.BoolSchema
            name = schemas.StrSchema
        
            @staticmethod
            def scope() -> typing.Type['WorkflowScope']:
                return WorkflowScope
        
            @staticmethod
            def startPointLayout() -> typing.Type['WorkflowLayout']:
                return WorkflowLayout
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowReferenceStatus']:
                        return WorkflowReferenceStatus
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowReferenceStatus'], typing.List['WorkflowReferenceStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowReferenceStatus':
                    return super().__getitem__(i)
            
            
            class taskId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taskId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class transitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowTransitions']:
                        return WorkflowTransitions
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowTransitions'], typing.List['WorkflowTransitions']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transitions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowTransitions':
                    return super().__getitem__(i)
            
            
            class usages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['ProjectIssueTypes']:
                        return ProjectIssueTypes
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ProjectIssueTypes'], typing.List['ProjectIssueTypes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'usages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProjectIssueTypes':
                    return super().__getitem__(i)
            __annotations__ = {
                "description": description,
                "version": version,
                "id": id,
                "isEditable": isEditable,
                "name": name,
                "scope": scope,
                "startPointLayout": startPointLayout,
                "statuses": statuses,
                "taskId": taskId,
                "transitions": transitions,
                "usages": usages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> 'DocumentVersion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEditable"]) -> MetaOapg.properties.isEditable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'WorkflowScope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startPointLayout"]) -> 'WorkflowLayout': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskId"]) -> MetaOapg.properties.taskId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transitions"]) -> MetaOapg.properties.transitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usages"]) -> MetaOapg.properties.usages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "version", "id", "isEditable", "name", "scope", "startPointLayout", "statuses", "taskId", "transitions", "usages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union['DocumentVersion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEditable"]) -> typing.Union[MetaOapg.properties.isEditable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union['WorkflowScope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startPointLayout"]) -> typing.Union['WorkflowLayout', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> typing.Union[MetaOapg.properties.statuses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskId"]) -> typing.Union[MetaOapg.properties.taskId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transitions"]) -> typing.Union[MetaOapg.properties.transitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usages"]) -> typing.Union[MetaOapg.properties.usages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "version", "id", "isEditable", "name", "scope", "startPointLayout", "statuses", "taskId", "transitions", "usages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        version: typing.Union['DocumentVersion', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        isEditable: typing.Union[MetaOapg.properties.isEditable, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        scope: typing.Union['WorkflowScope', schemas.Unset] = schemas.unset,
        startPointLayout: typing.Union['WorkflowLayout', schemas.Unset] = schemas.unset,
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, schemas.Unset] = schemas.unset,
        taskId: typing.Union[MetaOapg.properties.taskId, None, str, schemas.Unset] = schemas.unset,
        transitions: typing.Union[MetaOapg.properties.transitions, list, tuple, schemas.Unset] = schemas.unset,
        usages: typing.Union[MetaOapg.properties.usages, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JiraWorkflow':
        return super().__new__(
            cls,
            *args,
            description=description,
            version=version,
            id=id,
            isEditable=isEditable,
            name=name,
            scope=scope,
            startPointLayout=startPointLayout,
            statuses=statuses,
            taskId=taskId,
            transitions=transitions,
            usages=usages,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.document_version import DocumentVersion
from atlassian_jira_python_sdk.model.project_issue_types import ProjectIssueTypes
from atlassian_jira_python_sdk.model.workflow_layout import WorkflowLayout
from atlassian_jira_python_sdk.model.workflow_reference_status import WorkflowReferenceStatus
from atlassian_jira_python_sdk.model.workflow_scope import WorkflowScope
from atlassian_jira_python_sdk.model.workflow_transitions import WorkflowTransitions