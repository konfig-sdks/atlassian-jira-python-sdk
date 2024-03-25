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


class AvatarUrlsBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            _16x16 = schemas.StrSchema
            _24x24 = schemas.StrSchema
            _32x32 = schemas.StrSchema
            _48x48 = schemas.StrSchema
            __annotations__ = {
                "16x16": _16x16,
                "24x24": _24x24,
                "32x32": _32x32,
                "48x48": _48x48,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["16x16"]) -> MetaOapg.properties._16x16: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["24x24"]) -> MetaOapg.properties._24x24: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["32x32"]) -> MetaOapg.properties._32x32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["48x48"]) -> MetaOapg.properties._48x48: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["16x16", "24x24", "32x32", "48x48", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["16x16"]) -> typing.Union[MetaOapg.properties._16x16, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["24x24"]) -> typing.Union[MetaOapg.properties._24x24, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["32x32"]) -> typing.Union[MetaOapg.properties._32x32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["48x48"]) -> typing.Union[MetaOapg.properties._48x48, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["16x16", "24x24", "32x32", "48x48", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AvatarUrlsBean':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
