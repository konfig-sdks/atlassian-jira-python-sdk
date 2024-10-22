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


class JQLReferenceData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Lists of JQL reference data.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def jqlReservedWords() -> typing.Type['JQLReferenceDataJqlReservedWords']:
                return JQLReferenceDataJqlReservedWords
            
            
            class visibleFieldNames(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FieldReferenceData']:
                        return FieldReferenceData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FieldReferenceData'], typing.List['FieldReferenceData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'visibleFieldNames':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FieldReferenceData':
                    return super().__getitem__(i)
            
            
            class visibleFunctionNames(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FunctionReferenceData']:
                        return FunctionReferenceData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FunctionReferenceData'], typing.List['FunctionReferenceData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'visibleFunctionNames':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FunctionReferenceData':
                    return super().__getitem__(i)
            __annotations__ = {
                "jqlReservedWords": jqlReservedWords,
                "visibleFieldNames": visibleFieldNames,
                "visibleFunctionNames": visibleFunctionNames,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jqlReservedWords"]) -> 'JQLReferenceDataJqlReservedWords': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleFieldNames"]) -> MetaOapg.properties.visibleFieldNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleFunctionNames"]) -> MetaOapg.properties.visibleFunctionNames: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jqlReservedWords", "visibleFieldNames", "visibleFunctionNames", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jqlReservedWords"]) -> typing.Union['JQLReferenceDataJqlReservedWords', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleFieldNames"]) -> typing.Union[MetaOapg.properties.visibleFieldNames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleFunctionNames"]) -> typing.Union[MetaOapg.properties.visibleFunctionNames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jqlReservedWords", "visibleFieldNames", "visibleFunctionNames", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jqlReservedWords: typing.Union['JQLReferenceDataJqlReservedWords', schemas.Unset] = schemas.unset,
        visibleFieldNames: typing.Union[MetaOapg.properties.visibleFieldNames, list, tuple, schemas.Unset] = schemas.unset,
        visibleFunctionNames: typing.Union[MetaOapg.properties.visibleFunctionNames, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JQLReferenceData':
        return super().__new__(
            cls,
            *args,
            jqlReservedWords=jqlReservedWords,
            visibleFieldNames=visibleFieldNames,
            visibleFunctionNames=visibleFunctionNames,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.field_reference_data import FieldReferenceData
from atlassian_jira_python_sdk.model.function_reference_data import FunctionReferenceData
from atlassian_jira_python_sdk.model.jql_reference_data_jql_reserved_words import JQLReferenceDataJqlReservedWords
