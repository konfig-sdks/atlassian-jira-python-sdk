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


class WebhookRegistrationDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of webhooks to register.
    """


    class MetaOapg:
        required = {
            "webhooks",
            "url",
        }
        
        class properties:
            url = schemas.StrSchema
            
            
            class webhooks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WebhookDetails']:
                        return WebhookDetails
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WebhookDetails'], typing.List['WebhookDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'webhooks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WebhookDetails':
                    return super().__getitem__(i)
            __annotations__ = {
                "url": url,
                "webhooks": webhooks,
            }
    
    webhooks: MetaOapg.properties.webhooks
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhooks"]) -> MetaOapg.properties.webhooks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "webhooks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhooks"]) -> MetaOapg.properties.webhooks: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "webhooks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        webhooks: typing.Union[MetaOapg.properties.webhooks, list, tuple, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookRegistrationDetails':
        return super().__new__(
            cls,
            *args,
            webhooks=webhooks,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.webhook_details import WebhookDetails
