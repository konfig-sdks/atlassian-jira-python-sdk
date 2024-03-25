# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs.post import CreateTab
from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs_tab_id.delete import DeleteTab
from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs.get import GetAllTabs
from atlassian_jira_python_sdk.paths.rest_api_3_screens_tabs.get import ListBulkScreenTabs
from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs_tab_id_move_pos.post import MoveTabPost
from atlassian_jira_python_sdk.paths.rest_api_3_screens_screen_id_tabs_tab_id.put import UpdateTabName
from atlassian_jira_python_sdk.apis.tags.screen_tabs_api_raw import ScreenTabsApiRaw


class ScreenTabsApi(
    CreateTab,
    DeleteTab,
    GetAllTabs,
    ListBulkScreenTabs,
    MoveTabPost,
    UpdateTabName,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ScreenTabsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ScreenTabsApiRaw(api_client)