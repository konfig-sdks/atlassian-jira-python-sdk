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


class CreateWorkflowCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A workflow transition condition.
    """


    class MetaOapg:
        
        class properties:
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreateWorkflowCondition']:
                        return CreateWorkflowCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CreateWorkflowCondition'], typing.List['CreateWorkflowCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CreateWorkflowCondition':
                    return super().__getitem__(i)
        
            @staticmethod
            def configuration() -> typing.Type['CreateWorkflowConditionConfiguration']:
                return CreateWorkflowConditionConfiguration
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AND(cls):
                    return cls("AND")
                
                @schemas.classproperty
                def OR(cls):
                    return cls("OR")
            type = schemas.StrSchema
            __annotations__ = {
                "conditions": conditions,
                "configuration": configuration,
                "operator": operator,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'CreateWorkflowConditionConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditions", "configuration", "operator", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['CreateWorkflowConditionConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditions", "configuration", "operator", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        configuration: typing.Union['CreateWorkflowConditionConfiguration', schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateWorkflowCondition':
        return super().__new__(
            cls,
            *args,
            conditions=conditions,
            configuration=configuration,
            operator=operator,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.create_workflow_condition_configuration import CreateWorkflowConditionConfiguration