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


class PageBeanGroupDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A page of items.
    """


    class MetaOapg:
        
        class properties:
            isLast = schemas.BoolSchema
            maxResults = schemas.Int32Schema
            nextPage = schemas.StrSchema
            _self = schemas.StrSchema
            startAt = schemas.Int64Schema
            total = schemas.Int64Schema
            
            
            class values(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GroupDetails']:
                        return GroupDetails
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GroupDetails'], typing.List['GroupDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'values':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GroupDetails':
                    return super().__getitem__(i)
            __annotations__ = {
                "isLast": isLast,
                "maxResults": maxResults,
                "nextPage": nextPage,
                "self": _self,
                "startAt": startAt,
                "total": total,
                "values": values,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isLast"]) -> MetaOapg.properties.isLast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxResults"]) -> MetaOapg.properties.maxResults: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPage"]) -> MetaOapg.properties.nextPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startAt"]) -> MetaOapg.properties.startAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isLast", "maxResults", "nextPage", "self", "startAt", "total", "values", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isLast"]) -> typing.Union[MetaOapg.properties.isLast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxResults"]) -> typing.Union[MetaOapg.properties.maxResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPage"]) -> typing.Union[MetaOapg.properties.nextPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startAt"]) -> typing.Union[MetaOapg.properties.startAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union[MetaOapg.properties.values, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isLast", "maxResults", "nextPage", "self", "startAt", "total", "values", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isLast: typing.Union[MetaOapg.properties.isLast, bool, schemas.Unset] = schemas.unset,
        maxResults: typing.Union[MetaOapg.properties.maxResults, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nextPage: typing.Union[MetaOapg.properties.nextPage, str, schemas.Unset] = schemas.unset,
        startAt: typing.Union[MetaOapg.properties.startAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        values: typing.Union[MetaOapg.properties.values, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageBeanGroupDetails':
        return super().__new__(
            cls,
            *args,
            isLast=isLast,
            maxResults=maxResults,
            nextPage=nextPage,
            startAt=startAt,
            total=total,
            values=values,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.group_details import GroupDetails
