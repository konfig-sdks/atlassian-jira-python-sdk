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


class ChangedWorklog(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a changed worklog.
    """


    class MetaOapg:
        
        class properties:
            
            
            class properties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EntityProperty']:
                        return EntityProperty
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EntityProperty'], typing.List['EntityProperty']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'properties':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EntityProperty':
                    return super().__getitem__(i)
            updatedTime = schemas.Int64Schema
            worklogId = schemas.Int64Schema
            __annotations__ = {
                "properties": properties,
                "updatedTime": updatedTime,
                "worklogId": worklogId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedTime"]) -> MetaOapg.properties.updatedTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worklogId"]) -> MetaOapg.properties.worklogId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["properties", "updatedTime", "worklogId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedTime"]) -> typing.Union[MetaOapg.properties.updatedTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worklogId"]) -> typing.Union[MetaOapg.properties.worklogId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["properties", "updatedTime", "worklogId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        properties: typing.Union[MetaOapg.properties.properties, list, tuple, schemas.Unset] = schemas.unset,
        updatedTime: typing.Union[MetaOapg.properties.updatedTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        worklogId: typing.Union[MetaOapg.properties.worklogId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangedWorklog':
        return super().__new__(
            cls,
            *args,
            properties=properties,
            updatedTime=updatedTime,
            worklogId=worklogId,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.entity_property import EntityProperty