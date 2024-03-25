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


class AnnouncementBannerConfiguration(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Announcement banner configuration.
    """


    class MetaOapg:
        
        class properties:
            hashId = schemas.StrSchema
            isDismissible = schemas.BoolSchema
            isEnabled = schemas.BoolSchema
            message = schemas.StrSchema
            
            
            class visibility(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
            __annotations__ = {
                "hashId": hashId,
                "isDismissible": isDismissible,
                "isEnabled": isEnabled,
                "message": message,
                "visibility": visibility,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDismissible"]) -> MetaOapg.properties.isDismissible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEnabled"]) -> MetaOapg.properties.isEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hashId", "isDismissible", "isEnabled", "message", "visibility", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDismissible"]) -> typing.Union[MetaOapg.properties.isDismissible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEnabled"]) -> typing.Union[MetaOapg.properties.isEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hashId", "isDismissible", "isEnabled", "message", "visibility", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hashId: typing.Union[MetaOapg.properties.hashId, str, schemas.Unset] = schemas.unset,
        isDismissible: typing.Union[MetaOapg.properties.isDismissible, bool, schemas.Unset] = schemas.unset,
        isEnabled: typing.Union[MetaOapg.properties.isEnabled, bool, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnnouncementBannerConfiguration':
        return super().__new__(
            cls,
            *args,
            hashId=hashId,
            isDismissible=isDismissible,
            isEnabled=isEnabled,
            message=message,
            visibility=visibility,
            _configuration=_configuration,
            **kwargs,
        )