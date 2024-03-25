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


class WorkflowCreateResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the created workflows and statuses.
    """


    class MetaOapg:
        
        class properties:
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['JiraWorkflowStatus']:
                        return JiraWorkflowStatus
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JiraWorkflowStatus'], typing.List['JiraWorkflowStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JiraWorkflowStatus':
                    return super().__getitem__(i)
            
            
            class workflows(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['JiraWorkflow']:
                        return JiraWorkflow
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JiraWorkflow'], typing.List['JiraWorkflow']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'workflows':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JiraWorkflow':
                    return super().__getitem__(i)
            __annotations__ = {
                "statuses": statuses,
                "workflows": workflows,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflows"]) -> MetaOapg.properties.workflows: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statuses", "workflows", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> typing.Union[MetaOapg.properties.statuses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflows"]) -> typing.Union[MetaOapg.properties.workflows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statuses", "workflows", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, schemas.Unset] = schemas.unset,
        workflows: typing.Union[MetaOapg.properties.workflows, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowCreateResponse':
        return super().__new__(
            cls,
            *args,
            statuses=statuses,
            workflows=workflows,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.jira_workflow import JiraWorkflow
from atlassian_jira_python_sdk.model.jira_workflow_status import JiraWorkflowStatus
