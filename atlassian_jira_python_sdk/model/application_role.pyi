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


class ApplicationRole(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of an application role.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def defaultGroups() -> typing.Type['ApplicationRoleDefaultGroups']:
                return ApplicationRoleDefaultGroups
            
            
            class defaultGroupsDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GroupName']:
                        return GroupName
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GroupName'], typing.List['GroupName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultGroupsDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GroupName':
                    return super().__getitem__(i)
            defined = schemas.BoolSchema
            
            
            class groupDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GroupName']:
                        return GroupName
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GroupName'], typing.List['GroupName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groupDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GroupName':
                    return super().__getitem__(i)
        
            @staticmethod
            def groups() -> typing.Type['ApplicationRoleGroups']:
                return ApplicationRoleGroups
            hasUnlimitedSeats = schemas.BoolSchema
            key = schemas.StrSchema
            name = schemas.StrSchema
            numberOfSeats = schemas.Int32Schema
            platform = schemas.BoolSchema
            remainingSeats = schemas.Int32Schema
            selectedByDefault = schemas.BoolSchema
            userCount = schemas.Int32Schema
            userCountDescription = schemas.StrSchema
            __annotations__ = {
                "defaultGroups": defaultGroups,
                "defaultGroupsDetails": defaultGroupsDetails,
                "defined": defined,
                "groupDetails": groupDetails,
                "groups": groups,
                "hasUnlimitedSeats": hasUnlimitedSeats,
                "key": key,
                "name": name,
                "numberOfSeats": numberOfSeats,
                "platform": platform,
                "remainingSeats": remainingSeats,
                "selectedByDefault": selectedByDefault,
                "userCount": userCount,
                "userCountDescription": userCountDescription,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultGroups"]) -> 'ApplicationRoleDefaultGroups': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultGroupsDetails"]) -> MetaOapg.properties.defaultGroupsDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defined"]) -> MetaOapg.properties.defined: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupDetails"]) -> MetaOapg.properties.groupDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> 'ApplicationRoleGroups': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasUnlimitedSeats"]) -> MetaOapg.properties.hasUnlimitedSeats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfSeats"]) -> MetaOapg.properties.numberOfSeats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remainingSeats"]) -> MetaOapg.properties.remainingSeats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedByDefault"]) -> MetaOapg.properties.selectedByDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userCount"]) -> MetaOapg.properties.userCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userCountDescription"]) -> MetaOapg.properties.userCountDescription: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultGroups", "defaultGroupsDetails", "defined", "groupDetails", "groups", "hasUnlimitedSeats", "key", "name", "numberOfSeats", "platform", "remainingSeats", "selectedByDefault", "userCount", "userCountDescription", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultGroups"]) -> typing.Union['ApplicationRoleDefaultGroups', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultGroupsDetails"]) -> typing.Union[MetaOapg.properties.defaultGroupsDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defined"]) -> typing.Union[MetaOapg.properties.defined, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupDetails"]) -> typing.Union[MetaOapg.properties.groupDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union['ApplicationRoleGroups', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasUnlimitedSeats"]) -> typing.Union[MetaOapg.properties.hasUnlimitedSeats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfSeats"]) -> typing.Union[MetaOapg.properties.numberOfSeats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> typing.Union[MetaOapg.properties.platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remainingSeats"]) -> typing.Union[MetaOapg.properties.remainingSeats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedByDefault"]) -> typing.Union[MetaOapg.properties.selectedByDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userCount"]) -> typing.Union[MetaOapg.properties.userCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userCountDescription"]) -> typing.Union[MetaOapg.properties.userCountDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultGroups", "defaultGroupsDetails", "defined", "groupDetails", "groups", "hasUnlimitedSeats", "key", "name", "numberOfSeats", "platform", "remainingSeats", "selectedByDefault", "userCount", "userCountDescription", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        defaultGroups: typing.Union['ApplicationRoleDefaultGroups', schemas.Unset] = schemas.unset,
        defaultGroupsDetails: typing.Union[MetaOapg.properties.defaultGroupsDetails, list, tuple, schemas.Unset] = schemas.unset,
        defined: typing.Union[MetaOapg.properties.defined, bool, schemas.Unset] = schemas.unset,
        groupDetails: typing.Union[MetaOapg.properties.groupDetails, list, tuple, schemas.Unset] = schemas.unset,
        groups: typing.Union['ApplicationRoleGroups', schemas.Unset] = schemas.unset,
        hasUnlimitedSeats: typing.Union[MetaOapg.properties.hasUnlimitedSeats, bool, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        numberOfSeats: typing.Union[MetaOapg.properties.numberOfSeats, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        platform: typing.Union[MetaOapg.properties.platform, bool, schemas.Unset] = schemas.unset,
        remainingSeats: typing.Union[MetaOapg.properties.remainingSeats, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        selectedByDefault: typing.Union[MetaOapg.properties.selectedByDefault, bool, schemas.Unset] = schemas.unset,
        userCount: typing.Union[MetaOapg.properties.userCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userCountDescription: typing.Union[MetaOapg.properties.userCountDescription, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationRole':
        return super().__new__(
            cls,
            *args,
            defaultGroups=defaultGroups,
            defaultGroupsDetails=defaultGroupsDetails,
            defined=defined,
            groupDetails=groupDetails,
            groups=groups,
            hasUnlimitedSeats=hasUnlimitedSeats,
            key=key,
            name=name,
            numberOfSeats=numberOfSeats,
            platform=platform,
            remainingSeats=remainingSeats,
            selectedByDefault=selectedByDefault,
            userCount=userCount,
            userCountDescription=userCountDescription,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.application_role_default_groups import ApplicationRoleDefaultGroups
from atlassian_jira_python_sdk.model.application_role_groups import ApplicationRoleGroups
from atlassian_jira_python_sdk.model.group_name import GroupName