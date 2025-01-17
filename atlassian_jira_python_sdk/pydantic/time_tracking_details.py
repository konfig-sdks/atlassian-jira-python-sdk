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


class TimeTrackingDetails(BaseModel):
    # The original estimate of time needed for this issue in readable format.
    original_estimate: typing.Optional[str] = Field(None, alias='originalEstimate')

    # The original estimate of time needed for this issue in seconds.
    original_estimate_seconds: typing.Optional[int] = Field(None, alias='originalEstimateSeconds')

    # The remaining estimate of time needed for this issue in readable format.
    remaining_estimate: typing.Optional[str] = Field(None, alias='remainingEstimate')

    # The remaining estimate of time needed for this issue in seconds.
    remaining_estimate_seconds: typing.Optional[int] = Field(None, alias='remainingEstimateSeconds')

    # Time worked on this issue in readable format.
    time_spent: typing.Optional[str] = Field(None, alias='timeSpent')

    # Time worked on this issue in seconds.
    time_spent_seconds: typing.Optional[int] = Field(None, alias='timeSpentSeconds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
