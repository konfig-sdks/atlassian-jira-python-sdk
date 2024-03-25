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

from atlassian_jira_python_sdk.model.search_results import SearchResults as SearchResultsSchema

from atlassian_jira_python_sdk.type.search_results import SearchResults

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.search_results import SearchResults as SearchResultsPydantic

from . import path

# Query params
JqlSchema = schemas.StrSchema
StartAtSchema = schemas.Int32Schema
MaxResultsSchema = schemas.Int32Schema


class ValidateQuerySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "strict": "STRICT",
            "warn": "WARN",
            "none": "NONE",
            "true": "TRUE",
            "false": "FALSE",
        }
    
    @schemas.classproperty
    def STRICT(cls):
        return cls("strict")
    
    @schemas.classproperty
    def WARN(cls):
        return cls("warn")
    
    @schemas.classproperty
    def NONE(cls):
        return cls("none")
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")


class FieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ExpandSchema = schemas.StrSchema


class PropertiesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PropertiesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
FieldsByKeysSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'jql': typing.Union[JqlSchema, str, ],
        'startAt': typing.Union[StartAtSchema, decimal.Decimal, int, ],
        'maxResults': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'validateQuery': typing.Union[ValidateQuerySchema, str, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'expand': typing.Union[ExpandSchema, str, ],
        'properties': typing.Union[PropertiesSchema, list, tuple, ],
        'fieldsByKeys': typing.Union[FieldsByKeysSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_jql = api_client.QueryParameter(
    name="jql",
    style=api_client.ParameterStyle.FORM,
    schema=JqlSchema,
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
request_query_validate_query = api_client.QueryParameter(
    name="validateQuery",
    style=api_client.ParameterStyle.FORM,
    schema=ValidateQuerySchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
request_query_properties = api_client.QueryParameter(
    name="properties",
    style=api_client.ParameterStyle.FORM,
    schema=PropertiesSchema,
    explode=True,
)
request_query_fields_by_keys = api_client.QueryParameter(
    name="fieldsByKeys",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsByKeysSchema,
    explode=True,
)
_auth = [
    'OAuth2',
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = SearchResultsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SearchResults


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SearchResults


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _jql_get_mapped_args(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if jql is not None:
            _query_params["jql"] = jql
        if start_at is not None:
            _query_params["startAt"] = start_at
        if max_results is not None:
            _query_params["maxResults"] = max_results
        if validate_query is not None:
            _query_params["validateQuery"] = validate_query
        if fields is not None:
            _query_params["fields"] = fields
        if expand is not None:
            _query_params["expand"] = expand
        if properties is not None:
            _query_params["properties"] = properties
        if fields_by_keys is not None:
            _query_params["fieldsByKeys"] = fields_by_keys
        args.query = _query_params
        return args

    async def _ajql_get_oapg(
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
        Search for issues using JQL (GET)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_jql,
            request_query_start_at,
            request_query_max_results,
            request_query_validate_query,
            request_query_fields,
            request_query_expand,
            request_query_properties,
            request_query_fields_by_keys,
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
            path_template='/rest/api/3/search',
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


    def _jql_get_oapg(
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
        Search for issues using JQL (GET)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_jql,
            request_query_start_at,
            request_query_max_results,
            request_query_validate_query,
            request_query_fields,
            request_query_expand,
            request_query_properties,
            request_query_fields_by_keys,
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
            path_template='/rest/api/3/search',
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


class JqlGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ajql_get(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._jql_get_mapped_args(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
        )
        return await self._ajql_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def jql_get(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._jql_get_mapped_args(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
        )
        return self._jql_get_oapg(
            query_params=args.query,
        )

class JqlGet(BaseApi):

    async def ajql_get(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> SearchResultsPydantic:
        raw_response = await self.raw.ajql_get(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
            **kwargs,
        )
        if validate:
            return SearchResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(SearchResultsPydantic, raw_response.body)
    
    
    def jql_get(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> SearchResultsPydantic:
        raw_response = self.raw.jql_get(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
        )
        if validate:
            return SearchResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(SearchResultsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._jql_get_mapped_args(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
        )
        return await self._ajql_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        jql: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        validate_query: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        expand: typing.Optional[str] = None,
        properties: typing.Optional[typing.List[str]] = None,
        fields_by_keys: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._jql_get_mapped_args(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
        )
        return self._jql_get_oapg(
            query_params=args.query,
        )

