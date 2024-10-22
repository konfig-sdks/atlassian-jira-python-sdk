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


class IssueTypeIssueCreateMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the issue creation metadata for an issue type.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            avatarId = schemas.Int64Schema
            entityId = schemas.UUIDSchema
            expand = schemas.StrSchema
        
            @staticmethod
            def fields() -> typing.Type['IssueTypeIssueCreateMetadataFields']:
                return IssueTypeIssueCreateMetadataFields
            hierarchyLevel = schemas.Int32Schema
            iconUrl = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def scope() -> typing.Type['Scope']:
                return Scope
            _self = schemas.StrSchema
            subtask = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "avatarId": avatarId,
                "entityId": entityId,
                "expand": expand,
                "fields": fields,
                "hierarchyLevel": hierarchyLevel,
                "iconUrl": iconUrl,
                "id": id,
                "name": name,
                "scope": scope,
                "self": _self,
                "subtask": subtask,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatarId"]) -> MetaOapg.properties.avatarId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expand"]) -> MetaOapg.properties.expand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'IssueTypeIssueCreateMetadataFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hierarchyLevel"]) -> MetaOapg.properties.hierarchyLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconUrl"]) -> MetaOapg.properties.iconUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'Scope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtask"]) -> MetaOapg.properties.subtask: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "avatarId", "entityId", "expand", "fields", "hierarchyLevel", "iconUrl", "id", "name", "scope", "self", "subtask", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatarId"]) -> typing.Union[MetaOapg.properties.avatarId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> typing.Union[MetaOapg.properties.entityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expand"]) -> typing.Union[MetaOapg.properties.expand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['IssueTypeIssueCreateMetadataFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hierarchyLevel"]) -> typing.Union[MetaOapg.properties.hierarchyLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconUrl"]) -> typing.Union[MetaOapg.properties.iconUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union['Scope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtask"]) -> typing.Union[MetaOapg.properties.subtask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "avatarId", "entityId", "expand", "fields", "hierarchyLevel", "iconUrl", "id", "name", "scope", "self", "subtask", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        avatarId: typing.Union[MetaOapg.properties.avatarId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        entityId: typing.Union[MetaOapg.properties.entityId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        expand: typing.Union[MetaOapg.properties.expand, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['IssueTypeIssueCreateMetadataFields', schemas.Unset] = schemas.unset,
        hierarchyLevel: typing.Union[MetaOapg.properties.hierarchyLevel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        iconUrl: typing.Union[MetaOapg.properties.iconUrl, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        scope: typing.Union['Scope', schemas.Unset] = schemas.unset,
        subtask: typing.Union[MetaOapg.properties.subtask, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueTypeIssueCreateMetadata':
        return super().__new__(
            cls,
            *args,
            description=description,
            avatarId=avatarId,
            entityId=entityId,
            expand=expand,
            fields=fields,
            hierarchyLevel=hierarchyLevel,
            iconUrl=iconUrl,
            id=id,
            name=name,
            scope=scope,
            subtask=subtask,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_type_issue_create_metadata_fields import IssueTypeIssueCreateMetadataFields
from atlassian_jira_python_sdk.model.scope import Scope
