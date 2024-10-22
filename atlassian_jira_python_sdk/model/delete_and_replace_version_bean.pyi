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


class DeleteAndReplaceVersionBean(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class customFieldReplacementList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomFieldReplacement']:
                        return CustomFieldReplacement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomFieldReplacement'], typing.List['CustomFieldReplacement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customFieldReplacementList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomFieldReplacement':
                    return super().__getitem__(i)
            moveAffectedIssuesTo = schemas.Int64Schema
            moveFixIssuesTo = schemas.Int64Schema
            __annotations__ = {
                "customFieldReplacementList": customFieldReplacementList,
                "moveAffectedIssuesTo": moveAffectedIssuesTo,
                "moveFixIssuesTo": moveFixIssuesTo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldReplacementList"]) -> MetaOapg.properties.customFieldReplacementList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moveAffectedIssuesTo"]) -> MetaOapg.properties.moveAffectedIssuesTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moveFixIssuesTo"]) -> MetaOapg.properties.moveFixIssuesTo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customFieldReplacementList", "moveAffectedIssuesTo", "moveFixIssuesTo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldReplacementList"]) -> typing.Union[MetaOapg.properties.customFieldReplacementList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moveAffectedIssuesTo"]) -> typing.Union[MetaOapg.properties.moveAffectedIssuesTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moveFixIssuesTo"]) -> typing.Union[MetaOapg.properties.moveFixIssuesTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customFieldReplacementList", "moveAffectedIssuesTo", "moveFixIssuesTo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customFieldReplacementList: typing.Union[MetaOapg.properties.customFieldReplacementList, list, tuple, schemas.Unset] = schemas.unset,
        moveAffectedIssuesTo: typing.Union[MetaOapg.properties.moveAffectedIssuesTo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        moveFixIssuesTo: typing.Union[MetaOapg.properties.moveFixIssuesTo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeleteAndReplaceVersionBean':
        return super().__new__(
            cls,
            *args,
            customFieldReplacementList=customFieldReplacementList,
            moveAffectedIssuesTo=moveAffectedIssuesTo,
            moveFixIssuesTo=moveFixIssuesTo,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.custom_field_replacement import CustomFieldReplacement
