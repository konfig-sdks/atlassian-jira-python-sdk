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


class ApplicationProperty(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an application property.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def allowedValues() -> typing.Type['ApplicationPropertyAllowedValues']:
                return ApplicationPropertyAllowedValues
            defaultValue = schemas.StrSchema
            desc = schemas.StrSchema
            example = schemas.StrSchema
            id = schemas.StrSchema
            key = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            value = schemas.StrSchema
            x_konfig_original_example = schemas.StrSchema
            __annotations__ = {
                "allowedValues": allowedValues,
                "defaultValue": defaultValue,
                "desc": desc,
                "example": example,
                "id": id,
                "key": key,
                "name": name,
                "type": type,
                "value": value,
                "x-konfig-original-example": x_konfig_original_example,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedValues"]) -> 'ApplicationPropertyAllowedValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desc"]) -> MetaOapg.properties.desc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["example"]) -> MetaOapg.properties.example: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x-konfig-original-example"]) -> MetaOapg.properties.x_konfig_original_example: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowedValues", "defaultValue", "desc", "example", "id", "key", "name", "type", "value", "x-konfig-original-example", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedValues"]) -> typing.Union['ApplicationPropertyAllowedValues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desc"]) -> typing.Union[MetaOapg.properties.desc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["example"]) -> typing.Union[MetaOapg.properties.example, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x-konfig-original-example"]) -> typing.Union[MetaOapg.properties.x_konfig_original_example, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowedValues", "defaultValue", "desc", "example", "id", "key", "name", "type", "value", "x-konfig-original-example", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        allowedValues: typing.Union['ApplicationPropertyAllowedValues', schemas.Unset] = schemas.unset,
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, str, schemas.Unset] = schemas.unset,
        desc: typing.Union[MetaOapg.properties.desc, str, schemas.Unset] = schemas.unset,
        example: typing.Union[MetaOapg.properties.example, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationProperty':
        return super().__new__(
            cls,
            *args,
            allowedValues=allowedValues,
            defaultValue=defaultValue,
            desc=desc,
            example=example,
            id=id,
            key=key,
            name=name,
            type=type,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.application_property_allowed_values import ApplicationPropertyAllowedValues
