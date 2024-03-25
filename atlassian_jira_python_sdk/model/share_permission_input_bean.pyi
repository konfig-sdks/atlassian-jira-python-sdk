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


class SharePermissionInputBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
                
                @schemas.classproperty
                def PROJECT(cls):
                    return cls("project")
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("group")
                
                @schemas.classproperty
                def PROJECT_ROLE(cls):
                    return cls("projectRole")
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("global")
                
                @schemas.classproperty
                def AUTHENTICATED(cls):
                    return cls("authenticated")
            accountId = schemas.StrSchema
            groupId = schemas.StrSchema
            groupname = schemas.StrSchema
            projectId = schemas.StrSchema
            projectRoleId = schemas.StrSchema
            rights = schemas.Int32Schema
            __annotations__ = {
                "type": type,
                "accountId": accountId,
                "groupId": groupId,
                "groupname": groupname,
                "projectId": projectId,
                "projectRoleId": projectRoleId,
                "rights": rights,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupname"]) -> MetaOapg.properties.groupname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectRoleId"]) -> MetaOapg.properties.projectRoleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rights"]) -> MetaOapg.properties.rights: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "accountId", "groupId", "groupname", "projectId", "projectRoleId", "rights", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupname"]) -> typing.Union[MetaOapg.properties.groupname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> typing.Union[MetaOapg.properties.projectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectRoleId"]) -> typing.Union[MetaOapg.properties.projectRoleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rights"]) -> typing.Union[MetaOapg.properties.rights, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "accountId", "groupId", "groupname", "projectId", "projectRoleId", "rights", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        groupname: typing.Union[MetaOapg.properties.groupname, str, schemas.Unset] = schemas.unset,
        projectId: typing.Union[MetaOapg.properties.projectId, str, schemas.Unset] = schemas.unset,
        projectRoleId: typing.Union[MetaOapg.properties.projectRoleId, str, schemas.Unset] = schemas.unset,
        rights: typing.Union[MetaOapg.properties.rights, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SharePermissionInputBean':
        return super().__new__(
            cls,
            *args,
            type=type,
            accountId=accountId,
            groupId=groupId,
            groupname=groupname,
            projectId=projectId,
            projectRoleId=projectRoleId,
            rights=rights,
            _configuration=_configuration,
            **kwargs,
        )
