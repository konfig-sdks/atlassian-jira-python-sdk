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


class UpdateCustomFieldDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of a custom field.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class searcherKey(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CASCADINGSELECTSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher")
                
                @schemas.classproperty
                def DATERANGE(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:daterange")
                
                @schemas.classproperty
                def DATETIMERANGE(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:datetimerange")
                
                @schemas.classproperty
                def EXACTNUMBER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:exactnumber")
                
                @schemas.classproperty
                def EXACTTEXTSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher")
                
                @schemas.classproperty
                def GROUPPICKERSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher")
                
                @schemas.classproperty
                def LABELSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher")
                
                @schemas.classproperty
                def MULTISELECTSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher")
                
                @schemas.classproperty
                def NUMBERRANGE(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:numberrange")
                
                @schemas.classproperty
                def PROJECTSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher")
                
                @schemas.classproperty
                def TEXTSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:textsearcher")
                
                @schemas.classproperty
                def USERPICKERGROUPSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher")
                
                @schemas.classproperty
                def VERSIONSEARCHER(cls):
                    return cls("com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher")
            __annotations__ = {
                "description": description,
                "name": name,
                "searcherKey": searcherKey,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searcherKey"]) -> MetaOapg.properties.searcherKey: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "searcherKey", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searcherKey"]) -> typing.Union[MetaOapg.properties.searcherKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "searcherKey", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        searcherKey: typing.Union[MetaOapg.properties.searcherKey, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateCustomFieldDetails':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            searcherKey=searcherKey,
            _configuration=_configuration,
            **kwargs,
        )
