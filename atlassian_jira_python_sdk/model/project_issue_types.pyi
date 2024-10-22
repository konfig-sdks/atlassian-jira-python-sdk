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


class ProjectIssueTypes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Use the optional `workflows.usages` expand to get additional information about the projects and issue types associated with the requested workflows.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def issueTypes() -> typing.Type['ProjectIssueTypesIssueTypes']:
                return ProjectIssueTypesIssueTypes
        
            @staticmethod
            def project() -> typing.Type['ProjectId']:
                return ProjectId
            __annotations__ = {
                "issueTypes": issueTypes,
                "project": project,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueTypes"]) -> 'ProjectIssueTypesIssueTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> 'ProjectId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["issueTypes", "project", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueTypes"]) -> typing.Union['ProjectIssueTypesIssueTypes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union['ProjectId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["issueTypes", "project", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        issueTypes: typing.Union['ProjectIssueTypesIssueTypes', schemas.Unset] = schemas.unset,
        project: typing.Union['ProjectId', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectIssueTypes':
        return super().__new__(
            cls,
            *args,
            issueTypes=issueTypes,
            project=project,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.project_id import ProjectId
from atlassian_jira_python_sdk.model.project_issue_types_issue_types import ProjectIssueTypesIssueTypes
