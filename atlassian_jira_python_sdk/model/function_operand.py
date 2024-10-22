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


class FunctionOperand(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An operand that is a function. See [Advanced searching - functions reference](https://confluence.atlassian.com/x/dwiiLQ) for more information about JQL functions.
    """


    class MetaOapg:
        required = {
            "function",
            "arguments",
        }
        
        class properties:
        
            @staticmethod
            def arguments() -> typing.Type['FunctionOperandArguments']:
                return FunctionOperandArguments
            function = schemas.StrSchema
            encodedOperand = schemas.StrSchema
            __annotations__ = {
                "arguments": arguments,
                "function": function,
                "encodedOperand": encodedOperand,
            }
    
    function: MetaOapg.properties.function
    arguments: 'FunctionOperandArguments'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arguments"]) -> 'FunctionOperandArguments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["function"]) -> MetaOapg.properties.function: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encodedOperand"]) -> MetaOapg.properties.encodedOperand: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["arguments", "function", "encodedOperand", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arguments"]) -> 'FunctionOperandArguments': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["function"]) -> MetaOapg.properties.function: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encodedOperand"]) -> typing.Union[MetaOapg.properties.encodedOperand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["arguments", "function", "encodedOperand", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        function: typing.Union[MetaOapg.properties.function, str, ],
        arguments: 'FunctionOperandArguments',
        encodedOperand: typing.Union[MetaOapg.properties.encodedOperand, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionOperand':
        return super().__new__(
            cls,
            *args,
            function=function,
            arguments=arguments,
            encodedOperand=encodedOperand,
            _configuration=_configuration,
            **kwargs,
        )

from atlassian_jira_python_sdk.model.function_operand_arguments import FunctionOperandArguments
