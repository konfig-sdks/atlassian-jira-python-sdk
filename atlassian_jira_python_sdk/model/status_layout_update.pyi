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


class StatusLayoutUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The statuses associated with this workflow.
    """


    class MetaOapg:
        required = {
            "statusReference",
            "properties",
        }
        
        class properties:
        
            @staticmethod
            def properties() -> typing.Type['StatusLayoutUpdateProperties']:
                return StatusLayoutUpdateProperties
            statusReference = schemas.StrSchema
        
            @staticmethod
            def layout() -> typing.Type['WorkflowLayout']:
                return WorkflowLayout
            __annotations__ = {
                "properties": properties,
                "statusReference": statusReference,
                "layout": layout,
            }
        additional_properties = schemas.AnyTypeSchema
    
    statusReference: MetaOapg.properties.statusReference
    properties: 'StatusLayoutUpdateProperties'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusReference"]) -> MetaOapg.properties.statusReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'StatusLayoutUpdateProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layout"]) -> 'WorkflowLayout': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statusReference"], typing_extensions.Literal["properties"], typing_extensions.Literal["layout"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusReference"]) -> MetaOapg.properties.statusReference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> 'StatusLayoutUpdateProperties': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layout"]) -> typing.Union['WorkflowLayout', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statusReference"], typing_extensions.Literal["properties"], typing_extensions.Literal["layout"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        statusReference: typing.Union[MetaOapg.properties.statusReference, str, ],
        properties: 'StatusLayoutUpdateProperties',
        layout: typing.Union['WorkflowLayout', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'StatusLayoutUpdate':
        return super().__new__(
            cls,
            *args,
            statusReference=statusReference,
            properties=properties,
            layout=layout,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.status_layout_update_properties import StatusLayoutUpdateProperties
from atlassian_jira_python_sdk.model.workflow_layout import WorkflowLayout
