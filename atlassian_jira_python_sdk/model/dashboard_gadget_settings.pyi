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


class DashboardGadgetSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the settings for a dashboard gadget.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            color = schemas.StrSchema
            ignoreUriAndModuleKeyValidation = schemas.BoolSchema
            moduleKey = schemas.StrSchema
        
            @staticmethod
            def position() -> typing.Type['DashboardGadgetPosition']:
                return DashboardGadgetPosition
            uri = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "color": color,
                "ignoreUriAndModuleKeyValidation": ignoreUriAndModuleKeyValidation,
                "moduleKey": moduleKey,
                "position": position,
                "uri": uri,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignoreUriAndModuleKeyValidation"]) -> MetaOapg.properties.ignoreUriAndModuleKeyValidation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moduleKey"]) -> MetaOapg.properties.moduleKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> 'DashboardGadgetPosition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "color", "ignoreUriAndModuleKeyValidation", "moduleKey", "position", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignoreUriAndModuleKeyValidation"]) -> typing.Union[MetaOapg.properties.ignoreUriAndModuleKeyValidation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moduleKey"]) -> typing.Union[MetaOapg.properties.moduleKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union['DashboardGadgetPosition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "color", "ignoreUriAndModuleKeyValidation", "moduleKey", "position", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        ignoreUriAndModuleKeyValidation: typing.Union[MetaOapg.properties.ignoreUriAndModuleKeyValidation, bool, schemas.Unset] = schemas.unset,
        moduleKey: typing.Union[MetaOapg.properties.moduleKey, str, schemas.Unset] = schemas.unset,
        position: typing.Union['DashboardGadgetPosition', schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DashboardGadgetSettings':
        return super().__new__(
            cls,
            *args,
            title=title,
            color=color,
            ignoreUriAndModuleKeyValidation=ignoreUriAndModuleKeyValidation,
            moduleKey=moduleKey,
            position=position,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.dashboard_gadget_position import DashboardGadgetPosition
