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


class Dashboard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a dashboard.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            automaticRefreshMs = schemas.Int32Schema
            
            
            class editPermissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SharePermission']:
                        return SharePermission
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SharePermission'], typing.List['SharePermission']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'editPermissions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SharePermission':
                    return super().__getitem__(i)
            id = schemas.StrSchema
            isFavourite = schemas.BoolSchema
            isWritable = schemas.BoolSchema
            name = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['UserBean']:
                return UserBean
            popularity = schemas.Int64Schema
            rank = schemas.Int32Schema
            _self = schemas.StrSchema
            
            
            class sharePermissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SharePermission']:
                        return SharePermission
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SharePermission'], typing.List['SharePermission']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sharePermissions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SharePermission':
                    return super().__getitem__(i)
            systemDashboard = schemas.BoolSchema
            view = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "automaticRefreshMs": automaticRefreshMs,
                "editPermissions": editPermissions,
                "id": id,
                "isFavourite": isFavourite,
                "isWritable": isWritable,
                "name": name,
                "owner": owner,
                "popularity": popularity,
                "rank": rank,
                "self": _self,
                "sharePermissions": sharePermissions,
                "systemDashboard": systemDashboard,
                "view": view,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automaticRefreshMs"]) -> MetaOapg.properties.automaticRefreshMs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editPermissions"]) -> MetaOapg.properties.editPermissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFavourite"]) -> MetaOapg.properties.isFavourite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isWritable"]) -> MetaOapg.properties.isWritable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'UserBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["popularity"]) -> MetaOapg.properties.popularity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sharePermissions"]) -> MetaOapg.properties.sharePermissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemDashboard"]) -> MetaOapg.properties.systemDashboard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "automaticRefreshMs", "editPermissions", "id", "isFavourite", "isWritable", "name", "owner", "popularity", "rank", "self", "sharePermissions", "systemDashboard", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automaticRefreshMs"]) -> typing.Union[MetaOapg.properties.automaticRefreshMs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editPermissions"]) -> typing.Union[MetaOapg.properties.editPermissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFavourite"]) -> typing.Union[MetaOapg.properties.isFavourite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isWritable"]) -> typing.Union[MetaOapg.properties.isWritable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['UserBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["popularity"]) -> typing.Union[MetaOapg.properties.popularity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> typing.Union[MetaOapg.properties.rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sharePermissions"]) -> typing.Union[MetaOapg.properties.sharePermissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemDashboard"]) -> typing.Union[MetaOapg.properties.systemDashboard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union[MetaOapg.properties.view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "automaticRefreshMs", "editPermissions", "id", "isFavourite", "isWritable", "name", "owner", "popularity", "rank", "self", "sharePermissions", "systemDashboard", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        automaticRefreshMs: typing.Union[MetaOapg.properties.automaticRefreshMs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        editPermissions: typing.Union[MetaOapg.properties.editPermissions, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        isFavourite: typing.Union[MetaOapg.properties.isFavourite, bool, schemas.Unset] = schemas.unset,
        isWritable: typing.Union[MetaOapg.properties.isWritable, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['UserBean', schemas.Unset] = schemas.unset,
        popularity: typing.Union[MetaOapg.properties.popularity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rank: typing.Union[MetaOapg.properties.rank, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sharePermissions: typing.Union[MetaOapg.properties.sharePermissions, list, tuple, schemas.Unset] = schemas.unset,
        systemDashboard: typing.Union[MetaOapg.properties.systemDashboard, bool, schemas.Unset] = schemas.unset,
        view: typing.Union[MetaOapg.properties.view, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Dashboard':
        return super().__new__(
            cls,
            *args,
            description=description,
            automaticRefreshMs=automaticRefreshMs,
            editPermissions=editPermissions,
            id=id,
            isFavourite=isFavourite,
            isWritable=isWritable,
            name=name,
            owner=owner,
            popularity=popularity,
            rank=rank,
            sharePermissions=sharePermissions,
            systemDashboard=systemDashboard,
            view=view,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.share_permission import SharePermission
from atlassian_jira_python_sdk.model.user_bean import UserBean