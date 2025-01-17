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


class IssueFilterForBulkPropertySet(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Bulk operation filter details.
    """


    class MetaOapg:
        
        class properties:
            currentValue = schemas.AnyTypeSchema
        
            @staticmethod
            def entityIds() -> typing.Type['IssueFilterForBulkPropertySetEntityIds']:
                return IssueFilterForBulkPropertySetEntityIds
            hasProperty = schemas.BoolSchema
            __annotations__ = {
                "currentValue": currentValue,
                "entityIds": entityIds,
                "hasProperty": hasProperty,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentValue"]) -> MetaOapg.properties.currentValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityIds"]) -> 'IssueFilterForBulkPropertySetEntityIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasProperty"]) -> MetaOapg.properties.hasProperty: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currentValue", "entityIds", "hasProperty", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentValue"]) -> typing.Union[MetaOapg.properties.currentValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityIds"]) -> typing.Union['IssueFilterForBulkPropertySetEntityIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasProperty"]) -> typing.Union[MetaOapg.properties.hasProperty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currentValue", "entityIds", "hasProperty", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        currentValue: typing.Union[MetaOapg.properties.currentValue, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        entityIds: typing.Union['IssueFilterForBulkPropertySetEntityIds', schemas.Unset] = schemas.unset,
        hasProperty: typing.Union[MetaOapg.properties.hasProperty, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueFilterForBulkPropertySet':
        return super().__new__(
            cls,
            *args,
            currentValue=currentValue,
            entityIds=entityIds,
            hasProperty=hasProperty,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_filter_for_bulk_property_set_entity_ids import IssueFilterForBulkPropertySetEntityIds
