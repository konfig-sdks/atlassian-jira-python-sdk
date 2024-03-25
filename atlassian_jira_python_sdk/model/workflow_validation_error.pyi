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


class WorkflowValidationError(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details about a workflow validation error.
    """


    class MetaOapg:
        
        class properties:
            code = schemas.StrSchema
        
            @staticmethod
            def elementReference() -> typing.Type['WorkflowElementReference']:
                return WorkflowElementReference
            
            
            class level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WARNING(cls):
                    return cls("WARNING")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            message = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RULE(cls):
                    return cls("RULE")
                
                @schemas.classproperty
                def STATUS(cls):
                    return cls("STATUS")
                
                @schemas.classproperty
                def STATUS_LAYOUT(cls):
                    return cls("STATUS_LAYOUT")
                
                @schemas.classproperty
                def STATUS_PROPERTY(cls):
                    return cls("STATUS_PROPERTY")
                
                @schemas.classproperty
                def WORKFLOW(cls):
                    return cls("WORKFLOW")
                
                @schemas.classproperty
                def TRANSITION(cls):
                    return cls("TRANSITION")
                
                @schemas.classproperty
                def TRANSITION_PROPERTY(cls):
                    return cls("TRANSITION_PROPERTY")
                
                @schemas.classproperty
                def SCOPE(cls):
                    return cls("SCOPE")
                
                @schemas.classproperty
                def STATUS_MAPPING(cls):
                    return cls("STATUS_MAPPING")
                
                @schemas.classproperty
                def TRIGGER(cls):
                    return cls("TRIGGER")
            __annotations__ = {
                "code": code,
                "elementReference": elementReference,
                "level": level,
                "message": message,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elementReference"]) -> 'WorkflowElementReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "elementReference", "level", "message", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elementReference"]) -> typing.Union['WorkflowElementReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "elementReference", "level", "message", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        elementReference: typing.Union['WorkflowElementReference', schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowValidationError':
        return super().__new__(
            cls,
            *args,
            code=code,
            elementReference=elementReference,
            level=level,
            message=message,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_element_reference import WorkflowElementReference
