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

from atlassian_jira_python_sdk.model.issue_filter_for_bulk_property_delete_entity_ids import IssueFilterForBulkPropertyDeleteEntityIds as IssueFilterForBulkPropertyDeleteEntityIdsSchema
from atlassian_jira_python_sdk.model.error_collection import ErrorCollection as ErrorCollectionSchema
from atlassian_jira_python_sdk.model.issue_filter_for_bulk_property_delete import IssueFilterForBulkPropertyDelete as IssueFilterForBulkPropertyDeleteSchema

from atlassian_jira_python_sdk.type.issue_filter_for_bulk_property_delete_entity_ids import IssueFilterForBulkPropertyDeleteEntityIds
from atlassian_jira_python_sdk.type.error_collection import ErrorCollection
from atlassian_jira_python_sdk.type.issue_filter_for_bulk_property_delete import IssueFilterForBulkPropertyDelete

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.issue_filter_for_bulk_property_delete import IssueFilterForBulkPropertyDelete as IssueFilterForBulkPropertyDeletePydantic
from atlassian_jira_python_sdk.pydantic.issue_filter_for_bulk_property_delete_entity_ids import IssueFilterForBulkPropertyDeleteEntityIds as IssueFilterForBulkPropertyDeleteEntityIdsPydantic
from atlassian_jira_python_sdk.pydantic.error_collection import ErrorCollection as ErrorCollectionPydantic

# Path params
PropertyKeySchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'propertyKey': typing.Union[PropertyKeySchema, str, ],
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


request_path_property_key = api_client.PathParameter(
    name="propertyKey",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PropertyKeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = IssueFilterForBulkPropertyDeleteSchema


request_body_issue_filter_for_bulk_property_delete = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


@dataclass
class ApiResponseFor303(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor303Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_303 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor303,
    response_cls_async=ApiResponseFor303Async,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _bulk_delete_issue_property_by_filter_mapped_args(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if current_value is not None:
            _body["currentValue"] = current_value
        if entity_ids is not None:
            _body["entityIds"] = entity_ids
        args.body = _body
        if property_key is not None:
            _path_params["propertyKey"] = property_key
        args.path = _path_params
        return args

    async def _abulk_delete_issue_property_by_filter_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Bulk delete issue property
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_property_key,
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
            path_template='/rest/api/3/issue/properties/{propertyKey}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_filter_for_bulk_property_delete.serialize(body, content_type)
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


    def _bulk_delete_issue_property_by_filter_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Bulk delete issue property
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_property_key,
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
            path_template='/rest/api/3/issue/properties/{propertyKey}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_filter_for_bulk_property_delete.serialize(body, content_type)
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


class BulkDeleteIssuePropertyByFilterRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def abulk_delete_issue_property_by_filter(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._bulk_delete_issue_property_by_filter_mapped_args(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
        )
        return await self._abulk_delete_issue_property_by_filter_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def bulk_delete_issue_property_by_filter(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._bulk_delete_issue_property_by_filter_mapped_args(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
        )
        return self._bulk_delete_issue_property_by_filter_oapg(
            body=args.body,
            path_params=args.path,
        )

class BulkDeleteIssuePropertyByFilter(BaseApi):

    async def abulk_delete_issue_property_by_filter(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.abulk_delete_issue_property_by_filter(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
            **kwargs,
        )
    
    
    def bulk_delete_issue_property_by_filter(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.bulk_delete_issue_property_by_filter(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._bulk_delete_issue_property_by_filter_mapped_args(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
        )
        return await self._abulk_delete_issue_property_by_filter_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        property_key: str,
        current_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        entity_ids: typing.Optional[IssueFilterForBulkPropertyDeleteEntityIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._bulk_delete_issue_property_by_filter_mapped_args(
            property_key=property_key,
            current_value=current_value,
            entity_ids=entity_ids,
        )
        return self._bulk_delete_issue_property_by_filter_oapg(
            body=args.body,
            path_params=args.path,
        )

