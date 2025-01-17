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


class DashboardGadget(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a gadget.
    """


    class MetaOapg:
        required = {
            "color",
            "id",
            "position",
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            
            
            class color(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "blue": "BLUE",
                        "red": "RED",
                        "yellow": "YELLOW",
                        "green": "GREEN",
                        "cyan": "CYAN",
                        "purple": "PURPLE",
                        "gray": "GRAY",
                        "white": "WHITE",
                    }
                
                @schemas.classproperty
                def BLUE(cls):
                    return cls("blue")
                
                @schemas.classproperty
                def RED(cls):
                    return cls("red")
                
                @schemas.classproperty
                def YELLOW(cls):
                    return cls("yellow")
                
                @schemas.classproperty
                def GREEN(cls):
                    return cls("green")
                
                @schemas.classproperty
                def CYAN(cls):
                    return cls("cyan")
                
                @schemas.classproperty
                def PURPLE(cls):
                    return cls("purple")
                
                @schemas.classproperty
                def GRAY(cls):
                    return cls("gray")
                
                @schemas.classproperty
                def WHITE(cls):
                    return cls("white")
            id = schemas.Int64Schema
        
            @staticmethod
            def position() -> typing.Type['DashboardGadgetPosition']:
                return DashboardGadgetPosition
            moduleKey = schemas.StrSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "color": color,
                "id": id,
                "position": position,
                "moduleKey": moduleKey,
                "uri": uri,
            }
    
    color: MetaOapg.properties.color
    id: MetaOapg.properties.id
    position: 'DashboardGadgetPosition'
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> 'DashboardGadgetPosition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moduleKey"]) -> MetaOapg.properties.moduleKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "color", "id", "position", "moduleKey", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> 'DashboardGadgetPosition': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moduleKey"]) -> typing.Union[MetaOapg.properties.moduleKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "color", "id", "position", "moduleKey", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        position: 'DashboardGadgetPosition',
        title: typing.Union[MetaOapg.properties.title, str, ],
        moduleKey: typing.Union[MetaOapg.properties.moduleKey, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DashboardGadget':
        return super().__new__(
            cls,
            *args,
            color=color,
            id=id,
            position=position,
            title=title,
            moduleKey=moduleKey,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.dashboard_gadget_position import DashboardGadgetPosition
