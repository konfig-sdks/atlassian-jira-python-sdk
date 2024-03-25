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


class ContainerForWebhookIDs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Container for a list of webhook IDs.
    """


    class MetaOapg:
        required = {
            "webhookIds",
        }
        
        class properties:
        
            @staticmethod
            def webhookIds() -> typing.Type['ContainerForWebhookIDsWebhookIds']:
                return ContainerForWebhookIDsWebhookIds
            __annotations__ = {
                "webhookIds": webhookIds,
            }
    
    webhookIds: 'ContainerForWebhookIDsWebhookIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookIds"]) -> 'ContainerForWebhookIDsWebhookIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["webhookIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookIds"]) -> 'ContainerForWebhookIDsWebhookIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["webhookIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        webhookIds: 'ContainerForWebhookIDsWebhookIds',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContainerForWebhookIDs':
        return super().__new__(
            cls,
            *args,
            webhookIds=webhookIds,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.container_for_webhook_ids_webhook_ids import ContainerForWebhookIDsWebhookIds