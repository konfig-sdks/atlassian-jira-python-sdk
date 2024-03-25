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


class WorkflowStatusUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the status being updated.
    """


    class MetaOapg:
        required = {
            "name",
            "statusCategory",
            "statusReference",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class statusCategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TODO(cls):
                    return cls("TODO")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("IN_PROGRESS")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")
            statusReference = schemas.StrSchema
            description = schemas.StrSchema
            id = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "statusCategory": statusCategory,
                "statusReference": statusReference,
                "description": description,
                "id": id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    name: MetaOapg.properties.name
    statusCategory: MetaOapg.properties.statusCategory
    statusReference: MetaOapg.properties.statusReference
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusCategory"]) -> MetaOapg.properties.statusCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusReference"]) -> MetaOapg.properties.statusReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["statusCategory"], typing_extensions.Literal["statusReference"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusCategory"]) -> MetaOapg.properties.statusCategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusReference"]) -> MetaOapg.properties.statusReference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["statusCategory"], typing_extensions.Literal["statusReference"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        statusCategory: typing.Union[MetaOapg.properties.statusCategory, str, ],
        statusReference: typing.Union[MetaOapg.properties.statusReference, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WorkflowStatusUpdate':
        return super().__new__(
            cls,
            *args,
            name=name,
            statusCategory=statusCategory,
            statusReference=statusReference,
            description=description,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )