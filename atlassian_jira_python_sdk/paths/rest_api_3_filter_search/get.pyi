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
from atlassian_jira_python_sdk.model.page_bean_filter_details import PageBeanFilterDetails as PageBeanFilterDetailsSchema

from atlassian_jira_python_sdk.type.error_collection import ErrorCollection
from atlassian_jira_python_sdk.type.page_bean_filter_details import PageBeanFilterDetails

from ...api_client import Dictionary
from atlassian_jira_python_sdk.pydantic.page_bean_filter_details import PageBeanFilterDetails as PageBeanFilterDetailsPydantic
from atlassian_jira_python_sdk.pydantic.error_collection import ErrorCollection as ErrorCollectionPydantic

# Query params
FilterNameSchema = schemas.StrSchema


class AccountIdSchema(
    schemas.StrSchema
):
    pass
OwnerSchema = schemas.StrSchema
GroupnameSchema = schemas.StrSchema
GroupIdSchema = schemas.StrSchema
ProjectIdSchema = schemas.Int64Schema


class IdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.Int64Schema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class OrderBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
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
    def FAVOURITE_COUNT(cls):
        return cls("favourite_count")
    
    @schemas.classproperty
    def FAVOURITE_COUNT(cls):
        return cls("-favourite_count")
    
    @schemas.classproperty
    def FAVOURITE_COUNT(cls):
        return cls("+favourite_count")
    
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
    def IS_FAVOURITE(cls):
        return cls("is_favourite")
    
    @schemas.classproperty
    def IS_FAVOURITE(cls):
        return cls("-is_favourite")
    
    @schemas.classproperty
    def IS_FAVOURITE(cls):
        return cls("+is_favourite")
    
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
    
    @schemas.classproperty
    def IS_SHARED(cls):
        return cls("is_shared")
    
    @schemas.classproperty
    def IS_SHARED(cls):
        return cls("-is_shared")
    
    @schemas.classproperty
    def IS_SHARED(cls):
        return cls("+is_shared")
StartAtSchema = schemas.Int64Schema
MaxResultsSchema = schemas.Int32Schema
ExpandSchema = schemas.StrSchema
OverrideSharePermissionsSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'filterName': typing.Union[FilterNameSchema, str, ],
        'accountId': typing.Union[AccountIdSchema, str, ],
        'owner': typing.Union[OwnerSchema, str, ],
        'groupname': typing.Union[GroupnameSchema, str, ],
        'groupId': typing.Union[GroupIdSchema, str, ],
        'projectId': typing.Union[ProjectIdSchema, decimal.Decimal, int, ],
        'id': typing.Union[IdSchema, list, tuple, ],
        'orderBy': typing.Union[OrderBySchema, str, ],
        'startAt': typing.Union[StartAtSchema, decimal.Decimal, int, ],
        'maxResults': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'expand': typing.Union[ExpandSchema, str, ],
        'overrideSharePermissions': typing.Union[OverrideSharePermissionsSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_filter_name = api_client.QueryParameter(
    name="filterName",
    style=api_client.ParameterStyle.FORM,
    schema=FilterNameSchema,
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
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
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
request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
request_query_override_share_permissions = api_client.QueryParameter(
    name="overrideSharePermissions",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideSharePermissionsSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PageBeanFilterDetailsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PageBeanFilterDetails


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PageBeanFilterDetails


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _search_mapped_args(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if filter_name is not None:
            _query_params["filterName"] = filter_name
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
        if id is not None:
            _query_params["id"] = id
        if order_by is not None:
            _query_params["orderBy"] = order_by
        if start_at is not None:
            _query_params["startAt"] = start_at
        if max_results is not None:
            _query_params["maxResults"] = max_results
        if expand is not None:
            _query_params["expand"] = expand
        if override_share_permissions is not None:
            _query_params["overrideSharePermissions"] = override_share_permissions
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
        Search for filters
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_name,
            request_query_account_id,
            request_query_owner,
            request_query_groupname,
            request_query_group_id,
            request_query_project_id,
            request_query_id,
            request_query_order_by,
            request_query_start_at,
            request_query_max_results,
            request_query_expand,
            request_query_override_share_permissions,
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
            path_template='/rest/api/3/filter/search',
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
        Search for filters
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_name,
            request_query_account_id,
            request_query_owner,
            request_query_groupname,
            request_query_group_id,
            request_query_project_id,
            request_query_id,
            request_query_order_by,
            request_query_start_at,
            request_query_max_results,
            request_query_expand,
            request_query_override_share_permissions,
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
            path_template='/rest/api/3/filter/search',
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
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def search(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return self._search_oapg(
            query_params=args.query,
        )

class Search(BaseApi):

    async def asearch(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> PageBeanFilterDetailsPydantic:
        raw_response = await self.raw.asearch(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
            **kwargs,
        )
        if validate:
            return PageBeanFilterDetailsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanFilterDetailsPydantic, raw_response.body)
    
    
    def search(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> PageBeanFilterDetailsPydantic:
        raw_response = self.raw.search(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        if validate:
            return PageBeanFilterDetailsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageBeanFilterDetailsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        filter_name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        groupname: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        id: typing.Optional[typing.List[int]] = None,
        order_by: typing.Optional[str] = None,
        start_at: typing.Optional[int] = None,
        max_results: typing.Optional[int] = None,
        expand: typing.Optional[str] = None,
        override_share_permissions: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id=id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return self._search_oapg(
            query_params=args.query,
        )

