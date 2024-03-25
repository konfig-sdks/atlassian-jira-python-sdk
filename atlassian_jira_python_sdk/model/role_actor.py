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


class RoleActor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a user assigned to a project role.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def actorGroup() -> typing.Type['ProjectRoleGroup']:
                return ProjectRoleGroup
        
            @staticmethod
            def actorUser() -> typing.Type['ProjectRoleUser']:
                return ProjectRoleUser
            avatarUrl = schemas.StrSchema
            displayName = schemas.StrSchema
            id = schemas.Int64Schema
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "atlassian-group-role-actor": "GROUPROLEACTOR",
                        "atlassian-user-role-actor": "USERROLEACTOR",
                    }
                
                @schemas.classproperty
                def GROUPROLEACTOR(cls):
                    return cls("atlassian-group-role-actor")
                
                @schemas.classproperty
                def USERROLEACTOR(cls):
                    return cls("atlassian-user-role-actor")
            __annotations__ = {
                "actorGroup": actorGroup,
                "actorUser": actorUser,
                "avatarUrl": avatarUrl,
                "displayName": displayName,
                "id": id,
                "name": name,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actorGroup"]) -> 'ProjectRoleGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actorUser"]) -> 'ProjectRoleUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatarUrl"]) -> MetaOapg.properties.avatarUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actorGroup", "actorUser", "avatarUrl", "displayName", "id", "name", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actorGroup"]) -> typing.Union['ProjectRoleGroup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actorUser"]) -> typing.Union['ProjectRoleUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatarUrl"]) -> typing.Union[MetaOapg.properties.avatarUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actorGroup", "actorUser", "avatarUrl", "displayName", "id", "name", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        actorGroup: typing.Union['ProjectRoleGroup', schemas.Unset] = schemas.unset,
        actorUser: typing.Union['ProjectRoleUser', schemas.Unset] = schemas.unset,
        avatarUrl: typing.Union[MetaOapg.properties.avatarUrl, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RoleActor':
        return super().__new__(
            cls,
            *args,
            actorGroup=actorGroup,
            actorUser=actorUser,
            avatarUrl=avatarUrl,
            displayName=displayName,
            id=id,
            name=name,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.project_role_group import ProjectRoleGroup
from atlassian_jira_python_sdk.model.project_role_user import ProjectRoleUser
