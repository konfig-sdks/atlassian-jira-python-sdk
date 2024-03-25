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


class TaskProgressBeanObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about a task.
    """


    class MetaOapg:
        required = {
            "submittedBy",
            "submitted",
            "lastUpdate",
            "progress",
            "self",
            "id",
            "elapsedRuntime",
            "status",
        }
        
        class properties:
            elapsedRuntime = schemas.Int64Schema
            id = schemas.StrSchema
            lastUpdate = schemas.Int64Schema
            progress = schemas.Int64Schema
            _self = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENQUEUED(cls):
                    return cls("ENQUEUED")
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def CANCEL_REQUESTED(cls):
                    return cls("CANCEL_REQUESTED")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("CANCELLED")
                
                @schemas.classproperty
                def DEAD(cls):
                    return cls("DEAD")
            submitted = schemas.Int64Schema
            submittedBy = schemas.Int64Schema
            description = schemas.StrSchema
            finished = schemas.Int64Schema
            message = schemas.StrSchema
            result = schemas.AnyTypeSchema
            started = schemas.Int64Schema
            __annotations__ = {
                "elapsedRuntime": elapsedRuntime,
                "id": id,
                "lastUpdate": lastUpdate,
                "progress": progress,
                "self": _self,
                "status": status,
                "submitted": submitted,
                "submittedBy": submittedBy,
                "description": description,
                "finished": finished,
                "message": message,
                "result": result,
                "started": started,
            }
    
    submittedBy: MetaOapg.properties.submittedBy
    submitted: MetaOapg.properties.submitted
    lastUpdate: MetaOapg.properties.lastUpdate
    progress: MetaOapg.properties.progress
    id: MetaOapg.properties.id
    elapsedRuntime: MetaOapg.properties.elapsedRuntime
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elapsedRuntime"]) -> MetaOapg.properties.elapsedRuntime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitted"]) -> MetaOapg.properties.submitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedBy"]) -> MetaOapg.properties.submittedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finished"]) -> MetaOapg.properties.finished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started"]) -> MetaOapg.properties.started: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["elapsedRuntime", "id", "lastUpdate", "progress", "self", "status", "submitted", "submittedBy", "description", "finished", "message", "result", "started", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elapsedRuntime"]) -> MetaOapg.properties.elapsedRuntime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitted"]) -> MetaOapg.properties.submitted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedBy"]) -> MetaOapg.properties.submittedBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finished"]) -> typing.Union[MetaOapg.properties.finished, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started"]) -> typing.Union[MetaOapg.properties.started, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["elapsedRuntime", "id", "lastUpdate", "progress", "self", "status", "submitted", "submittedBy", "description", "finished", "message", "result", "started", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        submittedBy: typing.Union[MetaOapg.properties.submittedBy, decimal.Decimal, int, ],
        submitted: typing.Union[MetaOapg.properties.submitted, decimal.Decimal, int, ],
        lastUpdate: typing.Union[MetaOapg.properties.lastUpdate, decimal.Decimal, int, ],
        progress: typing.Union[MetaOapg.properties.progress, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        elapsedRuntime: typing.Union[MetaOapg.properties.elapsedRuntime, decimal.Decimal, int, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        finished: typing.Union[MetaOapg.properties.finished, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        result: typing.Union[MetaOapg.properties.result, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        started: typing.Union[MetaOapg.properties.started, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskProgressBeanObject':
        return super().__new__(
            cls,
            *args,
            submittedBy=submittedBy,
            submitted=submitted,
            lastUpdate=lastUpdate,
            progress=progress,
            id=id,
            elapsedRuntime=elapsedRuntime,
            status=status,
            description=description,
            finished=finished,
            message=message,
            result=result,
            started=started,
            _configuration=_configuration,
            **kwargs,
        )
