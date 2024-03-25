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

from atlassian_jira_python_sdk.pydantic.search_request_bean_expand import SearchRequestBeanExpand
from atlassian_jira_python_sdk.pydantic.search_request_bean_fields import SearchRequestBeanFields
from atlassian_jira_python_sdk.pydantic.search_request_bean_properties import SearchRequestBeanProperties

class SearchRequestBean(BaseModel):
    expand: typing.Optional[SearchRequestBeanExpand] = Field(None, alias='expand')

    fields: typing.Optional[SearchRequestBeanFields] = Field(None, alias='fields')

    # Reference fields by their key (rather than ID). The default is `false`.
    fields_by_keys: typing.Optional[bool] = Field(None, alias='fieldsByKeys')

    # A [JQL](https://confluence.atlassian.com/x/egORLQ) expression.
    jql: typing.Optional[str] = Field(None, alias='jql')

    # The maximum number of items to return per page.
    max_results: typing.Optional[int] = Field(None, alias='maxResults')

    properties: typing.Optional[SearchRequestBeanProperties] = Field(None, alias='properties')

    # The index of the first item to return in the page of results (page offset). The base index is `0`.
    start_at: typing.Optional[int] = Field(None, alias='startAt')

    # Determines how to validate the JQL query and treat the validation results. Supported values:   *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).  *  `warn` Returns all errors as warnings.  *  `none` No validation is performed.  *  `true` *Deprecated* A legacy synonym for `strict`.  *  `false` *Deprecated* A legacy synonym for `warn`.  The default is `strict`.  Note: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery` value.
    validate_query: typing.Optional[Literal["strict", "warn", "none", "true", "false"]] = Field(None, alias='validateQuery')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )