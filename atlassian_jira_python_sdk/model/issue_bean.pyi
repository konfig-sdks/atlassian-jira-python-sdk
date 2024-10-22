# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

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


class IssueBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about an issue.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def changelog() -> typing.Type['PageOfChangelogs']:
                return PageOfChangelogs
        
            @staticmethod
            def editmeta() -> typing.Type['IssueUpdateMetadata']:
                return IssueUpdateMetadata
            expand = schemas.StrSchema
        
            @staticmethod
            def fields() -> typing.Type['IssueBeanFields']:
                return IssueBeanFields
        
            @staticmethod
            def fieldsToInclude() -> typing.Type['IncludedFields']:
                return IncludedFields
            id = schemas.StrSchema
            key = schemas.StrSchema
        
            @staticmethod
            def names() -> typing.Type['IssueBeanNames']:
                return IssueBeanNames
        
            @staticmethod
            def operations() -> typing.Type['Operations']:
                return Operations
        
            @staticmethod
            def properties() -> typing.Type['IssueBeanProperties']:
                return IssueBeanProperties
        
            @staticmethod
            def renderedFields() -> typing.Type['IssueBeanRenderedFields']:
                return IssueBeanRenderedFields
        
            @staticmethod
            def schema() -> typing.Type['IssueBeanSchema']:
                return IssueBeanSchema
            _self = schemas.StrSchema
            
            
            class transitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IssueTransition']:
                        return IssueTransition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IssueTransition'], typing.List['IssueTransition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transitions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IssueTransition':
                    return super().__getitem__(i)
        
            @staticmethod
            def versionedRepresentations() -> typing.Type['IssueBeanVersionedRepresentations']:
                return IssueBeanVersionedRepresentations
            __annotations__ = {
                "changelog": changelog,
                "editmeta": editmeta,
                "expand": expand,
                "fields": fields,
                "fieldsToInclude": fieldsToInclude,
                "id": id,
                "key": key,
                "names": names,
                "operations": operations,
                "properties": properties,
                "renderedFields": renderedFields,
                "schema": schema,
                "self": _self,
                "transitions": transitions,
                "versionedRepresentations": versionedRepresentations,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changelog"]) -> 'PageOfChangelogs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editmeta"]) -> 'IssueUpdateMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expand"]) -> MetaOapg.properties.expand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'IssueBeanFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldsToInclude"]) -> 'IncludedFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["names"]) -> 'IssueBeanNames': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operations"]) -> 'Operations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'IssueBeanProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renderedFields"]) -> 'IssueBeanRenderedFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> 'IssueBeanSchema': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transitions"]) -> MetaOapg.properties.transitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionedRepresentations"]) -> 'IssueBeanVersionedRepresentations': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["changelog", "editmeta", "expand", "fields", "fieldsToInclude", "id", "key", "names", "operations", "properties", "renderedFields", "schema", "self", "transitions", "versionedRepresentations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changelog"]) -> typing.Union['PageOfChangelogs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editmeta"]) -> typing.Union['IssueUpdateMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expand"]) -> typing.Union[MetaOapg.properties.expand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['IssueBeanFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldsToInclude"]) -> typing.Union['IncludedFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["names"]) -> typing.Union['IssueBeanNames', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operations"]) -> typing.Union['Operations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union['IssueBeanProperties', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renderedFields"]) -> typing.Union['IssueBeanRenderedFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> typing.Union['IssueBeanSchema', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transitions"]) -> typing.Union[MetaOapg.properties.transitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionedRepresentations"]) -> typing.Union['IssueBeanVersionedRepresentations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["changelog", "editmeta", "expand", "fields", "fieldsToInclude", "id", "key", "names", "operations", "properties", "renderedFields", "schema", "self", "transitions", "versionedRepresentations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        changelog: typing.Union['PageOfChangelogs', schemas.Unset] = schemas.unset,
        editmeta: typing.Union['IssueUpdateMetadata', schemas.Unset] = schemas.unset,
        expand: typing.Union[MetaOapg.properties.expand, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['IssueBeanFields', schemas.Unset] = schemas.unset,
        fieldsToInclude: typing.Union['IncludedFields', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        names: typing.Union['IssueBeanNames', schemas.Unset] = schemas.unset,
        operations: typing.Union['Operations', schemas.Unset] = schemas.unset,
        properties: typing.Union['IssueBeanProperties', schemas.Unset] = schemas.unset,
        renderedFields: typing.Union['IssueBeanRenderedFields', schemas.Unset] = schemas.unset,
        schema: typing.Union['IssueBeanSchema', schemas.Unset] = schemas.unset,
        transitions: typing.Union[MetaOapg.properties.transitions, list, tuple, schemas.Unset] = schemas.unset,
        versionedRepresentations: typing.Union['IssueBeanVersionedRepresentations', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueBean':
        return super().__new__(
            cls,
            *args,
            changelog=changelog,
            editmeta=editmeta,
            expand=expand,
            fields=fields,
            fieldsToInclude=fieldsToInclude,
            id=id,
            key=key,
            names=names,
            operations=operations,
            properties=properties,
            renderedFields=renderedFields,
            schema=schema,
            transitions=transitions,
            versionedRepresentations=versionedRepresentations,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.included_fields import IncludedFields
from atlassian_jira_python_sdk.model.issue_bean_fields import IssueBeanFields
from atlassian_jira_python_sdk.model.issue_bean_names import IssueBeanNames
from atlassian_jira_python_sdk.model.issue_bean_properties import IssueBeanProperties
from atlassian_jira_python_sdk.model.issue_bean_rendered_fields import IssueBeanRenderedFields
from atlassian_jira_python_sdk.model.issue_bean_schema import IssueBeanSchema
from atlassian_jira_python_sdk.model.issue_bean_versioned_representations import IssueBeanVersionedRepresentations
from atlassian_jira_python_sdk.model.issue_transition import IssueTransition
from atlassian_jira_python_sdk.model.issue_update_metadata import IssueUpdateMetadata
from atlassian_jira_python_sdk.model.operations import Operations
from atlassian_jira_python_sdk.model.page_of_changelogs import PageOfChangelogs
