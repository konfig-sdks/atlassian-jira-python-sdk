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


class CustomFieldConfigurations(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of configurations for a custom field.
    """


    class MetaOapg:
        required = {
            "configurations",
        }
        
        class properties:
            
            
            class configurations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContextualConfiguration']:
                        return ContextualConfiguration
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContextualConfiguration'], typing.List['ContextualConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configurations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContextualConfiguration':
                    return super().__getitem__(i)
            __annotations__ = {
                "configurations": configurations,
            }
    
    configurations: MetaOapg.properties.configurations
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurations"]) -> MetaOapg.properties.configurations: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurations"]) -> MetaOapg.properties.configurations: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        configurations: typing.Union[MetaOapg.properties.configurations, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldConfigurations':
        return super().__new__(
            cls,
            *args,
            configurations=configurations,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.contextual_configuration import ContextualConfiguration
