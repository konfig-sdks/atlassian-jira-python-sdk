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


class UserFilter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Filter for a User Picker (single) custom field.
    """


    class MetaOapg:
        required = {
            "enabled",
        }
        
        class properties:
            enabled = schemas.BoolSchema
        
            @staticmethod
            def groups() -> typing.Type['UserFilterGroups']:
                return UserFilterGroups
        
            @staticmethod
            def roleIds() -> typing.Type['UserFilterRoleIds']:
                return UserFilterRoleIds
            __annotations__ = {
                "enabled": enabled,
                "groups": groups,
                "roleIds": roleIds,
            }
    
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> 'UserFilterGroups': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleIds"]) -> 'UserFilterRoleIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled", "groups", "roleIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union['UserFilterGroups', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleIds"]) -> typing.Union['UserFilterRoleIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled", "groups", "roleIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        groups: typing.Union['UserFilterGroups', schemas.Unset] = schemas.unset,
        roleIds: typing.Union['UserFilterRoleIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserFilter':
        return super().__new__(
            cls,
            *args,
            enabled=enabled,
            groups=groups,
            roleIds=roleIds,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.user_filter_groups import UserFilterGroups
from atlassian_jira_python_sdk.model.user_filter_role_ids import UserFilterRoleIds