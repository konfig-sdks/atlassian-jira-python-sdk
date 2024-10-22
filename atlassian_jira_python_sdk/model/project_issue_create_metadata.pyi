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


class ProjectIssueCreateMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the issue creation metadata for a project.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def avatarUrls() -> typing.Type['AvatarUrlsBean']:
                return AvatarUrlsBean
            expand = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class issuetypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IssueTypeIssueCreateMetadata']:
                        return IssueTypeIssueCreateMetadata
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IssueTypeIssueCreateMetadata'], typing.List['IssueTypeIssueCreateMetadata']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'issuetypes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IssueTypeIssueCreateMetadata':
                    return super().__getitem__(i)
            key = schemas.StrSchema
            name = schemas.StrSchema
            _self = schemas.StrSchema
            __annotations__ = {
                "avatarUrls": avatarUrls,
                "expand": expand,
                "id": id,
                "issuetypes": issuetypes,
                "key": key,
                "name": name,
                "self": _self,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatarUrls"]) -> 'AvatarUrlsBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expand"]) -> MetaOapg.properties.expand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuetypes"]) -> MetaOapg.properties.issuetypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatarUrls", "expand", "id", "issuetypes", "key", "name", "self", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatarUrls"]) -> typing.Union['AvatarUrlsBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expand"]) -> typing.Union[MetaOapg.properties.expand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuetypes"]) -> typing.Union[MetaOapg.properties.issuetypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatarUrls", "expand", "id", "issuetypes", "key", "name", "self", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        avatarUrls: typing.Union['AvatarUrlsBean', schemas.Unset] = schemas.unset,
        expand: typing.Union[MetaOapg.properties.expand, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        issuetypes: typing.Union[MetaOapg.properties.issuetypes, list, tuple, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectIssueCreateMetadata':
        return super().__new__(
            cls,
            *args,
            avatarUrls=avatarUrls,
            expand=expand,
            id=id,
            issuetypes=issuetypes,
            key=key,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.avatar_urls_bean import AvatarUrlsBean
from atlassian_jira_python_sdk.model.issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata
