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


class UpdatePriorityDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an issue priority.
    """


    class MetaOapg:
        
        class properties:
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class iconUrl(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    enum_value_to_name = {
                        "/images/icons/priorities/blocker.png": "BLOCKER_PNG",
                        "/images/icons/priorities/critical.png": "CRITICAL_PNG",
                        "/images/icons/priorities/high.png": "HIGH_PNG",
                        "/images/icons/priorities/highest.png": "HIGHEST_PNG",
                        "/images/icons/priorities/low.png": "LOW_PNG",
                        "/images/icons/priorities/lowest.png": "LOWEST_PNG",
                        "/images/icons/priorities/major.png": "MAJOR_PNG",
                        "/images/icons/priorities/medium.png": "MEDIUM_PNG",
                        "/images/icons/priorities/minor.png": "MINOR_PNG",
                        "/images/icons/priorities/trivial.png": "TRIVIAL_PNG",
                    }
                
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
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 60
            statusColor = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "iconUrl": iconUrl,
                "name": name,
                "statusColor": statusColor,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconUrl"]) -> MetaOapg.properties.iconUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusColor"]) -> MetaOapg.properties.statusColor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["iconUrl"], typing_extensions.Literal["name"], typing_extensions.Literal["statusColor"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconUrl"]) -> typing.Union[MetaOapg.properties.iconUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusColor"]) -> typing.Union[MetaOapg.properties.statusColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["iconUrl"], typing_extensions.Literal["name"], typing_extensions.Literal["statusColor"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        iconUrl: typing.Union[MetaOapg.properties.iconUrl, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        statusColor: typing.Union[MetaOapg.properties.statusColor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'UpdatePriorityDetails':
        return super().__new__(
            cls,
            *args,
            description=description,
            iconUrl=iconUrl,
            name=name,
            statusColor=statusColor,
            _configuration=_configuration,
            **kwargs,
        )
