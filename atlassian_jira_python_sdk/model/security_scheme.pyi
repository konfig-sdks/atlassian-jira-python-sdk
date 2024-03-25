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


class SecurityScheme(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a security scheme.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            defaultSecurityLevelId = schemas.Int64Schema
            id = schemas.Int64Schema
            
            
            class levels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SecurityLevel']:
                        return SecurityLevel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SecurityLevel'], typing.List['SecurityLevel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'levels':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SecurityLevel':
                    return super().__getitem__(i)
            name = schemas.StrSchema
            _self = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "defaultSecurityLevelId": defaultSecurityLevelId,
                "id": id,
                "levels": levels,
                "name": name,
                "self": _self,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultSecurityLevelId"]) -> MetaOapg.properties.defaultSecurityLevelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["levels"]) -> MetaOapg.properties.levels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "defaultSecurityLevelId", "id", "levels", "name", "self", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultSecurityLevelId"]) -> typing.Union[MetaOapg.properties.defaultSecurityLevelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["levels"]) -> typing.Union[MetaOapg.properties.levels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "defaultSecurityLevelId", "id", "levels", "name", "self", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        defaultSecurityLevelId: typing.Union[MetaOapg.properties.defaultSecurityLevelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        levels: typing.Union[MetaOapg.properties.levels, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SecurityScheme':
        return super().__new__(
            cls,
            *args,
            description=description,
            defaultSecurityLevelId=defaultSecurityLevelId,
            id=id,
            levels=levels,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.security_level import SecurityLevel