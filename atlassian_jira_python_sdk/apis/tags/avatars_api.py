# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_type_type_owner_owning_object_id_avatar_id.delete import DeleteAvatar
from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_view_type_type_avatar_id.get import GetAvatarImageById
from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_view_type_type_owner_entity_id.get import GetAvatarImageByOwner
from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_view_type_type.get import GetDefaultAvatarImageByType
from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_type_type_owner_entity_id.get import GetSystemAndCustomAvatarsByType
from atlassian_jira_python_sdk.paths.rest_api_3_avatar_type_system.get import GetSystemAvatarsByType
from atlassian_jira_python_sdk.paths.rest_api_3_universal_avatar_type_type_owner_entity_id.post import LoadCustomAvatarForProjectOrIssueType
from atlassian_jira_python_sdk.apis.tags.avatars_api_raw import AvatarsApiRaw


class AvatarsApi(
    DeleteAvatar,
    GetAvatarImageById,
    GetAvatarImageByOwner,
    GetDefaultAvatarImageByType,
    GetSystemAndCustomAvatarsByType,
    GetSystemAvatarsByType,
    LoadCustomAvatarForProjectOrIssueType,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AvatarsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AvatarsApiRaw(api_client)