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

from atlassian_jira_python_sdk.type.version_usage_in_custom_field import VersionUsageInCustomField

RequiredVersionIssueCounts = TypedDict("RequiredVersionIssueCounts", {
    })

OptionalVersionIssueCounts = TypedDict("OptionalVersionIssueCounts", {
    # List of custom fields using the version.
    "customFieldUsage": typing.List[VersionUsageInCustomField],

    # Count of issues where a version custom field is set to the version.
    "issueCountWithCustomFieldsShowingVersion": int,

    # Count of issues where the `affectedVersion` is set to the version.
    "issuesAffectedCount": int,

    # Count of issues where the `fixVersion` is set to the version.
    "issuesFixedCount": int,

    # The URL of these count details.
    "self": str,
    }, total=False)

class VersionIssueCounts(RequiredVersionIssueCounts, OptionalVersionIssueCounts):
    pass
