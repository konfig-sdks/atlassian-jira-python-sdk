# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_workflow_transitions_transition_id_properties.post import CreateTransitionProperty
from atlassian_jira_python_sdk.paths.rest_api_3_workflow_transitions_transition_id_properties.delete import DeleteProperty
from atlassian_jira_python_sdk.paths.rest_api_3_workflow_transitions_transition_id_properties.get import GetPropertyById
from atlassian_jira_python_sdk.paths.rest_api_3_workflow_transitions_transition_id_properties.put import UpdateProperty
from atlassian_jira_python_sdk.apis.tags.workflow_transition_properties_api_raw import WorkflowTransitionPropertiesApiRaw


class WorkflowTransitionPropertiesApi(
    CreateTransitionProperty,
    DeleteProperty,
    GetPropertyById,
    UpdateProperty,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WorkflowTransitionPropertiesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WorkflowTransitionPropertiesApiRaw(api_client)
