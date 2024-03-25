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


class FieldChangedClause(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A clause that asserts whether a field was changed. For example, `status CHANGED AFTER startOfMonth(-1M)`.See [CHANGED](https://confluence.atlassian.com/x/dgiiLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for more information about the CHANGED operator.
    """


    class MetaOapg:
        required = {
            "predicates",
            "field",
            "operator",
        }
        
        class properties:
        
            @staticmethod
            def field() -> typing.Type['JqlQueryField']:
                return JqlQueryField
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CHANGED(cls):
                    return cls("changed")
            
            
            class predicates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JqlQueryClauseTimePredicate']:
                        return JqlQueryClauseTimePredicate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JqlQueryClauseTimePredicate'], typing.List['JqlQueryClauseTimePredicate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'predicates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JqlQueryClauseTimePredicate':
                    return super().__getitem__(i)
            __annotations__ = {
                "field": field,
                "operator": operator,
                "predicates": predicates,
            }
    
    predicates: MetaOapg.properties.predicates
    field: 'JqlQueryField'
    operator: MetaOapg.properties.operator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predicates"]) -> MetaOapg.properties.predicates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field", "operator", "predicates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> 'JqlQueryField': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predicates"]) -> MetaOapg.properties.predicates: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field", "operator", "predicates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        predicates: typing.Union[MetaOapg.properties.predicates, list, tuple, ],
        field: 'JqlQueryField',
        operator: typing.Union[MetaOapg.properties.operator, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldChangedClause':
        return super().__new__(
            cls,
            *args,
            predicates=predicates,
            field=field,
            operator=operator,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
from atlassian_jira_python_sdk.model.jql_query_field import JqlQueryField
