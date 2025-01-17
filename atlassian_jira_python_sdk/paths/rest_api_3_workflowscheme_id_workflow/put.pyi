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

from atlassian_jira_python_sdk.model.issue_types_workflow_mapping import IssueTypesWorkflowMapping as IssueTypesWorkflowMappingSchema
from atlassian_jira_python_sdk.model.workflow_scheme import WorkflowScheme as WorkflowSchemeSchema
from atlassian_jira_python_sdk.model.issue_types_workflow_mapping_issue_types import IssueTypesWorkflowMappingIssueTypes as IssueTypesWorkflowMappingIssueTypesSchema

from atlassian_jira_python_sdk.type.workflow_scheme import WorkflowScheme
from atlassian_jira_python_sdk.type.issue_types_workflow_mapping_issue_types import IssueTypesWorkflowMappingIssueTypes
from atlassian_jira_python_sdk.type.issue_types_workflow_mapping import IssueTypesWorkflowMapping

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.issue_types_workflow_mapping_issue_types import IssueTypesWorkflowMappingIssueTypes as IssueTypesWorkflowMappingIssueTypesPydantic
from atlassian_jira_python_sdk.pydantic.issue_types_workflow_mapping import IssueTypesWorkflowMapping as IssueTypesWorkflowMappingPydantic
from atlassian_jira_python_sdk.pydantic.workflow_scheme import WorkflowScheme as WorkflowSchemePydantic

# Query params
WorkflowNameSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'workflowName': typing.Union[WorkflowNameSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_workflow_name = api_client.QueryParameter(
    name="workflowName",
    style=api_client.ParameterStyle.FORM,
    schema=WorkflowNameSchema,
    required=True,
    explode=True,
)
# Path params
IdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, decimal.Decimal, int, ],
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


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = IssueTypesWorkflowMappingSchema


request_body_issue_types_workflow_mapping = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = WorkflowSchemeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WorkflowScheme


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WorkflowScheme


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

    def _set_issue_types_for_workflow_in_scheme_mapped_args(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if default_mapping is not None:
            _body["defaultMapping"] = default_mapping
        if issue_types is not None:
            _body["issueTypes"] = issue_types
        if update_draft_if_needed is not None:
            _body["updateDraftIfNeeded"] = update_draft_if_needed
        if workflow is not None:
            _body["workflow"] = workflow
        args.body = _body
        if workflow_name is not None:
            _query_params["workflowName"] = workflow_name
        if id is not None:
            _path_params["id"] = id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aset_issue_types_for_workflow_in_scheme_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Set issue types for workflow in workflow scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
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
            request_query_workflow_name,
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
            path_template='/rest/api/3/workflowscheme/{id}/workflow',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_types_workflow_mapping.serialize(body, content_type)
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


    def _set_issue_types_for_workflow_in_scheme_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Set issue types for workflow in workflow scheme
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
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
            request_query_workflow_name,
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
            path_template='/rest/api/3/workflowscheme/{id}/workflow',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_issue_types_workflow_mapping.serialize(body, content_type)
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


class SetIssueTypesForWorkflowInSchemeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aset_issue_types_for_workflow_in_scheme(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_issue_types_for_workflow_in_scheme_mapped_args(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )
        return await self._aset_issue_types_for_workflow_in_scheme_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def set_issue_types_for_workflow_in_scheme(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_issue_types_for_workflow_in_scheme_mapped_args(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )
        return self._set_issue_types_for_workflow_in_scheme_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class SetIssueTypesForWorkflowInScheme(BaseApi):

    async def aset_issue_types_for_workflow_in_scheme(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> WorkflowSchemePydantic:
        raw_response = await self.raw.aset_issue_types_for_workflow_in_scheme(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
            **kwargs,
        )
        if validate:
            return WorkflowSchemePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowSchemePydantic, raw_response.body)
    
    
    def set_issue_types_for_workflow_in_scheme(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
        validate: bool = False,
    ) -> WorkflowSchemePydantic:
        raw_response = self.raw.set_issue_types_for_workflow_in_scheme(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )
        if validate:
            return WorkflowSchemePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowSchemePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_issue_types_for_workflow_in_scheme_mapped_args(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )
        return await self._aset_issue_types_for_workflow_in_scheme_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id: int,
        workflow_name: str,
        default_mapping: typing.Optional[bool] = None,
        issue_types: typing.Optional[IssueTypesWorkflowMappingIssueTypes] = None,
        update_draft_if_needed: typing.Optional[bool] = None,
        workflow: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_issue_types_for_workflow_in_scheme_mapped_args(
            id=id,
            workflow_name=workflow_name,
            default_mapping=default_mapping,
            issue_types=issue_types,
            update_draft_if_needed=update_draft_if_needed,
            workflow=workflow,
        )
        return self._set_issue_types_for_workflow_in_scheme_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

