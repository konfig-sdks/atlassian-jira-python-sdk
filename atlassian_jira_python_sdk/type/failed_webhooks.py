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

from atlassian_jira_python_sdk.type.failed_webhook import FailedWebhook

class RequiredFailedWebhooks(TypedDict):
    # The maximum number of items on the page. If the list of values is shorter than this number, then there are no more pages.
    maxResults: int

    # The list of webhooks.
    values: typing.List[FailedWebhook]

class OptionalFailedWebhooks(TypedDict, total=False):
    # The URL to the next page of results. Present only if the request returned at least one result.The next page may be empty at the time of receiving the response, but new failed webhooks may appear in time. You can save the URL to the next page and query for new results periodically (for example, every hour).
    next: str

class FailedWebhooks(RequiredFailedWebhooks, OptionalFailedWebhooks):
    pass
