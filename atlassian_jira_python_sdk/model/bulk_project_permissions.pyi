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


class BulkProjectPermissions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of project permissions and associated issues and projects to look up.
    """


    class MetaOapg:
        required = {
            "permissions",
        }
        
        class properties:
        
            @staticmethod
            def permissions() -> typing.Type['BulkProjectPermissionsPermissions']:
                return BulkProjectPermissionsPermissions
        
            @staticmethod
            def issues() -> typing.Type['BulkProjectPermissionsIssues']:
                return BulkProjectPermissionsIssues
        
            @staticmethod
            def projects() -> typing.Type['BulkProjectPermissionsProjects']:
                return BulkProjectPermissionsProjects
            __annotations__ = {
                "permissions": permissions,
                "issues": issues,
                "projects": projects,
            }
    
    permissions: 'BulkProjectPermissionsPermissions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'BulkProjectPermissionsPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues"]) -> 'BulkProjectPermissionsIssues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projects"]) -> 'BulkProjectPermissionsProjects': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["permissions", "issues", "projects", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> 'BulkProjectPermissionsPermissions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues"]) -> typing.Union['BulkProjectPermissionsIssues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projects"]) -> typing.Union['BulkProjectPermissionsProjects', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["permissions", "issues", "projects", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        permissions: 'BulkProjectPermissionsPermissions',
        issues: typing.Union['BulkProjectPermissionsIssues', schemas.Unset] = schemas.unset,
        projects: typing.Union['BulkProjectPermissionsProjects', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkProjectPermissions':
        return super().__new__(
            cls,
            *args,
            permissions=permissions,
            issues=issues,
            projects=projects,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.bulk_project_permissions_issues import BulkProjectPermissionsIssues
from atlassian_jira_python_sdk.model.bulk_project_permissions_permissions import BulkProjectPermissionsPermissions
from atlassian_jira_python_sdk.model.bulk_project_permissions_projects import BulkProjectPermissionsProjects
