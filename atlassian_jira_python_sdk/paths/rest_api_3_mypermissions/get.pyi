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
from atlassian_jira_python_sdk.model.permissions import Permissions as PermissionsSchema

from atlassian_jira_python_sdk.type.error_collection import ErrorCollection
from atlassian_jira_python_sdk.type.permissions import Permissions

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.permissions import Permissions as PermissionsPydantic
from atlassian_jira_python_sdk.pydantic.error_collection import ErrorCollection as ErrorCollectionPydantic

# Query params
ProjectKeySchema = schemas.StrSchema
ProjectIdSchema = schemas.StrSchema
IssueKeySchema = schemas.StrSchema
IssueIdSchema = schemas.StrSchema
PermissionsSchema = schemas.StrSchema
ProjectUuidSchema = schemas.StrSchema
ProjectConfigurationUuidSchema = schemas.StrSchema
CommentIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'projectKey': typing.Union[ProjectKeySchema, str, ],
        'projectId': typing.Union[ProjectIdSchema, str, ],
        'issueKey': typing.Union[IssueKeySchema, str, ],
        'issueId': typing.Union[IssueIdSchema, str, ],
        'permissions': typing.Union[PermissionsSchema, str, ],
        'projectUuid': typing.Union[ProjectUuidSchema, str, ],
        'projectConfigurationUuid': typing.Union[ProjectConfigurationUuidSchema, str, ],
        'commentId': typing.Union[CommentIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_project_key = api_client.QueryParameter(
    name="projectKey",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectKeySchema,
    explode=True,
)
request_query_project_id = api_client.QueryParameter(
    name="projectId",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectIdSchema,
    explode=True,
)
request_query_issue_key = api_client.QueryParameter(
    name="issueKey",
    style=api_client.ParameterStyle.FORM,
    schema=IssueKeySchema,
    explode=True,
)
request_query_issue_id = api_client.QueryParameter(
    name="issueId",
    style=api_client.ParameterStyle.FORM,
    schema=IssueIdSchema,
    explode=True,
)
request_query_permissions = api_client.QueryParameter(
    name="permissions",
    style=api_client.ParameterStyle.FORM,
    schema=PermissionsSchema,
    explode=True,
)
request_query_project_uuid = api_client.QueryParameter(
    name="projectUuid",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectUuidSchema,
    explode=True,
)
request_query_project_configuration_uuid = api_client.QueryParameter(
    name="projectConfigurationUuid",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectConfigurationUuidSchema,
    explode=True,
)
request_query_comment_id = api_client.QueryParameter(
    name="commentId",
    style=api_client.ParameterStyle.FORM,
    schema=CommentIdSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PermissionsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Permissions


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Permissions


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
SchemaFor404ResponseBodyApplicationJson = ErrorCollectionSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorCollection


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorCollection


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_user_permissions_mapped_args(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if project_key is not None:
            _query_params["projectKey"] = project_key
        if project_id is not None:
            _query_params["projectId"] = project_id
        if issue_key is not None:
            _query_params["issueKey"] = issue_key
        if issue_id is not None:
            _query_params["issueId"] = issue_id
        if permissions is not None:
            _query_params["permissions"] = permissions
        if project_uuid is not None:
            _query_params["projectUuid"] = project_uuid
        if project_configuration_uuid is not None:
            _query_params["projectConfigurationUuid"] = project_configuration_uuid
        if comment_id is not None:
            _query_params["commentId"] = comment_id
        args.query = _query_params
        return args

    async def _aget_user_permissions_oapg(
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
        Get my permissions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_key,
            request_query_project_id,
            request_query_issue_key,
            request_query_issue_id,
            request_query_permissions,
            request_query_project_uuid,
            request_query_project_configuration_uuid,
            request_query_comment_id,
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
            path_template='/rest/api/3/mypermissions',
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


    def _get_user_permissions_oapg(
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
        Get my permissions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_key,
            request_query_project_id,
            request_query_issue_key,
            request_query_issue_id,
            request_query_permissions,
            request_query_project_uuid,
            request_query_project_configuration_uuid,
            request_query_comment_id,
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
            path_template='/rest/api/3/mypermissions',
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


class GetUserPermissionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_permissions(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_permissions_mapped_args(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        return await self._aget_user_permissions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_permissions(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_permissions_mapped_args(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        return self._get_user_permissions_oapg(
            query_params=args.query,
        )

class GetUserPermissions(BaseApi):

    async def aget_user_permissions(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PermissionsPydantic:
        raw_response = await self.raw.aget_user_permissions(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
            **kwargs,
        )
        if validate:
            return PermissionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PermissionsPydantic, raw_response.body)
    
    
    def get_user_permissions(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PermissionsPydantic:
        raw_response = self.raw.get_user_permissions(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        if validate:
            return PermissionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PermissionsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_permissions_mapped_args(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        return await self._aget_user_permissions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        project_key: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        issue_key: typing.Optional[str] = None,
        issue_id: typing.Optional[str] = None,
        permissions: typing.Optional[str] = None,
        project_uuid: typing.Optional[str] = None,
        project_configuration_uuid: typing.Optional[str] = None,
        comment_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_permissions_mapped_args(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        return self._get_user_permissions_oapg(
            query_params=args.query,
        )

