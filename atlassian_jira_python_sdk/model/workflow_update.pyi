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


class WorkflowUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of the workflows to update.
    """


    class MetaOapg:
        required = {
            "statuses",
            "id",
            "transitions",
            "version",
        }
        
        class properties:
        
            @staticmethod
            def version() -> typing.Type['DocumentVersion']:
                return DocumentVersion
            id = schemas.StrSchema
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatusLayoutUpdate']:
                        return StatusLayoutUpdate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatusLayoutUpdate'], typing.List['StatusLayoutUpdate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatusLayoutUpdate':
                    return super().__getitem__(i)
            
            
            class transitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransitionUpdateDTO']:
                        return TransitionUpdateDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TransitionUpdateDTO'], typing.List['TransitionUpdateDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transitions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransitionUpdateDTO':
                    return super().__getitem__(i)
            description = schemas.StrSchema
            
            
            class defaultStatusMappings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatusMigration']:
                        return StatusMigration
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatusMigration'], typing.List['StatusMigration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultStatusMappings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatusMigration':
                    return super().__getitem__(i)
        
            @staticmethod
            def startPointLayout() -> typing.Type['WorkflowLayout']:
                return WorkflowLayout
            
            
            class statusMappings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatusMappingDTO']:
                        return StatusMappingDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatusMappingDTO'], typing.List['StatusMappingDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statusMappings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatusMappingDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "version": version,
                "id": id,
                "statuses": statuses,
                "transitions": transitions,
                "description": description,
                "defaultStatusMappings": defaultStatusMappings,
                "startPointLayout": startPointLayout,
                "statusMappings": statusMappings,
            }
        additional_properties = schemas.AnyTypeSchema
    
    statuses: MetaOapg.properties.statuses
    id: MetaOapg.properties.id
    transitions: MetaOapg.properties.transitions
    version: 'DocumentVersion'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transitions"]) -> MetaOapg.properties.transitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> 'DocumentVersion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultStatusMappings"]) -> MetaOapg.properties.defaultStatusMappings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startPointLayout"]) -> 'WorkflowLayout': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusMappings"]) -> MetaOapg.properties.statusMappings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statuses"], typing_extensions.Literal["id"], typing_extensions.Literal["transitions"], typing_extensions.Literal["version"], typing_extensions.Literal["description"], typing_extensions.Literal["defaultStatusMappings"], typing_extensions.Literal["startPointLayout"], typing_extensions.Literal["statusMappings"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transitions"]) -> MetaOapg.properties.transitions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> 'DocumentVersion': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultStatusMappings"]) -> typing.Union[MetaOapg.properties.defaultStatusMappings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startPointLayout"]) -> typing.Union['WorkflowLayout', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusMappings"]) -> typing.Union[MetaOapg.properties.statusMappings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statuses"], typing_extensions.Literal["id"], typing_extensions.Literal["transitions"], typing_extensions.Literal["version"], typing_extensions.Literal["description"], typing_extensions.Literal["defaultStatusMappings"], typing_extensions.Literal["startPointLayout"], typing_extensions.Literal["statusMappings"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        transitions: typing.Union[MetaOapg.properties.transitions, list, tuple, ],
        version: 'DocumentVersion',
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        defaultStatusMappings: typing.Union[MetaOapg.properties.defaultStatusMappings, list, tuple, schemas.Unset] = schemas.unset,
        startPointLayout: typing.Union['WorkflowLayout', schemas.Unset] = schemas.unset,
        statusMappings: typing.Union[MetaOapg.properties.statusMappings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WorkflowUpdate':
        return super().__new__(
            cls,
            *args,
            statuses=statuses,
            id=id,
            transitions=transitions,
            version=version,
            description=description,
            defaultStatusMappings=defaultStatusMappings,
            startPointLayout=startPointLayout,
            statusMappings=statusMappings,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.document_version import DocumentVersion
from atlassian_jira_python_sdk.model.status_layout_update import StatusLayoutUpdate
from atlassian_jira_python_sdk.model.status_mapping_dto import StatusMappingDTO
from atlassian_jira_python_sdk.model.status_migration import StatusMigration
from atlassian_jira_python_sdk.model.transition_update_dto import TransitionUpdateDTO
from atlassian_jira_python_sdk.model.workflow_layout import WorkflowLayout
