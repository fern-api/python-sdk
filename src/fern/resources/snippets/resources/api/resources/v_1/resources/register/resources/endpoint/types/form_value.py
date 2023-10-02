# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class FormValue_Json(pydantic.BaseModel):
    type: typing_extensions.Literal["json"]
    value: typing.Any

    class Config:
        frozen = True
        smart_union = True


class FormValue_Filename(pydantic.BaseModel):
    type: typing_extensions.Literal["filename"]
    value: str

    class Config:
        frozen = True
        smart_union = True


FormValue = typing.Union[FormValue_Json, FormValue_Filename]
