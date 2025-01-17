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


class ValidationOptionsForUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The level of validation to return from the API. If no values are provided, the default would return `WARNING` and `ERROR` level validation results.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def levels() -> typing.Type['ValidationOptionsForUpdateLevels']:
                return ValidationOptionsForUpdateLevels
            __annotations__ = {
                "levels": levels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["levels"]) -> 'ValidationOptionsForUpdateLevels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["levels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["levels"]) -> typing.Union['ValidationOptionsForUpdateLevels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["levels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        levels: typing.Union['ValidationOptionsForUpdateLevels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ValidationOptionsForUpdate':
        return super().__new__(
            cls,
            *args,
            levels=levels,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.validation_options_for_update_levels import ValidationOptionsForUpdateLevels
