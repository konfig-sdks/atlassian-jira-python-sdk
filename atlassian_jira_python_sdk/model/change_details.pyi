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


class ChangeDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A change item.
    """


    class MetaOapg:
        
        class properties:
            field = schemas.StrSchema
            fieldId = schemas.StrSchema
            fieldtype = schemas.StrSchema
            _from = schemas.StrSchema
            fromString = schemas.StrSchema
            to = schemas.StrSchema
            toString = schemas.StrSchema
            __annotations__ = {
                "field": field,
                "fieldId": fieldId,
                "fieldtype": fieldtype,
                "from": _from,
                "fromString": fromString,
                "to": to,
                "toString": toString,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> MetaOapg.properties.field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldtype"]) -> MetaOapg.properties.fieldtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromString"]) -> MetaOapg.properties.fromString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toString"]) -> MetaOapg.properties.toString: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field", "fieldId", "fieldtype", "from", "fromString", "to", "toString", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> typing.Union[MetaOapg.properties.field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldId"]) -> typing.Union[MetaOapg.properties.fieldId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldtype"]) -> typing.Union[MetaOapg.properties.fieldtype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromString"]) -> typing.Union[MetaOapg.properties.fromString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toString"]) -> typing.Union[MetaOapg.properties.toString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field", "fieldId", "fieldtype", "from", "fromString", "to", "toString", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field: typing.Union[MetaOapg.properties.field, str, schemas.Unset] = schemas.unset,
        fieldId: typing.Union[MetaOapg.properties.fieldId, str, schemas.Unset] = schemas.unset,
        fieldtype: typing.Union[MetaOapg.properties.fieldtype, str, schemas.Unset] = schemas.unset,
        fromString: typing.Union[MetaOapg.properties.fromString, str, schemas.Unset] = schemas.unset,
        to: typing.Union[MetaOapg.properties.to, str, schemas.Unset] = schemas.unset,
        toString: typing.Union[MetaOapg.properties.toString, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangeDetails':
        return super().__new__(
            cls,
            *args,
            field=field,
            fieldId=fieldId,
            fieldtype=fieldtype,
            fromString=fromString,
            to=to,
            toString=toString,
            _configuration=_configuration,
            **kwargs,
        )