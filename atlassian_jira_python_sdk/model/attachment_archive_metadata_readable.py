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


class AttachmentArchiveMetadataReadable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Metadata for an archive (for example a zip) and its contents.
    """


    class MetaOapg:
        
        class properties:
            
            
            class entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AttachmentArchiveItemReadable']:
                        return AttachmentArchiveItemReadable
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AttachmentArchiveItemReadable'], typing.List['AttachmentArchiveItemReadable']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AttachmentArchiveItemReadable':
                    return super().__getitem__(i)
            id = schemas.Int64Schema
            mediaType = schemas.StrSchema
            name = schemas.StrSchema
            totalEntryCount = schemas.Int64Schema
            __annotations__ = {
                "entries": entries,
                "id": id,
                "mediaType": mediaType,
                "name": name,
                "totalEntryCount": totalEntryCount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mediaType"]) -> MetaOapg.properties.mediaType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEntryCount"]) -> MetaOapg.properties.totalEntryCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["entries", "id", "mediaType", "name", "totalEntryCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entries"]) -> typing.Union[MetaOapg.properties.entries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mediaType"]) -> typing.Union[MetaOapg.properties.mediaType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEntryCount"]) -> typing.Union[MetaOapg.properties.totalEntryCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["entries", "id", "mediaType", "name", "totalEntryCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entries: typing.Union[MetaOapg.properties.entries, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mediaType: typing.Union[MetaOapg.properties.mediaType, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        totalEntryCount: typing.Union[MetaOapg.properties.totalEntryCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttachmentArchiveMetadataReadable':
        return super().__new__(
            cls,
            *args,
            entries=entries,
            id=id,
            mediaType=mediaType,
            name=name,
            totalEntryCount=totalEntryCount,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.attachment_archive_item_readable import AttachmentArchiveItemReadable
