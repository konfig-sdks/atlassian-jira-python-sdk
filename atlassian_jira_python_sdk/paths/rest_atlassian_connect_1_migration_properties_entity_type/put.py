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

from atlassian_jira_python_sdk.model.app_migration_bulk_update_entity_properties_request import AppMigrationBulkUpdateEntityPropertiesRequest as AppMigrationBulkUpdateEntityPropertiesRequestSchema

from atlassian_jira_python_sdk.type.app_migration_bulk_update_entity_properties_request import AppMigrationBulkUpdateEntityPropertiesRequest

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.app_migration_bulk_update_entity_properties_request import AppMigrationBulkUpdateEntityPropertiesRequest as AppMigrationBulkUpdateEntityPropertiesRequestPydantic

from . import path

# Header params
AtlassianTransferIdSchema = schemas.UUIDSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'Atlassian-Transfer-Id': typing.Union[AtlassianTransferIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_atlassian_transfer_id = api_client.HeaderParameter(
    name="Atlassian-Transfer-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AtlassianTransferIdSchema,
    required=True,
)
# Path params


class EntityTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "IssueProperty": "ISSUE_PROPERTY",
            "CommentProperty": "COMMENT_PROPERTY",
            "DashboardItemProperty": "DASHBOARD_ITEM_PROPERTY",
            "IssueTypeProperty": "ISSUE_TYPE_PROPERTY",
            "ProjectProperty": "PROJECT_PROPERTY",
            "UserProperty": "USER_PROPERTY",
            "WorklogProperty": "WORKLOG_PROPERTY",
            "BoardProperty": "BOARD_PROPERTY",
            "SprintProperty": "SPRINT_PROPERTY",
        }
    
    @schemas.classproperty
    def ISSUE_PROPERTY(cls):
        return cls("IssueProperty")
    
    @schemas.classproperty
    def COMMENT_PROPERTY(cls):
        return cls("CommentProperty")
    
    @schemas.classproperty
    def DASHBOARD_ITEM_PROPERTY(cls):
        return cls("DashboardItemProperty")
    
    @schemas.classproperty
    def ISSUE_TYPE_PROPERTY(cls):
        return cls("IssueTypeProperty")
    
    @schemas.classproperty
    def PROJECT_PROPERTY(cls):
        return cls("ProjectProperty")
    
    @schemas.classproperty
    def USER_PROPERTY(cls):
        return cls("UserProperty")
    
    @schemas.classproperty
    def WORKLOG_PROPERTY(cls):
        return cls("WorklogProperty")
    
    @schemas.classproperty
    def BOARD_PROPERTY(cls):
        return cls("BoardProperty")
    
    @schemas.classproperty
    def SPRINT_PROPERTY(cls):
        return cls("SprintProperty")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'entityType': typing.Union[EntityTypeSchema, str, ],
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


request_path_entity_type = api_client.PathParameter(
    name="entityType",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EntityTypeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = AppMigrationBulkUpdateEntityPropertiesRequestSchema


request_body_app_migration_bulk_update_entity_properties_request = api_client.RequestBody(
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
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
}


class BaseApi(api_client.Api):

    def _bulk_update_entity_properties_mapped_args(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        args.body = body if body is not None else _body
        if atlassian_transfer_id is not None:
            _header_params["Atlassian-Transfer-Id"] = atlassian_transfer_id
        if entity_type is not None:
            _path_params["entityType"] = entity_type
        args.header = _header_params
        args.path = _path_params
        return args

    async def _abulk_update_entity_properties_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Bulk update entity properties
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_entity_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_atlassian_transfer_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'put'.upper()
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
            path_template='/rest/atlassian-connect/1/migration/properties/{entityType}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_app_migration_bulk_update_entity_properties_request.serialize(body, content_type)
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


    def _bulk_update_entity_properties_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Bulk update entity properties
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_entity_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_atlassian_transfer_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'put'.upper()
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
            path_template='/rest/atlassian-connect/1/migration/properties/{entityType}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_app_migration_bulk_update_entity_properties_request.serialize(body, content_type)
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


class BulkUpdateEntityPropertiesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def abulk_update_entity_properties(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._bulk_update_entity_properties_mapped_args(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
        )
        return await self._abulk_update_entity_properties_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def bulk_update_entity_properties(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._bulk_update_entity_properties_mapped_args(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
        )
        return self._bulk_update_entity_properties_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class BulkUpdateEntityProperties(BaseApi):

    async def abulk_update_entity_properties(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.abulk_update_entity_properties(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
            **kwargs,
        )
    
    
    def bulk_update_entity_properties(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.bulk_update_entity_properties(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._bulk_update_entity_properties_mapped_args(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
        )
        return await self._abulk_update_entity_properties_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        body: AppMigrationBulkUpdateEntityPropertiesRequest,
        atlassian_transfer_id: str,
        entity_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._bulk_update_entity_properties_mapped_args(
            body=body,
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
        )
        return self._bulk_update_entity_properties_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )
