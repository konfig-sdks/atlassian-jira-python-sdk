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


class IssueTypeWithStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Status details for an issue type.
    """


    class MetaOapg:
        required = {
            "name",
            "self",
            "statuses",
            "id",
            "subtask",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            _self = schemas.StrSchema
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatusDetails']:
                        return StatusDetails
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatusDetails'], typing.List['StatusDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatusDetails':
                    return super().__getitem__(i)
            subtask = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "self": _self,
                "statuses": statuses,
                "subtask": subtask,
            }
    
    name: MetaOapg.properties.name
    statuses: MetaOapg.properties.statuses
    id: MetaOapg.properties.id
    subtask: MetaOapg.properties.subtask
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtask"]) -> MetaOapg.properties.subtask: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "self", "statuses", "subtask", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtask"]) -> MetaOapg.properties.subtask: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "self", "statuses", "subtask", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        subtask: typing.Union[MetaOapg.properties.subtask, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueTypeWithStatus':
        return super().__new__(
            cls,
            *args,
            name=name,
            statuses=statuses,
            id=id,
            subtask=subtask,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.status_details import StatusDetails
