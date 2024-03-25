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

from atlassian_jira_python_sdk.model.error_collection import ErrorCollection as ErrorCollectionSchema
from atlassian_jira_python_sdk.model.page_bean_security_level import PageBeanSecurityLevel as PageBeanSecurityLevelSchema

from atlassian_jira_python_sdk.type.error_collection import ErrorCollection
from atlassian_jira_python_sdk.type.page_bean_security_level import PageBeanSecurityLevel

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.page_bean_security_level import PageBeanSecurityLevel as PageBeanSecurityLevelPydantic
from atlassian_jira_python_sdk.pydantic.error_collection import ErrorCollection as ErrorCollectionPydantic

from . import path

# Query params
StartAtSchema = schemas.StrSchema
MaxResultsSchema = schemas.StrSchema


class IdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class SchemeIdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemeIdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
OnlyDefaultSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'startAt': typing.Union[StartAtSchema, str, ],
        'maxResults': typing.Union[MaxResultsSchema, str, ],
        'id': typing.Union[IdSchema, list, tuple, ],
        'schemeId': typing.Union[SchemeIdSchema, list, tuple, ],
        'onlyDefault': typing.Union[OnlyDefaultSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_scheme_id = api_client.QueryParameter(
    name="schemeId",
    style=api_client.ParameterStyle.FORM,
    schema=SchemeIdSchema,
    explode=True,
)
request_query_only_default = api_client.QueryParameter(
    name="onlyDefault",
    style=api_client.ParameterStyle.FORM,
    schema=OnlyDefaultSchema,
    explode=True,
)
_auth = [
    'OAuth2',
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = PageBeanSecurityLevelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PageBeanSecurityLevel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PageBeanSecurityLevel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorCollectionSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorCollection


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorCollection


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorCollectionSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorCollection


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorCollection


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorCollectionSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ErrorCollection


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ErrorCollection


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_security_levels_mapped_args(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if start_at is not None:
            _query_params["startAt"] = start_at
        if max_results is not None:
            _query_params["maxResults"] = max_results
        if id is not None:
            _query_params["id"] = id
        if scheme_id is not None:
            _query_params["schemeId"] = scheme_id
        if only_default is not None:
            _query_params["onlyDefault"] = only_default
        args.query = _query_params
        return args

    async def _aget_security_levels_oapg(
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
        Get issue security levels
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_start_at,
            request_query_max_results,
            request_query_id,
            request_query_scheme_id,
            request_query_only_default,
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
            path_template='/rest/api/3/issuesecurityschemes/level',
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


    def _get_security_levels_oapg(
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
        Get issue security levels
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_start_at,
            request_query_max_results,
            request_query_id,
            request_query_scheme_id,
            request_query_only_default,
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
            path_template='/rest/api/3/issuesecurityschemes/level',
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


class GetSecurityLevelsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_security_levels(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_security_levels_mapped_args(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        return await self._aget_security_levels_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_security_levels(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_security_levels_mapped_args(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        return self._get_security_levels_oapg(
            query_params=args.query,
        )

class GetSecurityLevels(BaseApi):

    async def aget_security_levels(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> PageBeanSecurityLevelPydantic:
        raw_response = await self.raw.aget_security_levels(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
            **kwargs,
        )
        if validate:
            return PageBeanSecurityLevelPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanSecurityLevelPydantic, raw_response.body)
    
    
    def get_security_levels(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> PageBeanSecurityLevelPydantic:
        raw_response = self.raw.get_security_levels(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        if validate:
            return PageBeanSecurityLevelPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanSecurityLevelPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_security_levels_mapped_args(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        return await self._aget_security_levels_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        start_at: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        id: typing.Optional[typing.List[str]] = None,
        scheme_id: typing.Optional[typing.List[str]] = None,
        only_default: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_security_levels_mapped_args(
            start_at=start_at,
            max_results=max_results,
            id=id,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        return self._get_security_levels_oapg(
            query_params=args.query,
        )
