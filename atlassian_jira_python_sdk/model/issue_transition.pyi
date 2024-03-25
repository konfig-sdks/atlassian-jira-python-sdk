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


class IssueTransition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an issue transition.
    """


    class MetaOapg:
        
        class properties:
            expand = schemas.StrSchema
        
            @staticmethod
            def fields() -> typing.Type['IssueTransitionFields']:
                return IssueTransitionFields
            hasScreen = schemas.BoolSchema
            id = schemas.StrSchema
            isAvailable = schemas.BoolSchema
            isConditional = schemas.BoolSchema
            isGlobal = schemas.BoolSchema
            isInitial = schemas.BoolSchema
            looped = schemas.BoolSchema
            name = schemas.StrSchema
        
            @staticmethod
            def to() -> typing.Type['StatusDetails']:
                return StatusDetails
            __annotations__ = {
                "expand": expand,
                "fields": fields,
                "hasScreen": hasScreen,
                "id": id,
                "isAvailable": isAvailable,
                "isConditional": isConditional,
                "isGlobal": isGlobal,
                "isInitial": isInitial,
                "looped": looped,
                "name": name,
                "to": to,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expand"]) -> MetaOapg.properties.expand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'IssueTransitionFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasScreen"]) -> MetaOapg.properties.hasScreen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAvailable"]) -> MetaOapg.properties.isAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isConditional"]) -> MetaOapg.properties.isConditional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isGlobal"]) -> MetaOapg.properties.isGlobal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInitial"]) -> MetaOapg.properties.isInitial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["looped"]) -> MetaOapg.properties.looped: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> 'StatusDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expand"], typing_extensions.Literal["fields"], typing_extensions.Literal["hasScreen"], typing_extensions.Literal["id"], typing_extensions.Literal["isAvailable"], typing_extensions.Literal["isConditional"], typing_extensions.Literal["isGlobal"], typing_extensions.Literal["isInitial"], typing_extensions.Literal["looped"], typing_extensions.Literal["name"], typing_extensions.Literal["to"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expand"]) -> typing.Union[MetaOapg.properties.expand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['IssueTransitionFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasScreen"]) -> typing.Union[MetaOapg.properties.hasScreen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAvailable"]) -> typing.Union[MetaOapg.properties.isAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isConditional"]) -> typing.Union[MetaOapg.properties.isConditional, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isGlobal"]) -> typing.Union[MetaOapg.properties.isGlobal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInitial"]) -> typing.Union[MetaOapg.properties.isInitial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["looped"]) -> typing.Union[MetaOapg.properties.looped, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union['StatusDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expand"], typing_extensions.Literal["fields"], typing_extensions.Literal["hasScreen"], typing_extensions.Literal["id"], typing_extensions.Literal["isAvailable"], typing_extensions.Literal["isConditional"], typing_extensions.Literal["isGlobal"], typing_extensions.Literal["isInitial"], typing_extensions.Literal["looped"], typing_extensions.Literal["name"], typing_extensions.Literal["to"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        expand: typing.Union[MetaOapg.properties.expand, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['IssueTransitionFields', schemas.Unset] = schemas.unset,
        hasScreen: typing.Union[MetaOapg.properties.hasScreen, bool, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        isAvailable: typing.Union[MetaOapg.properties.isAvailable, bool, schemas.Unset] = schemas.unset,
        isConditional: typing.Union[MetaOapg.properties.isConditional, bool, schemas.Unset] = schemas.unset,
        isGlobal: typing.Union[MetaOapg.properties.isGlobal, bool, schemas.Unset] = schemas.unset,
        isInitial: typing.Union[MetaOapg.properties.isInitial, bool, schemas.Unset] = schemas.unset,
        looped: typing.Union[MetaOapg.properties.looped, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        to: typing.Union['StatusDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'IssueTransition':
        return super().__new__(
            cls,
            *args,
            expand=expand,
            fields=fields,
            hasScreen=hasScreen,
            id=id,
            isAvailable=isAvailable,
            isConditional=isConditional,
            isGlobal=isGlobal,
            isInitial=isInitial,
            looped=looped,
            name=name,
            to=to,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_transition_fields import IssueTransitionFields
from atlassian_jira_python_sdk.model.status_details import StatusDetails
