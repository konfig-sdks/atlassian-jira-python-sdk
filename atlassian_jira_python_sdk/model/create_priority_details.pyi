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


class CreatePriorityDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an issue priority.
    """


    class MetaOapg:
        required = {
            "statusColor",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            statusColor = schemas.StrSchema
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            
            
            class iconUrl(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BLOCKER_PNG(cls):
                    return cls("/images/icons/priorities/blocker.png")
                
                @schemas.classproperty
                def CRITICAL_PNG(cls):
                    return cls("/images/icons/priorities/critical.png")
                
                @schemas.classproperty
                def HIGH_PNG(cls):
                    return cls("/images/icons/priorities/high.png")
                
                @schemas.classproperty
                def HIGHEST_PNG(cls):
                    return cls("/images/icons/priorities/highest.png")
                
                @schemas.classproperty
                def LOW_PNG(cls):
                    return cls("/images/icons/priorities/low.png")
                
                @schemas.classproperty
                def LOWEST_PNG(cls):
                    return cls("/images/icons/priorities/lowest.png")
                
                @schemas.classproperty
                def MAJOR_PNG(cls):
                    return cls("/images/icons/priorities/major.png")
                
                @schemas.classproperty
                def MEDIUM_PNG(cls):
                    return cls("/images/icons/priorities/medium.png")
                
                @schemas.classproperty
                def MINOR_PNG(cls):
                    return cls("/images/icons/priorities/minor.png")
                
                @schemas.classproperty
                def TRIVIAL_PNG(cls):
                    return cls("/images/icons/priorities/trivial.png")
            __annotations__ = {
                "name": name,
                "statusColor": statusColor,
                "description": description,
                "iconUrl": iconUrl,
            }
        additional_properties = schemas.AnyTypeSchema
    
    statusColor: MetaOapg.properties.statusColor
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusColor"]) -> MetaOapg.properties.statusColor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconUrl"]) -> MetaOapg.properties.iconUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statusColor"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["iconUrl"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusColor"]) -> MetaOapg.properties.statusColor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconUrl"]) -> typing.Union[MetaOapg.properties.iconUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statusColor"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["iconUrl"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        statusColor: typing.Union[MetaOapg.properties.statusColor, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        iconUrl: typing.Union[MetaOapg.properties.iconUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreatePriorityDetails':
        return super().__new__(
            cls,
            *args,
            statusColor=statusColor,
            name=name,
            description=description,
            iconUrl=iconUrl,
            _configuration=_configuration,
            **kwargs,
        )
