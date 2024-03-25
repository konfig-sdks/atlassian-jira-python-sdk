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


class WorkflowUsages(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The workflows that use this status. Only available if the `workflowUsages` expand is requested.
    """


    class MetaOapg:
        
        class properties:
            workflowId = schemas.StrSchema
            workflowName = schemas.StrSchema
            __annotations__ = {
                "workflowId": workflowId,
                "workflowName": workflowName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowId"]) -> MetaOapg.properties.workflowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowName"]) -> MetaOapg.properties.workflowName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["workflowId", "workflowName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowId"]) -> typing.Union[MetaOapg.properties.workflowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowName"]) -> typing.Union[MetaOapg.properties.workflowName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["workflowId", "workflowName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workflowId: typing.Union[MetaOapg.properties.workflowId, str, schemas.Unset] = schemas.unset,
        workflowName: typing.Union[MetaOapg.properties.workflowName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowUsages':
        return super().__new__(
            cls,
            *args,
            workflowId=workflowId,
            workflowName=workflowName,
            _configuration=_configuration,
            **kwargs,
        )
