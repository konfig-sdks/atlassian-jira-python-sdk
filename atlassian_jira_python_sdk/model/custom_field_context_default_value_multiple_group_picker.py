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


class CustomFieldContextDefaultValueMultipleGroupPicker(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The default value for a multiple group picker custom field.
    """


    class MetaOapg:
        required = {
            "groupIds",
            "contextId",
            "type",
        }
        
        class properties:
            contextId = schemas.StrSchema
        
            @staticmethod
            def groupIds() -> typing.Type['CustomFieldContextDefaultValueMultipleGroupPickerGroupIds']:
                return CustomFieldContextDefaultValueMultipleGroupPickerGroupIds
            type = schemas.StrSchema
            __annotations__ = {
                "contextId": contextId,
                "groupIds": groupIds,
                "type": type,
            }
    
    groupIds: 'CustomFieldContextDefaultValueMultipleGroupPickerGroupIds'
    contextId: MetaOapg.properties.contextId
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextId"]) -> MetaOapg.properties.contextId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupIds"]) -> 'CustomFieldContextDefaultValueMultipleGroupPickerGroupIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contextId", "groupIds", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextId"]) -> MetaOapg.properties.contextId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupIds"]) -> 'CustomFieldContextDefaultValueMultipleGroupPickerGroupIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contextId", "groupIds", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        groupIds: 'CustomFieldContextDefaultValueMultipleGroupPickerGroupIds',
        contextId: typing.Union[MetaOapg.properties.contextId, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldContextDefaultValueMultipleGroupPicker':
        return super().__new__(
            cls,
            *args,
            groupIds=groupIds,
            contextId=contextId,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.custom_field_context_default_value_multiple_group_picker_group_ids import CustomFieldContextDefaultValueMultipleGroupPickerGroupIds