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

from atlassian_jira_python_sdk.model.visibility import Visibility as VisibilitySchema
from atlassian_jira_python_sdk.model.user_details import UserDetails as UserDetailsSchema
from atlassian_jira_python_sdk.model.entity_property import EntityProperty as EntityPropertySchema
from atlassian_jira_python_sdk.model.comment import Comment as CommentSchema

from atlassian_jira_python_sdk.type.visibility import Visibility
from atlassian_jira_python_sdk.type.entity_property import EntityProperty
from atlassian_jira_python_sdk.type.comment import Comment
from atlassian_jira_python_sdk.type.user_details import UserDetails

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.visibility import Visibility as VisibilityPydantic
from atlassian_jira_python_sdk.pydantic.comment import Comment as CommentPydantic
from atlassian_jira_python_sdk.pydantic.entity_property import EntityProperty as EntityPropertyPydantic
from atlassian_jira_python_sdk.pydantic.user_details import UserDetails as UserDetailsPydantic

from . import path

# Query params
NotifyUsersSchema = schemas.BoolSchema
OverrideEditableFlagSchema = schemas.BoolSchema
ExpandSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'notifyUsers': typing.Union[NotifyUsersSchema, bool, ],
        'overrideEditableFlag': typing.Union[OverrideEditableFlagSchema, bool, ],
        'expand': typing.Union[ExpandSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_notify_users = api_client.QueryParameter(
    name="notifyUsers",
    style=api_client.ParameterStyle.FORM,
    schema=NotifyUsersSchema,
    explode=True,
)
request_query_override_editable_flag = api_client.QueryParameter(
    name="overrideEditableFlag",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideEditableFlagSchema,
    explode=True,
)
request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
# Path params
IssueIdOrKeySchema = schemas.StrSchema
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'issueIdOrKey': typing.Union[IssueIdOrKeySchema, str, ],
        'id': typing.Union[IdSchema, str, ],
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
request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CommentSchema


request_body_comment = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = CommentSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Comment


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Comment


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
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_comment_mapped_args(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if author is not None:
            _body["author"] = author
        if body is not None:
            _body["body"] = body
        if created is not None:
            _body["created"] = created
        if id is not None:
            _body["id"] = id
        if jsd_author_can_see_request is not None:
            _body["jsdAuthorCanSeeRequest"] = jsd_author_can_see_request
        if jsd_public is not None:
            _body["jsdPublic"] = jsd_public
        if properties is not None:
            _body["properties"] = properties
        if rendered_body is not None:
            _body["renderedBody"] = rendered_body
        if _self is not None:
            _body["self"] = _self
        if update_author is not None:
            _body["updateAuthor"] = update_author
        if updated is not None:
            _body["updated"] = updated
        if visibility is not None:
            _body["visibility"] = visibility
        args.body = _body
        if notify_users is not None:
            _query_params["notifyUsers"] = notify_users
        if override_editable_flag is not None:
            _query_params["overrideEditableFlag"] = override_editable_flag
        if expand is not None:
            _query_params["expand"] = expand
        if issue_id_or_key is not None:
            _path_params["issueIdOrKey"] = issue_id_or_key
        if id is not None:
            _path_params["id"] = id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_comment_oapg(
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
        Update comment
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
            request_query_notify_users,
            request_query_override_editable_flag,
            request_query_expand,
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
            path_template='/rest/api/3/issue/{issueIdOrKey}/comment/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_comment.serialize(body, content_type)
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


    def _update_comment_oapg(
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
        Update comment
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
            request_query_notify_users,
            request_query_override_editable_flag,
            request_query_expand,
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
            path_template='/rest/api/3/issue/{issueIdOrKey}/comment/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_comment.serialize(body, content_type)
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


class UpdateCommentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_comment(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_comment_mapped_args(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
        )
        return await self._aupdate_comment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_comment(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_comment_mapped_args(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
        )
        return self._update_comment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateComment(BaseApi):

    async def aupdate_comment(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CommentPydantic:
        raw_response = await self.raw.aupdate_comment(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
            **kwargs,
        )
        if validate:
            return CommentPydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentPydantic, raw_response.body)
    
    
    def update_comment(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CommentPydantic:
        raw_response = self.raw.update_comment(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
        )
        if validate:
            return CommentPydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_comment_mapped_args(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
        )
        return await self._aupdate_comment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        issue_id_or_key: str,
        id: str,
        author: typing.Optional[UserDetails] = None,
        body: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        jsd_author_can_see_request: typing.Optional[bool] = None,
        jsd_public: typing.Optional[bool] = None,
        properties: typing.Optional[typing.List[EntityProperty]] = None,
        rendered_body: typing.Optional[str] = None,
        _self: typing.Optional[str] = None,
        update_author: typing.Optional[UserDetails] = None,
        updated: typing.Optional[datetime] = None,
        visibility: typing.Optional[Visibility] = None,
        notify_users: typing.Optional[bool] = None,
        override_editable_flag: typing.Optional[bool] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_comment_mapped_args(
            issue_id_or_key=issue_id_or_key,
            id=id,
            author=author,
            body=body,
            created=created,
            id=id,
            jsd_author_can_see_request=jsd_author_can_see_request,
            jsd_public=jsd_public,
            properties=properties,
            rendered_body=rendered_body,
            _self=_self,
            update_author=update_author,
            updated=updated,
            visibility=visibility,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
        )
        return self._update_comment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

