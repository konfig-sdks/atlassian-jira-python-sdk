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


class JsonTypeBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The schema of a field.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
        
            @staticmethod
            def configuration() -> typing.Type['JsonTypeBeanConfiguration']:
                return JsonTypeBeanConfiguration
            custom = schemas.StrSchema
            customId = schemas.Int64Schema
            items = schemas.StrSchema
            system = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "configuration": configuration,
                "custom": custom,
                "customId": customId,
                "items": items,
                "system": system,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'JsonTypeBeanConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> MetaOapg.properties.custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customId"]) -> MetaOapg.properties.customId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "configuration", "custom", "customId", "items", "system", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['JsonTypeBeanConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customId"]) -> typing.Union[MetaOapg.properties.customId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union[MetaOapg.properties.system, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "configuration", "custom", "customId", "items", "system", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        configuration: typing.Union['JsonTypeBeanConfiguration', schemas.Unset] = schemas.unset,
        custom: typing.Union[MetaOapg.properties.custom, str, schemas.Unset] = schemas.unset,
        customId: typing.Union[MetaOapg.properties.customId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, str, schemas.Unset] = schemas.unset,
        system: typing.Union[MetaOapg.properties.system, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonTypeBean':
        return super().__new__(
            cls,
            *args,
            type=type,
            configuration=configuration,
            custom=custom,
            customId=customId,
            items=items,
            system=system,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.json_type_bean_configuration import JsonTypeBeanConfiguration