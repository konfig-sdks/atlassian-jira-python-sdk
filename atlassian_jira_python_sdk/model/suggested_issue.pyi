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


class SuggestedIssue(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An issue suggested for use in the issue picker auto-completion.
    """


    class MetaOapg:
        
        class properties:
            summary = schemas.StrSchema
            id = schemas.Int64Schema
            img = schemas.StrSchema
            key = schemas.StrSchema
            keyHtml = schemas.StrSchema
            summaryText = schemas.StrSchema
            __annotations__ = {
                "summary": summary,
                "id": id,
                "img": img,
                "key": key,
                "keyHtml": keyHtml,
                "summaryText": summaryText,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["img"]) -> MetaOapg.properties.img: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyHtml"]) -> MetaOapg.properties.keyHtml: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summaryText"]) -> MetaOapg.properties.summaryText: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "id", "img", "key", "keyHtml", "summaryText", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["img"]) -> typing.Union[MetaOapg.properties.img, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyHtml"]) -> typing.Union[MetaOapg.properties.keyHtml, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summaryText"]) -> typing.Union[MetaOapg.properties.summaryText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "id", "img", "key", "keyHtml", "summaryText", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        img: typing.Union[MetaOapg.properties.img, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        keyHtml: typing.Union[MetaOapg.properties.keyHtml, str, schemas.Unset] = schemas.unset,
        summaryText: typing.Union[MetaOapg.properties.summaryText, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SuggestedIssue':
        return super().__new__(
            cls,
            *args,
            summary=summary,
            id=id,
            img=img,
            key=key,
            keyHtml=keyHtml,
            summaryText=summaryText,
            _configuration=_configuration,
            **kwargs,
        )