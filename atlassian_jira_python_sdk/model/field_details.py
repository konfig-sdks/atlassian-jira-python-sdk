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


class FieldDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a field.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def clauseNames() -> typing.Type['FieldDetailsClauseNames']:
                return FieldDetailsClauseNames
            custom = schemas.BoolSchema
            id = schemas.StrSchema
            key = schemas.StrSchema
            name = schemas.StrSchema
            navigable = schemas.BoolSchema
            orderable = schemas.BoolSchema
        
            @staticmethod
            def schema() -> typing.Type['JsonTypeBean']:
                return JsonTypeBean
        
            @staticmethod
            def scope() -> typing.Type['Scope']:
                return Scope
            searchable = schemas.BoolSchema
            __annotations__ = {
                "clauseNames": clauseNames,
                "custom": custom,
                "id": id,
                "key": key,
                "name": name,
                "navigable": navigable,
                "orderable": orderable,
                "schema": schema,
                "scope": scope,
                "searchable": searchable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clauseNames"]) -> 'FieldDetailsClauseNames': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> MetaOapg.properties.custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["navigable"]) -> MetaOapg.properties.navigable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderable"]) -> MetaOapg.properties.orderable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> 'JsonTypeBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'Scope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchable"]) -> MetaOapg.properties.searchable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clauseNames", "custom", "id", "key", "name", "navigable", "orderable", "schema", "scope", "searchable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clauseNames"]) -> typing.Union['FieldDetailsClauseNames', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["navigable"]) -> typing.Union[MetaOapg.properties.navigable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderable"]) -> typing.Union[MetaOapg.properties.orderable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> typing.Union['JsonTypeBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union['Scope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchable"]) -> typing.Union[MetaOapg.properties.searchable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clauseNames", "custom", "id", "key", "name", "navigable", "orderable", "schema", "scope", "searchable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        clauseNames: typing.Union['FieldDetailsClauseNames', schemas.Unset] = schemas.unset,
        custom: typing.Union[MetaOapg.properties.custom, bool, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        navigable: typing.Union[MetaOapg.properties.navigable, bool, schemas.Unset] = schemas.unset,
        orderable: typing.Union[MetaOapg.properties.orderable, bool, schemas.Unset] = schemas.unset,
        schema: typing.Union['JsonTypeBean', schemas.Unset] = schemas.unset,
        scope: typing.Union['Scope', schemas.Unset] = schemas.unset,
        searchable: typing.Union[MetaOapg.properties.searchable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldDetails':
        return super().__new__(
            cls,
            *args,
            clauseNames=clauseNames,
            custom=custom,
            id=id,
            key=key,
            name=name,
            navigable=navigable,
            orderable=orderable,
            schema=schema,
            scope=scope,
            searchable=searchable,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.field_details_clause_names import FieldDetailsClauseNames
from atlassian_jira_python_sdk.model.json_type_bean import JsonTypeBean
from atlassian_jira_python_sdk.model.scope import Scope
