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

from atlassian_jira_python_sdk.model.user_search_find_assignable_users_response import UserSearchFindAssignableUsersResponse as UserSearchFindAssignableUsersResponseSchema

from atlassian_jira_python_sdk.type.user_search_find_assignable_users_response import UserSearchFindAssignableUsersResponse

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.user_search_find_assignable_users_response import UserSearchFindAssignableUsersResponse as UserSearchFindAssignableUsersResponsePydantic

# Query params
QuerySchema = schemas.StrSchema
UsernameSchema = schemas.StrSchema


class AccountIdSchema(
    schemas.StrSchema
):
    pass
ProjectKeysSchema = schemas.StrSchema
StartAtSchema = schemas.Int32Schema
MaxResultsSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'projectKeys': typing.Union[ProjectKeysSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'query': typing.Union[QuerySchema, str, ],
        'username': typing.Union[UsernameSchema, str, ],
        'accountId': typing.Union[AccountIdSchema, str, ],
        'startAt': typing.Union[StartAtSchema, decimal.Decimal, int, ],
        'maxResults': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_username = api_client.QueryParameter(
    name="username",
    style=api_client.ParameterStyle.FORM,
    schema=UsernameSchema,
    explode=True,
)
request_query_account_id = api_client.QueryParameter(
    name="accountId",
    style=api_client.ParameterStyle.FORM,
    schema=AccountIdSchema,
    explode=True,
)
request_query_project_keys = api_client.QueryParameter(
    name="projectKeys",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectKeysSchema,
    required=True,
    explode=True,
)
request_query_start_at = api_client.QueryParameter(
    name="startAt",
    style=api_client.ParameterStyle.FORM,
    schema=StartAtSchema,
    explode=True,
)
request_query_max_results = api_client.QueryParameter(
    name="maxResults",
    style=api_client.ParameterStyle.FORM,
    schema=MaxResultsSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = UserSearchFindAssignableUsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UserSearchFindAssignableUsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UserSearchFindAssignableUsersResponse


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


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _find_assignable_users_mapped_args(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if username is not None:
            _query_params["username"] = username
        if account_id is not None:
            _query_params["accountId"] = account_id
        if project_keys is not None:
            _query_params["projectKeys"] = project_keys
        if start_at is not None:
            _query_params["startAt"] = start_at
        if max_results is not None:
            _query_params["maxResults"] = max_results
        args.query = _query_params
        return args

    async def _afind_assignable_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Find users assignable to projects
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_username,
            request_query_account_id,
            request_query_project_keys,
            request_query_start_at,
            request_query_max_results,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/user/assignable/multiProjectSearch',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _find_assignable_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Find users assignable to projects
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_username,
            request_query_account_id,
            request_query_project_keys,
            request_query_start_at,
            request_query_max_results,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/user/assignable/multiProjectSearch',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class FindAssignableUsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_assignable_users(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_assignable_users_mapped_args(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
        )
        return await self._afind_assignable_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def find_assignable_users(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_assignable_users_mapped_args(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
        )
        return self._find_assignable_users_oapg(
            query_params=args.query,
        )

class FindAssignableUsers(BaseApi):

    async def afind_assignable_users(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserSearchFindAssignableUsersResponsePydantic:
        raw_response = await self.raw.afind_assignable_users(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
            **kwargs,
        )
        if validate:
            return RootModel[UserSearchFindAssignableUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserSearchFindAssignableUsersResponsePydantic, raw_response.body)
    
    
    def find_assignable_users(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate: bool = False,
    ) -> UserSearchFindAssignableUsersResponsePydantic:
        raw_response = self.raw.find_assignable_users(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
        )
        if validate:
            return RootModel[UserSearchFindAssignableUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserSearchFindAssignableUsersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_assignable_users_mapped_args(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
        )
        return await self._afind_assignable_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        project_keys: str,
        query: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_assignable_users_mapped_args(
            project_keys=project_keys,
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
        )
        return self._find_assignable_users_oapg(
            query_params=args.query,
        )

