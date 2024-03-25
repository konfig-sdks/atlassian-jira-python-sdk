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


class SoftwareNavigationInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            boardId = schemas.Int64Schema
            boardName = schemas.StrSchema
            simpleBoard = schemas.BoolSchema
            totalBoardsInProject = schemas.Int64Schema
            __annotations__ = {
                "boardId": boardId,
                "boardName": boardName,
                "simpleBoard": simpleBoard,
                "totalBoardsInProject": totalBoardsInProject,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boardId"]) -> MetaOapg.properties.boardId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boardName"]) -> MetaOapg.properties.boardName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simpleBoard"]) -> MetaOapg.properties.simpleBoard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalBoardsInProject"]) -> MetaOapg.properties.totalBoardsInProject: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["boardId", "boardName", "simpleBoard", "totalBoardsInProject", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boardId"]) -> typing.Union[MetaOapg.properties.boardId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boardName"]) -> typing.Union[MetaOapg.properties.boardName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simpleBoard"]) -> typing.Union[MetaOapg.properties.simpleBoard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalBoardsInProject"]) -> typing.Union[MetaOapg.properties.totalBoardsInProject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["boardId", "boardName", "simpleBoard", "totalBoardsInProject", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        boardId: typing.Union[MetaOapg.properties.boardId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        boardName: typing.Union[MetaOapg.properties.boardName, str, schemas.Unset] = schemas.unset,
        simpleBoard: typing.Union[MetaOapg.properties.simpleBoard, bool, schemas.Unset] = schemas.unset,
        totalBoardsInProject: typing.Union[MetaOapg.properties.totalBoardsInProject, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SoftwareNavigationInfo':
        return super().__new__(
            cls,
            *args,
            boardId=boardId,
            boardName=boardName,
            simpleBoard=simpleBoard,
            totalBoardsInProject=totalBoardsInProject,
            _configuration=_configuration,
            **kwargs,
        )