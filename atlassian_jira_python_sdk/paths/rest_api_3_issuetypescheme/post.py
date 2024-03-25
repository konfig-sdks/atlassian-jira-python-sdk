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

from atlassian_jira_python_sdk.model.issue_type_scheme_details_issue_type_ids import IssueTypeSchemeDetailsIssueTypeIds as IssueTypeSchemeDetailsIssueTypeIdsSchema
from atlassian_jira_python_sdk.model.issue_type_scheme_id import IssueTypeSchemeID as IssueTypeSchemeIDSchema
from atlassian_jira_python_sdk.model.issue_type_scheme_details import IssueTypeSchemeDetails as IssueTypeSchemeDetailsSchema

from atlassian_jira_python_sdk.type.issue_type_scheme_details_issue_type_ids import IssueTypeSchemeDetailsIssueTypeIds
from atlassian_jira_python_sdk.type.issue_type_scheme_id import IssueTypeSchemeID
from atlassian_jira_python_sdk.type.issue_type_scheme_details import IssueTypeSchemeDetails

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.issue_type_scheme_id import IssueTypeSchemeID as IssueTypeSchemeIDPydantic
from atlassian_jira_python_sdk.pydantic.issue_type_scheme_details_issue_type_ids import IssueTypeSchemeDetailsIssueTypeIds as IssueTypeSchemeDetailsIssueTypeIdsPydantic
from atlassian_jira_python_sdk.pydantic.issue_type_scheme_details import IssueTypeSchemeDetails as IssueTypeSchemeDetailsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = IssueTypeSchemeDetailsSchema


request_body_issue_type_scheme_details = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'OAuth2',
    'basicAuth',
]
SchemaFor201ResponseBodyApplicationJson = IssueTypeSchemeIDSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: IssueTypeSchemeID


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: IssueTypeSchemeID


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
SchemaFor409ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: str


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '409': _response_for_409,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_scheme_mapped_args(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if default_issue_type_id is not None:
            _body["defaultIssueTypeId"] = default_issue_type_id
        if issue_type_ids is not None:
            _body["issueTypeIds"] = issue_type_ids
        if name is not None:
            _body["name"] = name
        args.body = _body
        return args

    async def _acreate_scheme_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create issue type scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/rest/api/3/issuetypescheme',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_type_scheme_details.serialize(body, content_type)
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


    def _create_scheme_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create issue type scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/rest/api/3/issuetypescheme',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_type_scheme_details.serialize(body, content_type)
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


class CreateSchemeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_scheme(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_scheme_mapped_args(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
        )
        return await self._acreate_scheme_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_scheme(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_scheme_mapped_args(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
        )
        return self._create_scheme_oapg(
            body=args.body,
        )

class CreateScheme(BaseApi):

    async def acreate_scheme(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> IssueTypeSchemeIDPydantic:
        raw_response = await self.raw.acreate_scheme(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
            **kwargs,
        )
        if validate:
            return IssueTypeSchemeIDPydantic(**raw_response.body)
        return api_client.construct_model_instance(IssueTypeSchemeIDPydantic, raw_response.body)
    
    
    def create_scheme(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> IssueTypeSchemeIDPydantic:
        raw_response = self.raw.create_scheme(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
        )
        if validate:
            return IssueTypeSchemeIDPydantic(**raw_response.body)
        return api_client.construct_model_instance(IssueTypeSchemeIDPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_scheme_mapped_args(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
        )
        return await self._acreate_scheme_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        issue_type_ids: IssueTypeSchemeDetailsIssueTypeIds,
        name: str,
        description: typing.Optional[str] = None,
        default_issue_type_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_scheme_mapped_args(
            issue_type_ids=issue_type_ids,
            name=name,
            description=description,
            default_issue_type_id=default_issue_type_id,
        )
        return self._create_scheme_oapg(
            body=args.body,
        )

