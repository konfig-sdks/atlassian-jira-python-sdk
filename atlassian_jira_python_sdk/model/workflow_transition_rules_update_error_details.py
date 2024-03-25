# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlassian_jira_python_sdk import schemas  # noqa: F401


class WorkflowTransitionRulesUpdateErrorDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of any errors encountered while updating workflow transition rules for a workflow.
    """


    class MetaOapg:
        required = {
            "updateErrors",
            "workflowId",
            "ruleUpdateErrors",
        }
        
        class properties:
        
            @staticmethod
            def ruleUpdateErrors() -> typing.Type['WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors']:
                return WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
        
            @staticmethod
            def updateErrors() -> typing.Type['WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors']:
                return WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors
        
            @staticmethod
            def workflowId() -> typing.Type['WorkflowId']:
                return WorkflowId
            __annotations__ = {
                "ruleUpdateErrors": ruleUpdateErrors,
                "updateErrors": updateErrors,
                "workflowId": workflowId,
            }
    
    updateErrors: 'WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors'
    workflowId: 'WorkflowId'
    ruleUpdateErrors: 'WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleUpdateErrors"]) -> 'WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateErrors"]) -> 'WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowId"]) -> 'WorkflowId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ruleUpdateErrors", "updateErrors", "workflowId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleUpdateErrors"]) -> 'WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateErrors"]) -> 'WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowId"]) -> 'WorkflowId': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ruleUpdateErrors", "updateErrors", "workflowId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updateErrors: 'WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors',
        workflowId: 'WorkflowId',
        ruleUpdateErrors: 'WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowTransitionRulesUpdateErrorDetails':
        return super().__new__(
            cls,
            *args,
            updateErrors=updateErrors,
            workflowId=workflowId,
            ruleUpdateErrors=ruleUpdateErrors,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_id import WorkflowId
from atlassian_jira_python_sdk.model.workflow_transition_rules_update_error_details_rule_update_errors import WorkflowTransitionRulesUpdateErrorDetailsRuleUpdateErrors
from atlassian_jira_python_sdk.model.workflow_transition_rules_update_error_details_update_errors import WorkflowTransitionRulesUpdateErrorDetailsUpdateErrors