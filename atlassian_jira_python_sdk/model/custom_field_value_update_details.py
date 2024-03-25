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


class CustomFieldValueUpdateDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of updates for a custom field.
    """


    class MetaOapg:
        
        class properties:
            
            
            class updates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomFieldValueUpdate']:
                        return CustomFieldValueUpdate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomFieldValueUpdate'], typing.List['CustomFieldValueUpdate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'updates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomFieldValueUpdate':
                    return super().__getitem__(i)
            __annotations__ = {
                "updates": updates,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updates"]) -> MetaOapg.properties.updates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["updates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updates"]) -> typing.Union[MetaOapg.properties.updates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["updates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updates: typing.Union[MetaOapg.properties.updates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldValueUpdateDetails':
        return super().__new__(
            cls,
            *args,
            updates=updates,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.custom_field_value_update import CustomFieldValueUpdate