# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from atlassian_jira_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from atlassian_jira_python_sdk.api_response import AsyncGeneratorResponse
from atlassian_jira_python_sdk import api_client, exceptions
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

from atlassian_jira_python_sdk.model.share_permission import SharePermission as SharePermissionSchema
from atlassian_jira_python_sdk.model.filter_subscriptions_list import FilterSubscriptionsList as FilterSubscriptionsListSchema
from atlassian_jira_python_sdk.model.user_list import UserList as UserListSchema
from atlassian_jira_python_sdk.model.user import User as UserSchema
from atlassian_jira_python_sdk.model.filter import Filter as FilterSchema

from atlassian_jira_python_sdk.type.user import User
from atlassian_jira_python_sdk.type.filter_subscriptions_list import FilterSubscriptionsList
from atlassian_jira_python_sdk.type.user_list import UserList
from atlassian_jira_python_sdk.type.filter import Filter
from atlassian_jira_python_sdk.type.share_permission import SharePermission

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.user_list import UserList as UserListPydantic
from atlassian_jira_python_sdk.pydantic.filter_subscriptions_list import FilterSubscriptionsList as FilterSubscriptionsListPydantic
from atlassian_jira_python_sdk.pydantic.share_permission import SharePermission as SharePermissionPydantic
from atlassian_jira_python_sdk.pydantic.filter import Filter as FilterPydantic
from atlassian_jira_python_sdk.pydantic.user import User as UserPydantic

# Query params
ExpandSchema = schemas.StrSchema
OverrideSharePermissionsSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'expand': typing.Union[ExpandSchema, str, ],
        'overrideSharePermissions': typing.Union[OverrideSharePermissionsSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
request_query_override_share_permissions = api_client.QueryParameter(
    name="overrideSharePermissions",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideSharePermissionsSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = FilterSchema


request_body_filter = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = FilterSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Filter


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Filter


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_filter_mapped_args(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if approximate_last_used is not None:
            _body["approximateLastUsed"] = approximate_last_used
        if edit_permissions is not None:
            _body["editPermissions"] = edit_permissions
        if favourite is not None:
            _body["favourite"] = favourite
        if favourited_count is not None:
            _body["favouritedCount"] = favourited_count
        if id is not None:
            _body["id"] = id
        if jql is not None:
            _body["jql"] = jql
        if name is not None:
            _body["name"] = name
        if owner is not None:
            _body["owner"] = owner
        if search_url is not None:
            _body["searchUrl"] = search_url
        if _self is not None:
            _body["self"] = _self
        if share_permissions is not None:
            _body["sharePermissions"] = share_permissions
        if shared_users is not None:
            _body["sharedUsers"] = shared_users
        if subscriptions is not None:
            _body["subscriptions"] = subscriptions
        if view_url is not None:
            _body["viewUrl"] = view_url
        args.body = _body
        if expand is not None:
            _query_params["expand"] = expand
        if override_share_permissions is not None:
            _query_params["overrideSharePermissions"] = override_share_permissions
        args.query = _query_params
        return args

    async def _acreate_filter_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create filter
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
            request_query_override_share_permissions,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/filter',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_filter.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_filter_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create filter
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
            request_query_override_share_permissions,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/filter',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_filter.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateFilterRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_filter(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_filter_mapped_args(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return await self._acreate_filter_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_filter(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_filter_mapped_args(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return self._create_filter_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreateFilter(BaseApi):

    async def acreate_filter(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilterPydantic:
        raw_response = await self.raw.acreate_filter(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
            **kwargs,
        )
        if validate:
            return FilterPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilterPydantic, raw_response.body)
    
    
    def create_filter(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> FilterPydantic:
        raw_response = self.raw.create_filter(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        if validate:
            return FilterPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilterPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_filter_mapped_args(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return await self._acreate_filter_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        description: typing.Optional[str] = None,
        approximate_last_used: typing.Optional[datetime] = None,
        edit_permissions: typing.Optional[typing.List[SharePermission]] = None,
        favourite: typing.Optional[bool] = None,
        favourited_count: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        jql: typing.Optional[str] = None,
        owner: typing.Optional[User] = None,
        search_url: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        share_permissions: typing.Optional[typing.List[SharePermission]] = None,
        shared_users: typing.Optional[UserList] = None,
        subscriptions: typing.Optional[FilterSubscriptionsList] = None,
        view_url: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_filter_mapped_args(
            name=name,
            description=description,
            approximate_last_used=approximate_last_used,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            _self=_self,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return self._create_filter_oapg(
            body=args.body,
            query_params=args.query,
        )

