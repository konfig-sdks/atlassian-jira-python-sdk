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


class FieldValueClause(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A clause that asserts the current value of a field. For example, `summary ~ test`.
    """


    class MetaOapg:
        required = {
            "field",
            "operand",
            "operator",
        }
        
        class properties:
        
            @staticmethod
            def field() -> typing.Type['JqlQueryField']:
                return JqlQueryField
        
            @staticmethod
            def operand() -> typing.Type['JqlQueryClauseOperand']:
                return JqlQueryClauseOperand
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EQUALS(cls):
                    return cls("=")
                
                @schemas.classproperty
                def _(cls):
                    return cls("!=")
                
                @schemas.classproperty
                def GREATER_THAN(cls):
                    return cls(">")
                
                @schemas.classproperty
                def LESS_THAN(cls):
                    return cls("<")
                
                @schemas.classproperty
                def _(cls):
                    return cls(">=")
                
                @schemas.classproperty
                def _(cls):
                    return cls("<=")
                
                @schemas.classproperty
                def IN(cls):
                    return cls("in")
                
                @schemas.classproperty
                def NOT_IN(cls):
                    return cls("not in")
                
                @schemas.classproperty
                def TILDE(cls):
                    return cls("~")
                
                @schemas.classproperty
                def _(cls):
                    return cls("~=")
                
                @schemas.classproperty
                def IS(cls):
                    return cls("is")
                
                @schemas.classproperty
                def IS_NOT(cls):
                    return cls("is not")
            __annotations__ = {
                "field": field,
                "operand": operand,
                "operator": operator,
            }
    
    field: 'JqlQueryField'
    operand: 'JqlQueryClauseOperand'
    operator: MetaOapg.properties.operator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operand"]) -> 'JqlQueryClauseOperand': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field", "operand", "operator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operand"]) -> 'JqlQueryClauseOperand': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field", "operand", "operator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field: 'JqlQueryField',
        operand: 'JqlQueryClauseOperand',
        operator: typing.Union[MetaOapg.properties.operator, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldValueClause':
        return super().__new__(
            cls,
            *args,
            field=field,
            operand=operand,
            operator=operator,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jql_query_clause_operand import JqlQueryClauseOperand
from atlassian_jira_python_sdk.model.jql_query_field import JqlQueryField
