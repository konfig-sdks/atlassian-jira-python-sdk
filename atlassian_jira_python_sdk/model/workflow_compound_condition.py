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


class WorkflowCompoundCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A compound workflow transition rule condition. This object returns `nodeType` as `compound`.
    """


    class MetaOapg:
        required = {
            "conditions",
            "nodeType",
            "operator",
        }
        
        class properties:
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowCondition']:
                        return WorkflowCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowCondition'], typing.List['WorkflowCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowCondition':
                    return super().__getitem__(i)
            nodeType = schemas.StrSchema
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AND": "AND",
                        "OR": "OR",
                    }
                
                @schemas.classproperty
                def AND(cls):
                    return cls("AND")
                
                @schemas.classproperty
                def OR(cls):
                    return cls("OR")
            __annotations__ = {
                "conditions": conditions,
                "nodeType": nodeType,
                "operator": operator,
            }
    
    conditions: MetaOapg.properties.conditions
    nodeType: MetaOapg.properties.nodeType
    operator: MetaOapg.properties.operator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeType"]) -> MetaOapg.properties.nodeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditions", "nodeType", "operator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeType"]) -> MetaOapg.properties.nodeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditions", "nodeType", "operator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, ],
        nodeType: typing.Union[MetaOapg.properties.nodeType, str, ],
        operator: typing.Union[MetaOapg.properties.operator, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowCompoundCondition':
        return super().__new__(
            cls,
            *args,
            conditions=conditions,
            nodeType=nodeType,
            operator=operator,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_condition import WorkflowCondition
