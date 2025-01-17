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

from atlassian_jira_python_sdk.type.notification_event import NotificationEvent

class RequiredNotificationEvent(TypedDict):
    pass

class OptionalNotificationEvent(TypedDict, total=False):
    # The description of the event.
    description: str

    # The ID of the event. The event can be a [Jira system event](https://confluence.atlassian.com/x/8YdKLg#Creatinganotificationscheme-eventsEvents) or a [custom event](https://confluence.atlassian.com/x/AIlKLg).
    id: int

    # The name of the event.
    name: str

    # The template of the event. Only custom events configured by Jira administrators have template.
    templateEvent: "NotificationEvent"

class NotificationEvent(RequiredNotificationEvent, OptionalNotificationEvent):
    pass
