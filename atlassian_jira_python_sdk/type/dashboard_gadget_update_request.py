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

from atlassian_jira_python_sdk.type.dashboard_gadget_position import DashboardGadgetPosition

class RequiredDashboardGadgetUpdateRequest(TypedDict):
    pass

class OptionalDashboardGadgetUpdateRequest(TypedDict, total=False):
    # The title of the gadget.
    title: str

    # The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`.
    color: str

    # The position of the gadget.
    position: DashboardGadgetPosition

class DashboardGadgetUpdateRequest(RequiredDashboardGadgetUpdateRequest, OptionalDashboardGadgetUpdateRequest):
    pass
