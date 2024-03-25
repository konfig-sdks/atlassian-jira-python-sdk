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
from atlassian_jira_python_sdk.model.page_bean_dashboard import PageBeanDashboard as PageBeanDashboardSchema

from atlassian_jira_python_sdk.type.error_collection import ErrorCollection
from atlassian_jira_python_sdk.type.page_bean_dashboard import PageBeanDashboard

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.page_bean_dashboard import PageBeanDashboard as PageBeanDashboardPydantic
from atlassian_jira_python_sdk.pydantic.error_collection import ErrorCollection as ErrorCollectionPydantic

from . import path

# Query params
DashboardNameSchema = schemas.StrSchema


class AccountIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 128
OwnerSchema = schemas.StrSchema
GroupnameSchema = schemas.StrSchema
GroupIdSchema = schemas.StrSchema
ProjectIdSchema = schemas.Int64Schema


class OrderBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "description": "DESCRIPTION",
            "-description": "DESCRIPTION",
            "+description": "DESCRIPTION",
            "favorite_count": "FAVORITE_COUNT",
            "-favorite_count": "FAVORITE_COUNT",
            "+favorite_count": "FAVORITE_COUNT",
            "id": "ID",
            "-id": "ID",
            "+id": "ID",
            "is_favorite": "IS_FAVORITE",
            "-is_favorite": "IS_FAVORITE",
            "+is_favorite": "IS_FAVORITE",
            "name": "NAME",
            "-name": "NAME",
            "+name": "NAME",
            "owner": "OWNER",
            "-owner": "OWNER",
            "+owner": "OWNER",
        }
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("description")
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("-description")
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("+description")
    
    @schemas.classproperty
    def FAVORITE_COUNT(cls):
        return cls("favorite_count")
    
    @schemas.classproperty
    def FAVORITE_COUNT(cls):
        return cls("-favorite_count")
    
    @schemas.classproperty
    def FAVORITE_COUNT(cls):
        return cls("+favorite_count")
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
    
    @schemas.classproperty
    def ID(cls):
        return cls("-id")
    
    @schemas.classproperty
    def ID(cls):
        return cls("+id")
    
    @schemas.classproperty
    def IS_FAVORITE(cls):
        return cls("is_favorite")
    
    @schemas.classproperty
    def IS_FAVORITE(cls):
        return cls("-is_favorite")
    
    @schemas.classproperty
    def IS_FAVORITE(cls):
        return cls("+is_favorite")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("name")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("-name")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("+name")
    
    @schemas.classproperty
    def OWNER(cls):
        return cls("owner")
    
    @schemas.classproperty
    def OWNER(cls):
        return cls("-owner")
    
    @schemas.classproperty
    def OWNER(cls):
        return cls("+owner")
StartAtSchema = schemas.Int64Schema
MaxResultsSchema = schemas.Int32Schema


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "active": "ACTIVE",
            "archived": "ARCHIVED",
            "deleted": "DELETED",
        }
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("active")
    
    @schemas.classproperty
    def ARCHIVED(cls):
        return cls("archived")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("deleted")
ExpandSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dashboardName': typing.Union[DashboardNameSchema, str, ],
        'accountId': typing.Union[AccountIdSchema, str, ],
        'owner': typing.Union[OwnerSchema, str, ],
        'groupname': typing.Union[GroupnameSchema, str, ],
        'groupId': typing.Union[GroupIdSchema, str, ],
        'projectId': typing.Union[ProjectIdSchema, decimal.Decimal, int, ],
        'orderBy': typing.Union[OrderBySchema, str, ],
        'startAt': typing.Union[StartAtSchema, decimal.Decimal, int, ],
        'maxResults': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'status': typing.Union[StatusSchema, str, ],
        'expand': typing.Union[ExpandSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dashboard_name = api_client.QueryParameter(
    name="dashboardName",
    style=api_client.ParameterStyle.FORM,
    schema=DashboardNameSchema,
    explode=True,
)
request_query_account_id = api_client.QueryParameter(
    name="accountId",
    style=api_client.ParameterStyle.FORM,
    schema=AccountIdSchema,
    explode=True,
)
request_query_owner = api_client.QueryParameter(
    name="owner",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerSchema,
    explode=True,
)
request_query_groupname = api_client.QueryParameter(
    name="groupname",
    style=api_client.ParameterStyle.FORM,
    schema=GroupnameSchema,
    explode=True,
)
request_query_group_id = api_client.QueryParameter(
    name="groupId",
    style=api_client.ParameterStyle.FORM,
    schema=GroupIdSchema,
    explode=True,
)
request_query_project_id = api_client.QueryParameter(
    name="projectId",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectIdSchema,
    explode=True,
)
request_query_order_by = api_client.QueryParameter(
    name="orderBy",
    style=api_client.ParameterStyle.FORM,
    schema=OrderBySchema,
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
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
_auth = [
    'OAuth2',
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = PageBeanDashboardSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PageBeanDashboard


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PageBeanDashboard


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _search_mapped_args(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if dashboard_name is not None:
            _query_params["dashboardName"] = dashboard_name
        if account_id is not None:
            _query_params["accountId"] = account_id
        if owner is not None:
            _query_params["owner"] = owner
        if groupname is not None:
            _query_params["groupname"] = groupname
        if group_id is not None:
            _query_params["groupId"] = group_id
        if project_id is not None:
            _query_params["projectId"] = project_id
        if order_by is not None:
            _query_params["orderBy"] = order_by
        if start_at is not None:
            _query_params["startAt"] = start_at
        if max_results is not None:
            _query_params["maxResults"] = max_results
        if status is not None:
            _query_params["status"] = status
        if expand is not None:
            _query_params["expand"] = expand
        args.query = _query_params
        return args

    async def _asearch_oapg(
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
        Search for dashboards
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dashboard_name,
            request_query_account_id,
            request_query_owner,
            request_query_groupname,
            request_query_group_id,
            request_query_project_id,
            request_query_order_by,
            request_query_start_at,
            request_query_max_results,
            request_query_status,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/dashboard/search',
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


    def _search_oapg(
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
        Search for dashboards
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dashboard_name,
            request_query_account_id,
            request_query_owner,
            request_query_groupname,
            request_query_group_id,
            request_query_project_id,
            request_query_order_by,
            request_query_start_at,
            request_query_max_results,
            request_query_status,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest/api/3/dashboard/search',
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


class SearchRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def search(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        return self._search_oapg(
            query_params=args.query,
        )

class Search(BaseApi):

    async def asearch(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PageBeanDashboardPydantic:
        raw_response = await self.raw.asearch(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
            **kwargs,
        )
        if validate:
            return PageBeanDashboardPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanDashboardPydantic, raw_response.body)
    
    
    def search(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PageBeanDashboardPydantic:
        raw_response = self.raw.search(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        if validate:
            return PageBeanDashboardPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanDashboardPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        dashboard_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        return self._search_oapg(
            query_params=args.query,
        )
