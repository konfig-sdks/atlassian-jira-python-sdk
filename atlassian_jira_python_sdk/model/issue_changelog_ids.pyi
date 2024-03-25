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


class IssueChangelogIds(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of changelog IDs.
    """


    class MetaOapg:
        required = {
            "changelogIds",
        }
        
        class properties:
        
            @staticmethod
            def changelogIds() -> typing.Type['IssueChangelogIdsChangelogIds']:
                return IssueChangelogIdsChangelogIds
            __annotations__ = {
                "changelogIds": changelogIds,
            }
    
    changelogIds: 'IssueChangelogIdsChangelogIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changelogIds"]) -> 'IssueChangelogIdsChangelogIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["changelogIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changelogIds"]) -> 'IssueChangelogIdsChangelogIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["changelogIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        changelogIds: 'IssueChangelogIdsChangelogIds',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueChangelogIds':
        return super().__new__(
            cls,
            *args,
            changelogIds=changelogIds,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_changelog_ids_changelog_ids import IssueChangelogIdsChangelogIds
