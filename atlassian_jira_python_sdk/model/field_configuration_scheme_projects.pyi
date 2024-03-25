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


class FieldConfigurationSchemeProjects(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Project list with assigned field configuration schema.
    """


    class MetaOapg:
        required = {
            "projectIds",
        }
        
        class properties:
        
            @staticmethod
            def projectIds() -> typing.Type['FieldConfigurationSchemeProjectsProjectIds']:
                return FieldConfigurationSchemeProjectsProjectIds
        
            @staticmethod
            def fieldConfigurationScheme() -> typing.Type['FieldConfigurationScheme']:
                return FieldConfigurationScheme
            __annotations__ = {
                "projectIds": projectIds,
                "fieldConfigurationScheme": fieldConfigurationScheme,
            }
    
    projectIds: 'FieldConfigurationSchemeProjectsProjectIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectIds"]) -> 'FieldConfigurationSchemeProjectsProjectIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldConfigurationScheme"]) -> 'FieldConfigurationScheme': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["projectIds", "fieldConfigurationScheme", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectIds"]) -> 'FieldConfigurationSchemeProjectsProjectIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldConfigurationScheme"]) -> typing.Union['FieldConfigurationScheme', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["projectIds", "fieldConfigurationScheme", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        projectIds: 'FieldConfigurationSchemeProjectsProjectIds',
        fieldConfigurationScheme: typing.Union['FieldConfigurationScheme', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldConfigurationSchemeProjects':
        return super().__new__(
            cls,
            *args,
            projectIds=projectIds,
            fieldConfigurationScheme=fieldConfigurationScheme,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.field_configuration_scheme import FieldConfigurationScheme
from atlassian_jira_python_sdk.model.field_configuration_scheme_projects_project_ids import FieldConfigurationSchemeProjectsProjectIds
