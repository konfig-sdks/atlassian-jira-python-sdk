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

from atlassian_jira_python_sdk.model.issue_update_metadata import IssueUpdateMetadata as IssueUpdateMetadataSchema

from atlassian_jira_python_sdk.type.issue_update_metadata import IssueUpdateMetadata

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.issue_update_metadata import IssueUpdateMetadata as IssueUpdateMetadataPydantic

# Query params
OverrideScreenSecuritySchema = schemas.BoolSchema
OverrideEditableFlagSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'overrideScreenSecurity': typing.Union[OverrideScreenSecuritySchema, bool, ],
        'overrideEditableFlag': typing.Union[OverrideEditableFlagSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_override_screen_security = api_client.QueryParameter(
    name="overrideScreenSecurity",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideScreenSecuritySchema,
    explode=True,
)
request_query_override_editable_flag = api_client.QueryParameter(
    name="overrideEditableFlag",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideEditableFlagSchema,
    explode=True,
)
# Path params
IssueIdOrKeySchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'issueIdOrKey': typing.Union[IssueIdOrKeySchema, str, ],
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


request_path_issue_id_or_key = api_client.PathParameter(
    name="issueIdOrKey",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IssueIdOrKeySchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = IssueUpdateMetadataSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: IssueUpdateMetadata


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IssueUpdateMetadata


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_edit_meta_mapped_args(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if override_screen_security is not None:
            _query_params["overrideScreenSecurity"] = override_screen_security
        if override_editable_flag is not None:
            _query_params["overrideEditableFlag"] = override_editable_flag
        if issue_id_or_key is not None:
            _path_params["issueIdOrKey"] = issue_id_or_key
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_edit_meta_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Get edit issue metadata
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_issue_id_or_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_override_screen_security,
            request_query_override_editable_flag,
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
            path_template='/rest/api/3/issue/{issueIdOrKey}/editmeta',
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


    def _get_edit_meta_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get edit issue metadata
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_issue_id_or_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_override_screen_security,
            request_query_override_editable_flag,
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
            path_template='/rest/api/3/issue/{issueIdOrKey}/editmeta',
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


class GetEditMetaRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_edit_meta(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_edit_meta_mapped_args(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        return await self._aget_edit_meta_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_edit_meta(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_edit_meta_mapped_args(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        return self._get_edit_meta_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetEditMeta(BaseApi):

    async def aget_edit_meta(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> IssueUpdateMetadataPydantic:
        raw_response = await self.raw.aget_edit_meta(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
            **kwargs,
        )
        if validate:
            return IssueUpdateMetadataPydantic(**raw_response.body)
        return api_client.construct_model_instance(IssueUpdateMetadataPydantic, raw_response.body)
    
    
    def get_edit_meta(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> IssueUpdateMetadataPydantic:
        raw_response = self.raw.get_edit_meta(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        if validate:
            return IssueUpdateMetadataPydantic(**raw_response.body)
        return api_client.construct_model_instance(IssueUpdateMetadataPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_edit_meta_mapped_args(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        return await self._aget_edit_meta_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        issue_id_or_key: str,
        override_screen_security: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_edit_meta_mapped_args(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        return self._get_edit_meta_oapg(
            query_params=args.query,
            path_params=args.path,
        )

