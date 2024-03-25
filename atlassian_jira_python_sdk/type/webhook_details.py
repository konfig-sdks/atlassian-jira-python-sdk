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

from atlassian_jira_python_sdk.type.webhook_details_events import WebhookDetailsEvents
from atlassian_jira_python_sdk.type.webhook_details_field_ids_filter import WebhookDetailsFieldIdsFilter
from atlassian_jira_python_sdk.type.webhook_details_issue_property_keys_filter import WebhookDetailsIssuePropertyKeysFilter

class RequiredWebhookDetails(TypedDict):
    events: WebhookDetailsEvents

    # The JQL filter that specifies which issues the webhook is sent for. Only a subset of JQL can be used. The supported elements are:   *  Fields: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]`. For custom fields (`cf[id]`), only the epic label custom field is supported.\".  *  Operators: `=`, `!=`, `IN`, and `NOT IN`.
    jqlFilter: str

class OptionalWebhookDetails(TypedDict, total=False):
    fieldIdsFilter: WebhookDetailsFieldIdsFilter

    issuePropertyKeysFilter: WebhookDetailsIssuePropertyKeysFilter

class WebhookDetails(RequiredWebhookDetails, OptionalWebhookDetails):
    pass
