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


class JqlQueryFieldEntityProperty(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an entity property.
    """


    class MetaOapg:
        required = {
            "path",
            "entity",
            "key",
        }
        
        class properties:
            entity = schemas.StrSchema
            key = schemas.StrSchema
            path = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "number": "NUMBER",
                        "string": "STRING",
                        "text": "TEXT",
                        "date": "DATE",
                        "user": "USER",
                    }
                
                @schemas.classproperty
                def NUMBER(cls):
                    return cls("number")
                
                @schemas.classproperty
                def STRING(cls):
                    return cls("string")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("text")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("date")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
            __annotations__ = {
                "entity": entity,
                "key": key,
                "path": path,
                "type": type,
            }
    
    path: MetaOapg.properties.path
    entity: MetaOapg.properties.entity
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity"]) -> MetaOapg.properties.entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["entity", "key", "path", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity"]) -> MetaOapg.properties.entity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["entity", "key", "path", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        path: typing.Union[MetaOapg.properties.path, str, ],
        entity: typing.Union[MetaOapg.properties.entity, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JqlQueryFieldEntityProperty':
        return super().__new__(
            cls,
            *args,
            path=path,
            entity=entity,
            key=key,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
