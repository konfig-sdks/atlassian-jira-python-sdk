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


class AvailableWorkflowConnectRule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Connect provided ecosystem rules available.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            addonKey = schemas.StrSchema
            createUrl = schemas.StrSchema
            editUrl = schemas.StrSchema
            moduleKey = schemas.StrSchema
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
            viewUrl = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "addonKey": addonKey,
                "createUrl": createUrl,
                "editUrl": editUrl,
                "moduleKey": moduleKey,
                "name": name,
                "ruleKey": ruleKey,
                "ruleType": ruleType,
                "viewUrl": viewUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addonKey"]) -> MetaOapg.properties.addonKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUrl"]) -> MetaOapg.properties.createUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editUrl"]) -> MetaOapg.properties.editUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moduleKey"]) -> MetaOapg.properties.moduleKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleKey"]) -> MetaOapg.properties.ruleKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleType"]) -> MetaOapg.properties.ruleType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewUrl"]) -> MetaOapg.properties.viewUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "addonKey", "createUrl", "editUrl", "moduleKey", "name", "ruleKey", "ruleType", "viewUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addonKey"]) -> typing.Union[MetaOapg.properties.addonKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUrl"]) -> typing.Union[MetaOapg.properties.createUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editUrl"]) -> typing.Union[MetaOapg.properties.editUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moduleKey"]) -> typing.Union[MetaOapg.properties.moduleKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleKey"]) -> typing.Union[MetaOapg.properties.ruleKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleType"]) -> typing.Union[MetaOapg.properties.ruleType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewUrl"]) -> typing.Union[MetaOapg.properties.viewUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "addonKey", "createUrl", "editUrl", "moduleKey", "name", "ruleKey", "ruleType", "viewUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        addonKey: typing.Union[MetaOapg.properties.addonKey, str, schemas.Unset] = schemas.unset,
        createUrl: typing.Union[MetaOapg.properties.createUrl, str, schemas.Unset] = schemas.unset,
        editUrl: typing.Union[MetaOapg.properties.editUrl, str, schemas.Unset] = schemas.unset,
        moduleKey: typing.Union[MetaOapg.properties.moduleKey, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        ruleKey: typing.Union[MetaOapg.properties.ruleKey, str, schemas.Unset] = schemas.unset,
        ruleType: typing.Union[MetaOapg.properties.ruleType, str, schemas.Unset] = schemas.unset,
        viewUrl: typing.Union[MetaOapg.properties.viewUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AvailableWorkflowConnectRule':
        return super().__new__(
            cls,
            *args,
            description=description,
            addonKey=addonKey,
            createUrl=createUrl,
            editUrl=editUrl,
            moduleKey=moduleKey,
            name=name,
            ruleKey=ruleKey,
            ruleType=ruleType,
            viewUrl=viewUrl,
            _configuration=_configuration,
            **kwargs,
        )
