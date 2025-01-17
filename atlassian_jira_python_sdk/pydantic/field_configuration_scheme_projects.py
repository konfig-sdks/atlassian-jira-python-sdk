# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from atlassian_jira_python_sdk.pydantic.field_configuration_scheme import FieldConfigurationScheme
from atlassian_jira_python_sdk.pydantic.field_configuration_scheme_projects_project_ids import FieldConfigurationSchemeProjectsProjectIds

class FieldConfigurationSchemeProjects(BaseModel):
    project_ids: FieldConfigurationSchemeProjectsProjectIds = Field(alias='projectIds')

    field_configuration_scheme: typing.Optional[FieldConfigurationScheme] = Field(None, alias='fieldConfigurationScheme')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
