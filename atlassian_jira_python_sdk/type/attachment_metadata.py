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

from atlassian_jira_python_sdk.type.attachment_metadata_properties import AttachmentMetadataProperties
from atlassian_jira_python_sdk.type.user import User

RequiredAttachmentMetadata = TypedDict("RequiredAttachmentMetadata", {
    })

OptionalAttachmentMetadata = TypedDict("OptionalAttachmentMetadata", {
    # Details of the user who attached the file.
    "author": User,

    # The URL of the attachment.
    "content": str,

    # The datetime the attachment was created.
    "created": datetime,

    # The name of the attachment file.
    "filename": str,

    # The ID of the attachment.
    "id": int,

    # The MIME type of the attachment.
    "mimeType": str,

    "properties": AttachmentMetadataProperties,

    # The URL of the attachment metadata details.
    "self": str,

    # The size of the attachment.
    "size": int,

    # The URL of a thumbnail representing the attachment.
    "thumbnail": str,
    }, total=False)

class AttachmentMetadata(RequiredAttachmentMetadata, OptionalAttachmentMetadata):
    pass