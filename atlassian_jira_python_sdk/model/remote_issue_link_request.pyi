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


class RemoteIssueLinkRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a remote issue link.
    """


    class MetaOapg:
        required = {
            "object",
        }
        
        class properties:
        
            @staticmethod
            def object() -> typing.Type['RemoteObject']:
                return RemoteObject
        
            @staticmethod
            def application() -> typing.Type['Application']:
                return Application
            globalId = schemas.StrSchema
            relationship = schemas.StrSchema
            __annotations__ = {
                "object": object,
                "application": application,
                "globalId": globalId,
                "relationship": relationship,
            }
        additional_properties = schemas.AnyTypeSchema
    
    object: 'RemoteObject'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> 'RemoteObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["application"]) -> 'Application': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["globalId"]) -> MetaOapg.properties.globalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object"], typing_extensions.Literal["application"], typing_extensions.Literal["globalId"], typing_extensions.Literal["relationship"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> 'RemoteObject': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application"]) -> typing.Union['Application', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["globalId"]) -> typing.Union[MetaOapg.properties.globalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationship"]) -> typing.Union[MetaOapg.properties.relationship, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object"], typing_extensions.Literal["application"], typing_extensions.Literal["globalId"], typing_extensions.Literal["relationship"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        object: 'RemoteObject',
        application: typing.Union['Application', schemas.Unset] = schemas.unset,
        globalId: typing.Union[MetaOapg.properties.globalId, str, schemas.Unset] = schemas.unset,
        relationship: typing.Union[MetaOapg.properties.relationship, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'RemoteIssueLinkRequest':
        return super().__new__(
            cls,
            *args,
            object=object,
            application=application,
            globalId=globalId,
            relationship=relationship,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.application import Application
from atlassian_jira_python_sdk.model.remote_object import RemoteObject