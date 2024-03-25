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


class MultipleCustomFieldValuesUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A custom field and its new value with a list of issue to update.
    """


    class MetaOapg:
        required = {
            "issueIds",
            "value",
            "customField",
        }
        
        class properties:
            customField = schemas.StrSchema
        
            @staticmethod
            def issueIds() -> typing.Type['MultipleCustomFieldValuesUpdateIssueIds']:
                return MultipleCustomFieldValuesUpdateIssueIds
            value = schemas.AnyTypeSchema
            __annotations__ = {
                "customField": customField,
                "issueIds": issueIds,
                "value": value,
            }
    
    issueIds: 'MultipleCustomFieldValuesUpdateIssueIds'
    value: MetaOapg.properties.value
    customField: MetaOapg.properties.customField
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customField"]) -> MetaOapg.properties.customField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueIds"]) -> 'MultipleCustomFieldValuesUpdateIssueIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customField", "issueIds", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customField"]) -> MetaOapg.properties.customField: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueIds"]) -> 'MultipleCustomFieldValuesUpdateIssueIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customField", "issueIds", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        issueIds: 'MultipleCustomFieldValuesUpdateIssueIds',
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        customField: typing.Union[MetaOapg.properties.customField, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MultipleCustomFieldValuesUpdate':
        return super().__new__(
            cls,
            *args,
            issueIds=issueIds,
            value=value,
            customField=customField,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.multiple_custom_field_values_update_issue_ids import MultipleCustomFieldValuesUpdateIssueIds
