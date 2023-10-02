# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..........core.datetime_utils import serialize_datetime
from .font_config import FontConfig


class DocsTypographyConfig(pydantic.BaseModel):
    headings_font: typing.Optional[FontConfig] = pydantic.Field(alias="headingsFont")
    body_font: typing.Optional[FontConfig] = pydantic.Field(alias="bodyFont")
    code_font: typing.Optional[FontConfig] = pydantic.Field(alias="codeFont")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
