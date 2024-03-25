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


class AvailableWorkflowSystemRule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Atlassian provided system rules available.
    """


    class MetaOapg:
        required = {
            "isAvailableForInitialTransition",
            "ruleType",
            "name",
            "description",
            "isVisible",
            "ruleKey",
            "incompatibleRuleKeys",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def incompatibleRuleKeys() -> typing.Type['AvailableWorkflowSystemRuleIncompatibleRuleKeys']:
                return AvailableWorkflowSystemRuleIncompatibleRuleKeys
            isAvailableForInitialTransition = schemas.BoolSchema
            isVisible = schemas.BoolSchema
            name = schemas.StrSchema
            ruleKey = schemas.StrSchema
            
            
            class ruleType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONDITION(cls):
                    return cls("Condition")
                
                @schemas.classproperty
                def VALIDATOR(cls):
                    return cls("Validator")
                
                @schemas.classproperty
                def FUNCTION(cls):
                    return cls("Function")
                
                @schemas.classproperty
                def SCREEN(cls):
                    return cls("Screen")
            __annotations__ = {
                "description": description,
                "incompatibleRuleKeys": incompatibleRuleKeys,
                "isAvailableForInitialTransition": isAvailableForInitialTransition,
                "isVisible": isVisible,
                "name": name,
                "ruleKey": ruleKey,
                "ruleType": ruleType,
            }
    
    isAvailableForInitialTransition: MetaOapg.properties.isAvailableForInitialTransition
    ruleType: MetaOapg.properties.ruleType
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    isVisible: MetaOapg.properties.isVisible
    ruleKey: MetaOapg.properties.ruleKey
    incompatibleRuleKeys: 'AvailableWorkflowSystemRuleIncompatibleRuleKeys'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incompatibleRuleKeys"]) -> 'AvailableWorkflowSystemRuleIncompatibleRuleKeys': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAvailableForInitialTransition"]) -> MetaOapg.properties.isAvailableForInitialTransition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleKey"]) -> MetaOapg.properties.ruleKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleType"]) -> MetaOapg.properties.ruleType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "incompatibleRuleKeys", "isAvailableForInitialTransition", "isVisible", "name", "ruleKey", "ruleType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incompatibleRuleKeys"]) -> 'AvailableWorkflowSystemRuleIncompatibleRuleKeys': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAvailableForInitialTransition"]) -> MetaOapg.properties.isAvailableForInitialTransition: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleKey"]) -> MetaOapg.properties.ruleKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleType"]) -> MetaOapg.properties.ruleType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "incompatibleRuleKeys", "isAvailableForInitialTransition", "isVisible", "name", "ruleKey", "ruleType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isAvailableForInitialTransition: typing.Union[MetaOapg.properties.isAvailableForInitialTransition, bool, ],
        ruleType: typing.Union[MetaOapg.properties.ruleType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        isVisible: typing.Union[MetaOapg.properties.isVisible, bool, ],
        ruleKey: typing.Union[MetaOapg.properties.ruleKey, str, ],
        incompatibleRuleKeys: 'AvailableWorkflowSystemRuleIncompatibleRuleKeys',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AvailableWorkflowSystemRule':
        return super().__new__(
            cls,
            *args,
            isAvailableForInitialTransition=isAvailableForInitialTransition,
            ruleType=ruleType,
            name=name,
            description=description,
            isVisible=isVisible,
            ruleKey=ruleKey,
            incompatibleRuleKeys=incompatibleRuleKeys,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.available_workflow_system_rule_incompatible_rule_keys import AvailableWorkflowSystemRuleIncompatibleRuleKeys
