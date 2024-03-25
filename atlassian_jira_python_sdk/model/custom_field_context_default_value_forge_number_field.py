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


class CustomFieldContextDefaultValueForgeNumberField(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Default value for a Forge number custom field.
    """


    class MetaOapg:
        required = {
            "number",
            "contextId",
            "type",
        }
        
        class properties:
            contextId = schemas.StrSchema
            number = schemas.Float64Schema
            type = schemas.StrSchema
            __annotations__ = {
                "contextId": contextId,
                "number": number,
                "type": type,
            }
    
    number: MetaOapg.properties.number
    contextId: MetaOapg.properties.contextId
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextId"]) -> MetaOapg.properties.contextId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contextId", "number", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextId"]) -> MetaOapg.properties.contextId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contextId", "number", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, float, ],
        contextId: typing.Union[MetaOapg.properties.contextId, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldContextDefaultValueForgeNumberField':
        return super().__new__(
            cls,
            *args,
            number=number,
            contextId=contextId,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )