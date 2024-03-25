# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_atlassian_connect_1_migration_properties_entity_type.put import BulkUpdateEntityProperties
from atlassian_jira_python_sdk.paths.rest_atlassian_connect_1_migration_field.put import UpdateCustomFieldValue
from atlassian_jira_python_sdk.paths.rest_atlassian_connect_1_migration_workflow_rule_search.post import WorkflowTransitionRuleConfigurations
from atlassian_jira_python_sdk.apis.tags.app_migration_api_raw import AppMigrationApiRaw


class AppMigrationApi(
    BulkUpdateEntityProperties,
    UpdateCustomFieldValue,
    WorkflowTransitionRuleConfigurations,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AppMigrationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AppMigrationApiRaw(api_client)