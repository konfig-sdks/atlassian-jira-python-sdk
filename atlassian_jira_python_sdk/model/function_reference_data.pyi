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


class FunctionReferenceData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of functions that can be used in advanced searches.
    """


    class MetaOapg:
        
        class properties:
            displayName = schemas.StrSchema
            
            
            class isList(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            
            
            class supportsListAndSingleValueOperators(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
        
            @staticmethod
            def types() -> typing.Type['FunctionReferenceDataTypes']:
                return FunctionReferenceDataTypes
            value = schemas.StrSchema
            __annotations__ = {
                "displayName": displayName,
                "isList": isList,
                "supportsListAndSingleValueOperators": supportsListAndSingleValueOperators,
                "types": types,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isList"]) -> MetaOapg.properties.isList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsListAndSingleValueOperators"]) -> MetaOapg.properties.supportsListAndSingleValueOperators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["types"]) -> 'FunctionReferenceDataTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["displayName", "isList", "supportsListAndSingleValueOperators", "types", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isList"]) -> typing.Union[MetaOapg.properties.isList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsListAndSingleValueOperators"]) -> typing.Union[MetaOapg.properties.supportsListAndSingleValueOperators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["types"]) -> typing.Union['FunctionReferenceDataTypes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["displayName", "isList", "supportsListAndSingleValueOperators", "types", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        isList: typing.Union[MetaOapg.properties.isList, str, schemas.Unset] = schemas.unset,
        supportsListAndSingleValueOperators: typing.Union[MetaOapg.properties.supportsListAndSingleValueOperators, str, schemas.Unset] = schemas.unset,
        types: typing.Union['FunctionReferenceDataTypes', schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionReferenceData':
        return super().__new__(
            cls,
            *args,
            displayName=displayName,
            isList=isList,
            supportsListAndSingleValueOperators=supportsListAndSingleValueOperators,
            types=types,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.function_reference_data_types import FunctionReferenceDataTypes
