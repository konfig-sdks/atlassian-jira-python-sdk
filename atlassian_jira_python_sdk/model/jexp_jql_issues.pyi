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


class JexpJqlIssues(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The JQL specifying the issues available in the evaluated Jira expression under the `issues` context variable. Not all issues returned by the JQL query are loaded, only those described by the `startAt` and `maxResults` properties. To determine whether it is necessary to iterate to ensure all the issues returned by the JQL query are evaluated, inspect `meta.issues.jql.count` in the response.
    """


    class MetaOapg:
        
        class properties:
            maxResults = schemas.Int32Schema
            query = schemas.StrSchema
            startAt = schemas.Int64Schema
            
            
            class validation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STRICT(cls):
                    return cls("strict")
                
                @schemas.classproperty
                def WARN(cls):
                    return cls("warn")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
            __annotations__ = {
                "maxResults": maxResults,
                "query": query,
                "startAt": startAt,
                "validation": validation,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxResults"]) -> MetaOapg.properties.maxResults: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startAt"]) -> MetaOapg.properties.startAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation"]) -> MetaOapg.properties.validation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxResults", "query", "startAt", "validation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxResults"]) -> typing.Union[MetaOapg.properties.maxResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startAt"]) -> typing.Union[MetaOapg.properties.startAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union[MetaOapg.properties.validation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxResults", "query", "startAt", "validation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxResults: typing.Union[MetaOapg.properties.maxResults, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        startAt: typing.Union[MetaOapg.properties.startAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        validation: typing.Union[MetaOapg.properties.validation, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JexpJqlIssues':
        return super().__new__(
            cls,
            *args,
            maxResults=maxResults,
            query=query,
            startAt=startAt,
            validation=validation,
            _configuration=_configuration,
            **kwargs,
        )
