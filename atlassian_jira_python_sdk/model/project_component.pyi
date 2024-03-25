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


class ProjectComponent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a project component.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            ari = schemas.StrSchema
        
            @staticmethod
            def assignee() -> typing.Type['User']:
                return User
            
            
            class assigneeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PROJECT_DEFAULT(cls):
                    return cls("PROJECT_DEFAULT")
                
                @schemas.classproperty
                def COMPONENT_LEAD(cls):
                    return cls("COMPONENT_LEAD")
                
                @schemas.classproperty
                def PROJECT_LEAD(cls):
                    return cls("PROJECT_LEAD")
                
                @schemas.classproperty
                def UNASSIGNED(cls):
                    return cls("UNASSIGNED")
            id = schemas.StrSchema
            isAssigneeTypeValid = schemas.BoolSchema
        
            @staticmethod
            def lead() -> typing.Type['User']:
                return User
            
            
            class leadAccountId(
                schemas.StrSchema
            ):
                pass
            leadUserName = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['ProjectComponentMetadata']:
                return ProjectComponentMetadata
            name = schemas.StrSchema
            project = schemas.StrSchema
            projectId = schemas.Int64Schema
        
            @staticmethod
            def realAssignee() -> typing.Type['User']:
                return User
            
            
            class realAssigneeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PROJECT_DEFAULT(cls):
                    return cls("PROJECT_DEFAULT")
                
                @schemas.classproperty
                def COMPONENT_LEAD(cls):
                    return cls("COMPONENT_LEAD")
                
                @schemas.classproperty
                def PROJECT_LEAD(cls):
                    return cls("PROJECT_LEAD")
                
                @schemas.classproperty
                def UNASSIGNED(cls):
                    return cls("UNASSIGNED")
            _self = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "ari": ari,
                "assignee": assignee,
                "assigneeType": assigneeType,
                "id": id,
                "isAssigneeTypeValid": isAssigneeTypeValid,
                "lead": lead,
                "leadAccountId": leadAccountId,
                "leadUserName": leadUserName,
                "metadata": metadata,
                "name": name,
                "project": project,
                "projectId": projectId,
                "realAssignee": realAssignee,
                "realAssigneeType": realAssigneeType,
                "self": _self,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ari"]) -> MetaOapg.properties.ari: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assigneeType"]) -> MetaOapg.properties.assigneeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAssigneeTypeValid"]) -> MetaOapg.properties.isAssigneeTypeValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lead"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leadAccountId"]) -> MetaOapg.properties.leadAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leadUserName"]) -> MetaOapg.properties.leadUserName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'ProjectComponentMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> MetaOapg.properties.project: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realAssignee"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realAssigneeType"]) -> MetaOapg.properties.realAssigneeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "ari", "assignee", "assigneeType", "id", "isAssigneeTypeValid", "lead", "leadAccountId", "leadUserName", "metadata", "name", "project", "projectId", "realAssignee", "realAssigneeType", "self", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ari"]) -> typing.Union[MetaOapg.properties.ari, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assigneeType"]) -> typing.Union[MetaOapg.properties.assigneeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAssigneeTypeValid"]) -> typing.Union[MetaOapg.properties.isAssigneeTypeValid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lead"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leadAccountId"]) -> typing.Union[MetaOapg.properties.leadAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leadUserName"]) -> typing.Union[MetaOapg.properties.leadUserName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['ProjectComponentMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union[MetaOapg.properties.project, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> typing.Union[MetaOapg.properties.projectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realAssignee"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realAssigneeType"]) -> typing.Union[MetaOapg.properties.realAssigneeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "ari", "assignee", "assigneeType", "id", "isAssigneeTypeValid", "lead", "leadAccountId", "leadUserName", "metadata", "name", "project", "projectId", "realAssignee", "realAssigneeType", "self", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        ari: typing.Union[MetaOapg.properties.ari, str, schemas.Unset] = schemas.unset,
        assignee: typing.Union['User', schemas.Unset] = schemas.unset,
        assigneeType: typing.Union[MetaOapg.properties.assigneeType, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        isAssigneeTypeValid: typing.Union[MetaOapg.properties.isAssigneeTypeValid, bool, schemas.Unset] = schemas.unset,
        lead: typing.Union['User', schemas.Unset] = schemas.unset,
        leadAccountId: typing.Union[MetaOapg.properties.leadAccountId, str, schemas.Unset] = schemas.unset,
        leadUserName: typing.Union[MetaOapg.properties.leadUserName, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['ProjectComponentMetadata', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        project: typing.Union[MetaOapg.properties.project, str, schemas.Unset] = schemas.unset,
        projectId: typing.Union[MetaOapg.properties.projectId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        realAssignee: typing.Union['User', schemas.Unset] = schemas.unset,
        realAssigneeType: typing.Union[MetaOapg.properties.realAssigneeType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectComponent':
        return super().__new__(
            cls,
            *args,
            description=description,
            ari=ari,
            assignee=assignee,
            assigneeType=assigneeType,
            id=id,
            isAssigneeTypeValid=isAssigneeTypeValid,
            lead=lead,
            leadAccountId=leadAccountId,
            leadUserName=leadUserName,
            metadata=metadata,
            name=name,
            project=project,
            projectId=projectId,
            realAssignee=realAssignee,
            realAssigneeType=realAssigneeType,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.project_component_metadata import ProjectComponentMetadata
from atlassian_jira_python_sdk.model.user import User
