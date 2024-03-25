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



from ...api_client import Dictionary

from . import path

# Path params
IssueTypeSchemeIdSchema = schemas.Int64Schema
IssueTypeIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'issueTypeSchemeId': typing.Union[IssueTypeSchemeIdSchema, decimal.Decimal, int, ],
        'issueTypeId': typing.Union[IssueTypeIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_issue_type_scheme_id = api_client.PathParameter(
    name="issueTypeSchemeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IssueTypeSchemeIdSchema,
    required=True,
)
request_path_issue_type_id = api_client.PathParameter(
    name="issueTypeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IssueTypeIdSchema,
    required=True,
)
_auth = [
    'OAuth2',
    'basicAuth',
]
SchemaFor204ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: str


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
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
SchemaFor403ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: str


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: str


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _remove_issue_type_scheme_mapping_mapped_args(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if issue_type_scheme_id is not None:
            _path_params["issueTypeSchemeId"] = issue_type_scheme_id
        if issue_type_id is not None:
            _path_params["issueTypeId"] = issue_type_id
        args.path = _path_params
        return args

    async def _aremove_issue_type_scheme_mapping_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Remove issue type from issue type scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_issue_type_scheme_id,
            request_path_issue_type_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _remove_issue_type_scheme_mapping_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Remove issue type from issue type scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_issue_type_scheme_id,
            request_path_issue_type_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class RemoveIssueTypeSchemeMappingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_issue_type_scheme_mapping(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_issue_type_scheme_mapping_mapped_args(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        return await self._aremove_issue_type_scheme_mapping_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def remove_issue_type_scheme_mapping(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_issue_type_scheme_mapping_mapped_args(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        return self._remove_issue_type_scheme_mapping_oapg(
            path_params=args.path,
        )

class RemoveIssueTypeSchemeMapping(BaseApi):

    async def aremove_issue_type_scheme_mapping(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.aremove_issue_type_scheme_mapping(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def remove_issue_type_scheme_mapping(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.remove_issue_type_scheme_mapping(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_issue_type_scheme_mapping_mapped_args(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        return await self._aremove_issue_type_scheme_mapping_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_issue_type_scheme_mapping_mapped_args(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        return self._remove_issue_type_scheme_mapping_oapg(
            path_params=args.path,
        )
