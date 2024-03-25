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


class User(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A user with details as permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case, `displayName` provides an indication and other parameters have default values or are blank (for example, email is blank).
 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values.
    """


    class MetaOapg:
        
        class properties:
            
            
            class accountId(
                schemas.StrSchema
            ):
                pass
            
            
            class accountType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ATLASSIAN(cls):
                    return cls("atlassian")
                
                @schemas.classproperty
                def APP(cls):
                    return cls("app")
                
                @schemas.classproperty
                def CUSTOMER(cls):
                    return cls("customer")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
            active = schemas.BoolSchema
        
            @staticmethod
            def applicationRoles() -> typing.Type['SimpleListWrapperApplicationRole']:
                return SimpleListWrapperApplicationRole
        
            @staticmethod
            def avatarUrls() -> typing.Type['AvatarUrlsBean']:
                return AvatarUrlsBean
            displayName = schemas.StrSchema
            emailAddress = schemas.StrSchema
            expand = schemas.StrSchema
        
            @staticmethod
            def groups() -> typing.Type['SimpleListWrapperGroupName']:
                return SimpleListWrapperGroupName
            key = schemas.StrSchema
            locale = schemas.StrSchema
            name = schemas.StrSchema
            _self = schemas.StrSchema
            timeZone = schemas.StrSchema
            __annotations__ = {
                "accountId": accountId,
                "accountType": accountType,
                "active": active,
                "applicationRoles": applicationRoles,
                "avatarUrls": avatarUrls,
                "displayName": displayName,
                "emailAddress": emailAddress,
                "expand": expand,
                "groups": groups,
                "key": key,
                "locale": locale,
                "name": name,
                "self": _self,
                "timeZone": timeZone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationRoles"]) -> 'SimpleListWrapperApplicationRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatarUrls"]) -> 'AvatarUrlsBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expand"]) -> MetaOapg.properties.expand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> 'SimpleListWrapperGroupName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeZone"]) -> MetaOapg.properties.timeZone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "accountType", "active", "applicationRoles", "avatarUrls", "displayName", "emailAddress", "expand", "groups", "key", "locale", "name", "self", "timeZone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> typing.Union[MetaOapg.properties.accountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationRoles"]) -> typing.Union['SimpleListWrapperApplicationRole', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatarUrls"]) -> typing.Union['AvatarUrlsBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> typing.Union[MetaOapg.properties.emailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expand"]) -> typing.Union[MetaOapg.properties.expand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union['SimpleListWrapperGroupName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union[MetaOapg.properties.locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeZone"]) -> typing.Union[MetaOapg.properties.timeZone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "accountType", "active", "applicationRoles", "avatarUrls", "displayName", "emailAddress", "expand", "groups", "key", "locale", "name", "self", "timeZone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
        accountType: typing.Union[MetaOapg.properties.accountType, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        applicationRoles: typing.Union['SimpleListWrapperApplicationRole', schemas.Unset] = schemas.unset,
        avatarUrls: typing.Union['AvatarUrlsBean', schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, str, schemas.Unset] = schemas.unset,
        expand: typing.Union[MetaOapg.properties.expand, str, schemas.Unset] = schemas.unset,
        groups: typing.Union['SimpleListWrapperGroupName', schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        locale: typing.Union[MetaOapg.properties.locale, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        timeZone: typing.Union[MetaOapg.properties.timeZone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            accountId=accountId,
            accountType=accountType,
            active=active,
            applicationRoles=applicationRoles,
            avatarUrls=avatarUrls,
            displayName=displayName,
            emailAddress=emailAddress,
            expand=expand,
            groups=groups,
            key=key,
            locale=locale,
            name=name,
            timeZone=timeZone,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.avatar_urls_bean import AvatarUrlsBean
from atlassian_jira_python_sdk.model.simple_list_wrapper_application_role import SimpleListWrapperApplicationRole
from atlassian_jira_python_sdk.model.simple_list_wrapper_group_name import SimpleListWrapperGroupName