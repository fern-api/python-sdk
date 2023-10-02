# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...type.types.object_type import ObjectType


class HttpResponseBodyShape_Object(ObjectType):
    type: typing_extensions.Literal["object"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class HttpResponseBodyShape_Reference(pydantic.BaseModel):
    type: typing_extensions.Literal["reference"]
    value: TypeReference

    class Config:
        frozen = True
        smart_union = True


class HttpResponseBodyShape_FileDownload(pydantic.BaseModel):
    type: typing_extensions.Literal["fileDownload"]

    class Config:
        frozen = True
        smart_union = True


class HttpResponseBodyShape_StreamingText(pydantic.BaseModel):
    type: typing_extensions.Literal["streamingText"]

    class Config:
        frozen = True
        smart_union = True


HttpResponseBodyShape = typing.Union[
    HttpResponseBodyShape_Object,
    HttpResponseBodyShape_Reference,
    HttpResponseBodyShape_FileDownload,
    HttpResponseBodyShape_StreamingText,
]
from ...type.types.type_reference import TypeReference  # noqa: E402