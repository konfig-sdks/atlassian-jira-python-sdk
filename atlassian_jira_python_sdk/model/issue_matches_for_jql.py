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


class IssueMatchesForJQL(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of the issues matched to a JQL query or details of errors encountered during matching.
    """


    class MetaOapg:
        required = {
            "errors",
            "matchedIssues",
        }
        
        class properties:
        
            @staticmethod
            def errors() -> typing.Type['IssueMatchesForJQLErrors']:
                return IssueMatchesForJQLErrors
        
            @staticmethod
            def matchedIssues() -> typing.Type['IssueMatchesForJQLMatchedIssues']:
                return IssueMatchesForJQLMatchedIssues
            __annotations__ = {
                "errors": errors,
                "matchedIssues": matchedIssues,
            }
    
    errors: 'IssueMatchesForJQLErrors'
    matchedIssues: 'IssueMatchesForJQLMatchedIssues'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'IssueMatchesForJQLErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchedIssues"]) -> 'IssueMatchesForJQLMatchedIssues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "matchedIssues", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'IssueMatchesForJQLErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchedIssues"]) -> 'IssueMatchesForJQLMatchedIssues': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "matchedIssues", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        errors: 'IssueMatchesForJQLErrors',
        matchedIssues: 'IssueMatchesForJQLMatchedIssues',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueMatchesForJQL':
        return super().__new__(
            cls,
            *args,
            errors=errors,
            matchedIssues=matchedIssues,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_matches_for_jql_errors import IssueMatchesForJQLErrors
from atlassian_jira_python_sdk.model.issue_matches_for_jql_matched_issues import IssueMatchesForJQLMatchedIssues