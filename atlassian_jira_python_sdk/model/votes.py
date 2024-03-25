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


class Votes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of votes on an issue.
    """


    class MetaOapg:
        
        class properties:
            hasVoted = schemas.BoolSchema
            _self = schemas.StrSchema
            
            
            class voters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'voters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            votes = schemas.Int64Schema
            __annotations__ = {
                "hasVoted": hasVoted,
                "self": _self,
                "voters": voters,
                "votes": votes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasVoted"]) -> MetaOapg.properties.hasVoted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voters"]) -> MetaOapg.properties.voters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["votes"]) -> MetaOapg.properties.votes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hasVoted", "self", "voters", "votes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasVoted"]) -> typing.Union[MetaOapg.properties.hasVoted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voters"]) -> typing.Union[MetaOapg.properties.voters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["votes"]) -> typing.Union[MetaOapg.properties.votes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hasVoted", "self", "voters", "votes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hasVoted: typing.Union[MetaOapg.properties.hasVoted, bool, schemas.Unset] = schemas.unset,
        voters: typing.Union[MetaOapg.properties.voters, list, tuple, schemas.Unset] = schemas.unset,
        votes: typing.Union[MetaOapg.properties.votes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Votes':
        return super().__new__(
            cls,
            *args,
            hasVoted=hasVoted,
            voters=voters,
            votes=votes,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.user import User
