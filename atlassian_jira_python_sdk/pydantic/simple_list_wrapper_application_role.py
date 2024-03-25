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

from atlassian_jira_python_sdk.pydantic.application_role import ApplicationRole

class SimpleListWrapperApplicationRole(BaseModel):
    callback: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='callback')

    items: typing.Optional[typing.List[ApplicationRole]] = Field(None, alias='items')

    max-results_: typing.Optional[int] = Field(None, alias='max-results')

    paging_callback: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='pagingCallback')

    size: typing.Optional[int] = Field(None, alias='size')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )