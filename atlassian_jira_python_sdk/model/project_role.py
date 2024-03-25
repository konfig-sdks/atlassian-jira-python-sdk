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


class ProjectRole(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about the roles in a project.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            
            
            class actors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RoleActor']:
                        return RoleActor
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['RoleActor'], typing.List['RoleActor']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RoleActor':
                    return super().__getitem__(i)
            admin = schemas.BoolSchema
            currentUserRole = schemas.BoolSchema
            default = schemas.BoolSchema
            id = schemas.Int64Schema
            name = schemas.StrSchema
            roleConfigurable = schemas.BoolSchema
        
            @staticmethod
            def scope() -> typing.Type['Scope']:
                return Scope
            _self = schemas.StrSchema
            translatedName = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "actors": actors,
                "admin": admin,
                "currentUserRole": currentUserRole,
                "default": default,
                "id": id,
                "name": name,
                "roleConfigurable": roleConfigurable,
                "scope": scope,
                "self": _self,
                "translatedName": translatedName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actors"]) -> MetaOapg.properties.actors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin"]) -> MetaOapg.properties.admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentUserRole"]) -> MetaOapg.properties.currentUserRole: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleConfigurable"]) -> MetaOapg.properties.roleConfigurable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'Scope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translatedName"]) -> MetaOapg.properties.translatedName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "actors", "admin", "currentUserRole", "default", "id", "name", "roleConfigurable", "scope", "self", "translatedName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actors"]) -> typing.Union[MetaOapg.properties.actors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin"]) -> typing.Union[MetaOapg.properties.admin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentUserRole"]) -> typing.Union[MetaOapg.properties.currentUserRole, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default"]) -> typing.Union[MetaOapg.properties.default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleConfigurable"]) -> typing.Union[MetaOapg.properties.roleConfigurable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union['Scope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translatedName"]) -> typing.Union[MetaOapg.properties.translatedName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "actors", "admin", "currentUserRole", "default", "id", "name", "roleConfigurable", "scope", "self", "translatedName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        actors: typing.Union[MetaOapg.properties.actors, list, tuple, schemas.Unset] = schemas.unset,
        admin: typing.Union[MetaOapg.properties.admin, bool, schemas.Unset] = schemas.unset,
        currentUserRole: typing.Union[MetaOapg.properties.currentUserRole, bool, schemas.Unset] = schemas.unset,
        default: typing.Union[MetaOapg.properties.default, bool, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        roleConfigurable: typing.Union[MetaOapg.properties.roleConfigurable, bool, schemas.Unset] = schemas.unset,
        scope: typing.Union['Scope', schemas.Unset] = schemas.unset,
        translatedName: typing.Union[MetaOapg.properties.translatedName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectRole':
        return super().__new__(
            cls,
            *args,
            description=description,
            actors=actors,
            admin=admin,
            currentUserRole=currentUserRole,
            default=default,
            id=id,
            name=name,
            roleConfigurable=roleConfigurable,
            scope=scope,
            translatedName=translatedName,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.role_actor import RoleActor
from atlassian_jira_python_sdk.model.scope import Scope
