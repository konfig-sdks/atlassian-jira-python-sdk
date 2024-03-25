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


class RequiredAvailableDashboardGadget(TypedDict):
    # The title of the gadget.
    title: str

class OptionalAvailableDashboardGadget(TypedDict, total=False):
    # The module key of the gadget type.
    moduleKey: str

    # The URI of the gadget type.
    uri: str

class AvailableDashboardGadget(RequiredAvailableDashboardGadget, OptionalAvailableDashboardGadget):
    pass