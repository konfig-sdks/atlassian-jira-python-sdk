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


class FoundUsers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The list of users found in a search, including header text (Showing X of Y matching users) and total of matched users.
    """


    class MetaOapg:
        
        class properties:
            header = schemas.StrSchema
            total = schemas.Int32Schema
            
            
            class users(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserPickerUser']:
                        return UserPickerUser
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserPickerUser'], typing.List['UserPickerUser']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'users':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserPickerUser':
                    return super().__getitem__(i)
            __annotations__ = {
                "header": header,
                "total": total,
                "users": users,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["header"]) -> MetaOapg.properties.header: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["header", "total", "users", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["header"]) -> typing.Union[MetaOapg.properties.header, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union[MetaOapg.properties.users, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["header", "total", "users", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        header: typing.Union[MetaOapg.properties.header, str, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        users: typing.Union[MetaOapg.properties.users, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FoundUsers':
        return super().__new__(
            cls,
            *args,
            header=header,
            total=total,
            users=users,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.user_picker_user import UserPickerUser
