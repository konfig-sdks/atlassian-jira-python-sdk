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


class Fields(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Key fields from the linked issue.
    """


    class MetaOapg:
        
        class properties:
            summary = schemas.StrSchema
        
            @staticmethod
            def assignee() -> typing.Type['UserDetails']:
                return UserDetails
        
            @staticmethod
            def issueType() -> typing.Type['IssueTypeDetails']:
                return IssueTypeDetails
        
            @staticmethod
            def issuetype() -> typing.Type['IssueTypeDetails']:
                return IssueTypeDetails
        
            @staticmethod
            def priority() -> typing.Type['Priority']:
                return Priority
        
            @staticmethod
            def status() -> typing.Type['StatusDetails']:
                return StatusDetails
        
            @staticmethod
            def timetracking() -> typing.Type['TimeTrackingDetails']:
                return TimeTrackingDetails
            __annotations__ = {
                "summary": summary,
                "assignee": assignee,
                "issueType": issueType,
                "issuetype": issuetype,
                "priority": priority,
                "status": status,
                "timetracking": timetracking,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> 'UserDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueType"]) -> 'IssueTypeDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuetype"]) -> 'IssueTypeDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> 'Priority': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'StatusDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timetracking"]) -> 'TimeTrackingDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "assignee", "issueType", "issuetype", "priority", "status", "timetracking", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union['UserDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueType"]) -> typing.Union['IssueTypeDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuetype"]) -> typing.Union['IssueTypeDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union['Priority', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['StatusDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timetracking"]) -> typing.Union['TimeTrackingDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "assignee", "issueType", "issuetype", "priority", "status", "timetracking", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        assignee: typing.Union['UserDetails', schemas.Unset] = schemas.unset,
        issueType: typing.Union['IssueTypeDetails', schemas.Unset] = schemas.unset,
        issuetype: typing.Union['IssueTypeDetails', schemas.Unset] = schemas.unset,
        priority: typing.Union['Priority', schemas.Unset] = schemas.unset,
        status: typing.Union['StatusDetails', schemas.Unset] = schemas.unset,
        timetracking: typing.Union['TimeTrackingDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Fields':
        return super().__new__(
            cls,
            *args,
            summary=summary,
            assignee=assignee,
            issueType=issueType,
            issuetype=issuetype,
            priority=priority,
            status=status,
            timetracking=timetracking,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.issue_type_details import IssueTypeDetails
from atlassian_jira_python_sdk.model.priority import Priority
from atlassian_jira_python_sdk.model.status_details import StatusDetails
from atlassian_jira_python_sdk.model.time_tracking_details import TimeTrackingDetails
from atlassian_jira_python_sdk.model.user_details import UserDetails