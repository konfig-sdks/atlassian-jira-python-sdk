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


class NewUserDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The user details.
    """


    class MetaOapg:
        required = {
            "emailAddress",
        }
        
        class properties:
            emailAddress = schemas.StrSchema
        
            @staticmethod
            def applicationKeys() -> typing.Type['NewUserDetailsApplicationKeys']:
                return NewUserDetailsApplicationKeys
            displayName = schemas.StrSchema
            key = schemas.StrSchema
            name = schemas.StrSchema
            password = schemas.StrSchema
        
            @staticmethod
            def products() -> typing.Type['NewUserDetailsProducts']:
                return NewUserDetailsProducts
            _self = schemas.StrSchema
            __annotations__ = {
                "emailAddress": emailAddress,
                "applicationKeys": applicationKeys,
                "displayName": displayName,
                "key": key,
                "name": name,
                "password": password,
                "products": products,
                "self": _self,
            }
        additional_properties = schemas.AnyTypeSchema
    
    emailAddress: MetaOapg.properties.emailAddress
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationKeys"]) -> 'NewUserDetailsApplicationKeys': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["products"]) -> 'NewUserDetailsProducts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["emailAddress"], typing_extensions.Literal["applicationKeys"], typing_extensions.Literal["displayName"], typing_extensions.Literal["key"], typing_extensions.Literal["name"], typing_extensions.Literal["password"], typing_extensions.Literal["products"], typing_extensions.Literal["self"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationKeys"]) -> typing.Union['NewUserDetailsApplicationKeys', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["products"]) -> typing.Union['NewUserDetailsProducts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["emailAddress"], typing_extensions.Literal["applicationKeys"], typing_extensions.Literal["displayName"], typing_extensions.Literal["key"], typing_extensions.Literal["name"], typing_extensions.Literal["password"], typing_extensions.Literal["products"], typing_extensions.Literal["self"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, str, ],
        applicationKeys: typing.Union['NewUserDetailsApplicationKeys', schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        products: typing.Union['NewUserDetailsProducts', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'NewUserDetails':
        return super().__new__(
            cls,
            *args,
            emailAddress=emailAddress,
            applicationKeys=applicationKeys,
            displayName=displayName,
            key=key,
            name=name,
            password=password,
            products=products,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.new_user_details_application_keys import NewUserDetailsApplicationKeys
from atlassian_jira_python_sdk.model.new_user_details_products import NewUserDetailsProducts
