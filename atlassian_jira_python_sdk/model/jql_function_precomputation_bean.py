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


class JqlFunctionPrecomputationBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Jql function precomputation.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def arguments() -> typing.Type['JqlFunctionPrecomputationBeanArguments']:
                return JqlFunctionPrecomputationBeanArguments
            created = schemas.DateTimeSchema
            error = schemas.StrSchema
            field = schemas.StrSchema
            functionKey = schemas.StrSchema
            functionName = schemas.StrSchema
            id = schemas.StrSchema
            operator = schemas.StrSchema
            updated = schemas.DateTimeSchema
            used = schemas.DateTimeSchema
            value = schemas.StrSchema
            __annotations__ = {
                "arguments": arguments,
                "created": created,
                "error": error,
                "field": field,
                "functionKey": functionKey,
                "functionName": functionName,
                "id": id,
                "operator": operator,
                "updated": updated,
                "used": used,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arguments"]) -> 'JqlFunctionPrecomputationBeanArguments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> MetaOapg.properties.field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionKey"]) -> MetaOapg.properties.functionKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionName"]) -> MetaOapg.properties.functionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["used"]) -> MetaOapg.properties.used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["arguments", "created", "error", "field", "functionKey", "functionName", "id", "operator", "updated", "used", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arguments"]) -> typing.Union['JqlFunctionPrecomputationBeanArguments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> typing.Union[MetaOapg.properties.field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionKey"]) -> typing.Union[MetaOapg.properties.functionKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionName"]) -> typing.Union[MetaOapg.properties.functionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["used"]) -> typing.Union[MetaOapg.properties.used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["arguments", "created", "error", "field", "functionKey", "functionName", "id", "operator", "updated", "used", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        arguments: typing.Union['JqlFunctionPrecomputationBeanArguments', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        field: typing.Union[MetaOapg.properties.field, str, schemas.Unset] = schemas.unset,
        functionKey: typing.Union[MetaOapg.properties.functionKey, str, schemas.Unset] = schemas.unset,
        functionName: typing.Union[MetaOapg.properties.functionName, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, str, datetime, schemas.Unset] = schemas.unset,
        used: typing.Union[MetaOapg.properties.used, str, datetime, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JqlFunctionPrecomputationBean':
        return super().__new__(
            cls,
            *args,
            arguments=arguments,
            created=created,
            error=error,
            field=field,
            functionKey=functionKey,
            functionName=functionName,
            id=id,
            operator=operator,
            updated=updated,
            used=used,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jql_function_precomputation_bean_arguments import JqlFunctionPrecomputationBeanArguments