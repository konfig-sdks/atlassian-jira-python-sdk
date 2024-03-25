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


class FieldCreateMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The metadata describing an issue field for createmeta.
    """


    class MetaOapg:
        required = {
            "schema",
            "operations",
            "name",
            "key",
            "required",
            "fieldId",
        }
        
        class properties:
            fieldId = schemas.StrSchema
            key = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def operations() -> typing.Type['FieldCreateMetadataOperations']:
                return FieldCreateMetadataOperations
            required = schemas.BoolSchema
        
            @staticmethod
            def schema() -> typing.Type['JsonTypeBean']:
                return JsonTypeBean
        
            @staticmethod
            def allowedValues() -> typing.Type['FieldCreateMetadataAllowedValues']:
                return FieldCreateMetadataAllowedValues
            autoCompleteUrl = schemas.StrSchema
        
            @staticmethod
            def configuration() -> typing.Type['FieldCreateMetadataConfiguration']:
                return FieldCreateMetadataConfiguration
            defaultValue = schemas.AnyTypeSchema
            hasDefaultValue = schemas.BoolSchema
            __annotations__ = {
                "fieldId": fieldId,
                "key": key,
                "name": name,
                "operations": operations,
                "required": required,
                "schema": schema,
                "allowedValues": allowedValues,
                "autoCompleteUrl": autoCompleteUrl,
                "configuration": configuration,
                "defaultValue": defaultValue,
                "hasDefaultValue": hasDefaultValue,
            }
    
    schema: 'JsonTypeBean'
    operations: 'FieldCreateMetadataOperations'
    name: MetaOapg.properties.name
    key: MetaOapg.properties.key
    required: MetaOapg.properties.required
    fieldId: MetaOapg.properties.fieldId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operations"]) -> 'FieldCreateMetadataOperations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> 'JsonTypeBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedValues"]) -> 'FieldCreateMetadataAllowedValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoCompleteUrl"]) -> MetaOapg.properties.autoCompleteUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'FieldCreateMetadataConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasDefaultValue"]) -> MetaOapg.properties.hasDefaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fieldId", "key", "name", "operations", "required", "schema", "allowedValues", "autoCompleteUrl", "configuration", "defaultValue", "hasDefaultValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operations"]) -> 'FieldCreateMetadataOperations': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> 'JsonTypeBean': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedValues"]) -> typing.Union['FieldCreateMetadataAllowedValues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoCompleteUrl"]) -> typing.Union[MetaOapg.properties.autoCompleteUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['FieldCreateMetadataConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasDefaultValue"]) -> typing.Union[MetaOapg.properties.hasDefaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fieldId", "key", "name", "operations", "required", "schema", "allowedValues", "autoCompleteUrl", "configuration", "defaultValue", "hasDefaultValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        schema: 'JsonTypeBean',
        operations: 'FieldCreateMetadataOperations',
        name: typing.Union[MetaOapg.properties.name, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        fieldId: typing.Union[MetaOapg.properties.fieldId, str, ],
        allowedValues: typing.Union['FieldCreateMetadataAllowedValues', schemas.Unset] = schemas.unset,
        autoCompleteUrl: typing.Union[MetaOapg.properties.autoCompleteUrl, str, schemas.Unset] = schemas.unset,
        configuration: typing.Union['FieldCreateMetadataConfiguration', schemas.Unset] = schemas.unset,
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        hasDefaultValue: typing.Union[MetaOapg.properties.hasDefaultValue, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldCreateMetadata':
        return super().__new__(
            cls,
            *args,
            schema=schema,
            operations=operations,
            name=name,
            key=key,
            required=required,
            fieldId=fieldId,
            allowedValues=allowedValues,
            autoCompleteUrl=autoCompleteUrl,
            configuration=configuration,
            defaultValue=defaultValue,
            hasDefaultValue=hasDefaultValue,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.field_create_metadata_allowed_values import FieldCreateMetadataAllowedValues
from atlassian_jira_python_sdk.model.field_create_metadata_configuration import FieldCreateMetadataConfiguration
from atlassian_jira_python_sdk.model.field_create_metadata_operations import FieldCreateMetadataOperations
from atlassian_jira_python_sdk.model.json_type_bean import JsonTypeBean