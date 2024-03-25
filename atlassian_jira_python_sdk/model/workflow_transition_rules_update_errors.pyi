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


class WorkflowTransitionRulesUpdateErrors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of any errors encountered while updating workflow transition rules.
    """


    class MetaOapg:
        required = {
            "updateResults",
        }
        
        class properties:
            
            
            class updateResults(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowTransitionRulesUpdateErrorDetails']:
                        return WorkflowTransitionRulesUpdateErrorDetails
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkflowTransitionRulesUpdateErrorDetails'], typing.List['WorkflowTransitionRulesUpdateErrorDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'updateResults':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowTransitionRulesUpdateErrorDetails':
                    return super().__getitem__(i)
            __annotations__ = {
                "updateResults": updateResults,
            }
    
    updateResults: MetaOapg.properties.updateResults
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateResults"]) -> MetaOapg.properties.updateResults: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["updateResults", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateResults"]) -> MetaOapg.properties.updateResults: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["updateResults", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updateResults: typing.Union[MetaOapg.properties.updateResults, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowTransitionRulesUpdateErrors':
        return super().__new__(
            cls,
            *args,
            updateResults=updateResults,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.workflow_transition_rules_update_error_details import WorkflowTransitionRulesUpdateErrorDetails
