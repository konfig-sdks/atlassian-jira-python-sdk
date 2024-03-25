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


class RequiredAnnouncementBannerConfiguration(TypedDict):
    pass

class OptionalAnnouncementBannerConfiguration(TypedDict, total=False):
    # Hash of the banner data. The client detects updates by comparing hash IDs.
    hashId: str

    # Flag indicating if the announcement banner can be dismissed by the user.
    isDismissible: bool

    # Flag indicating if the announcement banner is enabled or not.
    isEnabled: bool

    # The text on the announcement banner.
    message: str

    # Visibility of the announcement banner.
    visibility: str

class AnnouncementBannerConfiguration(RequiredAnnouncementBannerConfiguration, OptionalAnnouncementBannerConfiguration):
    pass