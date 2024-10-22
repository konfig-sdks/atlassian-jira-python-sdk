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


class ChangedValueBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of names changed in the record event.
    """


    class MetaOapg:
        
        class properties:
            changedFrom = schemas.StrSchema
            changedTo = schemas.StrSchema
            fieldName = schemas.StrSchema
            __annotations__ = {
                "changedFrom": changedFrom,
                "changedTo": changedTo,
                "fieldName": fieldName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changedFrom"]) -> MetaOapg.properties.changedFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changedTo"]) -> MetaOapg.properties.changedTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldName"]) -> MetaOapg.properties.fieldName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["changedFrom", "changedTo", "fieldName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changedFrom"]) -> typing.Union[MetaOapg.properties.changedFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changedTo"]) -> typing.Union[MetaOapg.properties.changedTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldName"]) -> typing.Union[MetaOapg.properties.fieldName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["changedFrom", "changedTo", "fieldName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        changedFrom: typing.Union[MetaOapg.properties.changedFrom, str, schemas.Unset] = schemas.unset,
        changedTo: typing.Union[MetaOapg.properties.changedTo, str, schemas.Unset] = schemas.unset,
        fieldName: typing.Union[MetaOapg.properties.fieldName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangedValueBean':
        return super().__new__(
            cls,
            *args,
            changedFrom=changedFrom,
            changedTo=changedTo,
            fieldName=fieldName,
            _configuration=_configuration,
            **kwargs,
        )
