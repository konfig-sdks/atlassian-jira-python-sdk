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


class JqlQueryClauseTimePredicate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A time predicate for a temporal JQL clause.
    """


    class MetaOapg:
        required = {
            "operand",
            "operator",
        }
        
        class properties:
        
            @staticmethod
            def operand() -> typing.Type['JqlQueryClauseOperand']:
                return JqlQueryClauseOperand
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "before": "BEFORE",
                        "after": "AFTER",
                        "from": "FROM",
                        "to": "TO",
                        "true": "TRUE",
                        "during": "DURING",
                        "by": "BY",
                    }
                
                @schemas.classproperty
                def BEFORE(cls):
                    return cls("before")
                
                @schemas.classproperty
                def AFTER(cls):
                    return cls("after")
                
                @schemas.classproperty
                def FROM(cls):
                    return cls("from")
                
                @schemas.classproperty
                def TO(cls):
                    return cls("to")
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def DURING(cls):
                    return cls("during")
                
                @schemas.classproperty
                def BY(cls):
                    return cls("by")
            __annotations__ = {
                "operand": operand,
                "operator": operator,
            }
    
    operand: 'JqlQueryClauseOperand'
    operator: MetaOapg.properties.operator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operand"]) -> 'JqlQueryClauseOperand': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["operand", "operator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operand"]) -> 'JqlQueryClauseOperand': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["operand", "operator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        operand: 'JqlQueryClauseOperand',
        operator: typing.Union[MetaOapg.properties.operator, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JqlQueryClauseTimePredicate':
        return super().__new__(
            cls,
            *args,
            operand=operand,
            operator=operator,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jql_query_clause_operand import JqlQueryClauseOperand