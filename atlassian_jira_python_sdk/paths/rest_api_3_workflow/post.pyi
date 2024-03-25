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

from atlassian_jira_python_sdk.model.create_workflow_details import CreateWorkflowDetails as CreateWorkflowDetailsSchema
from atlassian_jira_python_sdk.model.create_workflow_status_details import CreateWorkflowStatusDetails as CreateWorkflowStatusDetailsSchema
from atlassian_jira_python_sdk.model.create_workflow_transition_details import CreateWorkflowTransitionDetails as CreateWorkflowTransitionDetailsSchema
from atlassian_jira_python_sdk.model.workflow_ids import WorkflowIDs as WorkflowIDsSchema

from atlassian_jira_python_sdk.type.workflow_ids import WorkflowIDs
from atlassian_jira_python_sdk.type.create_workflow_status_details import CreateWorkflowStatusDetails
from atlassian_jira_python_sdk.type.create_workflow_details import CreateWorkflowDetails
from atlassian_jira_python_sdk.type.create_workflow_transition_details import CreateWorkflowTransitionDetails

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.create_workflow_transition_details import CreateWorkflowTransitionDetails as CreateWorkflowTransitionDetailsPydantic
from atlassian_jira_python_sdk.pydantic.workflow_ids import WorkflowIDs as WorkflowIDsPydantic
from atlassian_jira_python_sdk.pydantic.create_workflow_status_details import CreateWorkflowStatusDetails as CreateWorkflowStatusDetailsPydantic
from atlassian_jira_python_sdk.pydantic.create_workflow_details import CreateWorkflowDetails as CreateWorkflowDetailsPydantic

# body param
SchemaForRequestBodyApplicationJson = CreateWorkflowDetailsSchema


request_body_create_workflow_details = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = WorkflowIDsSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: WorkflowIDs


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: WorkflowIDs


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_workflow_transition_rule_configurations_mapped_args(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if statuses is not None:
            _body["statuses"] = statuses
        if transitions is not None:
            _body["transitions"] = transitions
        args.body = _body
        return args

    async def _acreate_workflow_transition_rule_configurations_oapg(
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
        Create workflow
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
            path_template='/rest/api/3/workflow',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_workflow_details.serialize(body, content_type)
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


    def _create_workflow_transition_rule_configurations_oapg(
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
        Create workflow
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
            path_template='/rest/api/3/workflow',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_workflow_details.serialize(body, content_type)
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


class CreateWorkflowTransitionRuleConfigurationsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="workflows")
    async def acreate_workflow_transition_rule_configurations(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_workflow_transition_rule_configurations_mapped_args(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )
        return await self._acreate_workflow_transition_rule_configurations_oapg(
            body=args.body,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="workflows")
    def create_workflow_transition_rule_configurations(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_workflow_transition_rule_configurations_mapped_args(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )
        return self._create_workflow_transition_rule_configurations_oapg(
            body=args.body,
        )

class CreateWorkflowTransitionRuleConfigurations(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="workflows")
    async def acreate_workflow_transition_rule_configurations(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> WorkflowIDsPydantic:
        raw_response = await self.raw.acreate_workflow_transition_rule_configurations(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
            **kwargs,
        )
        if validate:
            return WorkflowIDsPydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowIDsPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="workflows")
    def create_workflow_transition_rule_configurations(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
        validate: bool = False,
    ) -> WorkflowIDsPydantic:
        raw_response = self.raw.create_workflow_transition_rule_configurations(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )
        if validate:
            return WorkflowIDsPydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowIDsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="workflows")
    async def apost(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_workflow_transition_rule_configurations_mapped_args(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )
        return await self._acreate_workflow_transition_rule_configurations_oapg(
            body=args.body,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="workflows")
    def post(
        self,
        name: str,
        statuses: typing.List[CreateWorkflowStatusDetails],
        transitions: typing.List[CreateWorkflowTransitionDetails],
        description: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_workflow_transition_rule_configurations_mapped_args(
            name=name,
            statuses=statuses,
            transitions=transitions,
            description=description,
        )
        return self._create_workflow_transition_rule_configurations_oapg(
            body=args.body,
        )

