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


class JqlQueryOrderByClauseElement(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An element of the order-by JQL clause.
    """


    class MetaOapg:
        required = {
            "field",
        }
        
        class properties:
        
            @staticmethod
            def field() -> typing.Type['JqlQueryField']:
                return JqlQueryField
            
            
            class direction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ASC(cls):
                    return cls("asc")
                
                @schemas.classproperty
                def DESC(cls):
                    return cls("desc")
            __annotations__ = {
                "field": field,
                "direction": direction,
            }
    
    field: 'JqlQueryField'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field", "direction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field", "direction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field: 'JqlQueryField',
        direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JqlQueryOrderByClauseElement':
        return super().__new__(
            cls,
            *args,
            field=field,
            direction=direction,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jql_query_field import JqlQueryField
