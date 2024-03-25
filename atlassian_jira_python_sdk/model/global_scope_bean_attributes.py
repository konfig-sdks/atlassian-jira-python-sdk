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


class GlobalScopeBeanAttributes(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Defines the behavior of the option in the global context.If notSelectable is set, the option cannot be set as the field's value. This is useful for archiving an option that has previously been selected but shouldn't be used anymore.If defaultValue is set, the option is selected by default.
    """


    class MetaOapg:
        unique_items = True
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "notSelectable": "NOT_SELECTABLE",
                    "defaultValue": "DEFAULT_VALUE",
                }
            
            @schemas.classproperty
            def NOT_SELECTABLE(cls):
                return cls("notSelectable")
            
            @schemas.classproperty
            def DEFAULT_VALUE(cls):
                return cls("defaultValue")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GlobalScopeBeanAttributes':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
