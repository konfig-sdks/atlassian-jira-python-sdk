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


class RequiredFailedWebhook(TypedDict):
    # The time the webhook was added to the list of failed webhooks (that is, the time of the last failed retry).
    failureTime: int

    # The webhook ID, as sent in the `X-Atlassian-Webhook-Identifier` header with the webhook.
    id: str

    # The original webhook destination.
    url: str

class OptionalFailedWebhook(TypedDict, total=False):
    # The webhook body.
    body: str

class FailedWebhook(RequiredFailedWebhook, OptionalFailedWebhook):
    pass
