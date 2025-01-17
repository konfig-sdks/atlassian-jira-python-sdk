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


class RequiredOldToNewSecurityLevelMappingsBean(TypedDict):
    # The new issue security level ID. Providing null will clear the assigned old level from issues.
    newLevelId: str

    # The old issue security level ID. Providing null will remap all issues without any assigned levels.
    oldLevelId: str

class OptionalOldToNewSecurityLevelMappingsBean(TypedDict, total=False):
    pass

class OldToNewSecurityLevelMappingsBean(RequiredOldToNewSecurityLevelMappingsBean, OptionalOldToNewSecurityLevelMappingsBean):
    pass
