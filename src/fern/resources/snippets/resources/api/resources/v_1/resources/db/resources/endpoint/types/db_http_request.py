# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ............core.datetime_utils import serialize_datetime
from .....read.resources.commons.types.with_description import WithDescription
from .....read.resources.endpoint.types.http_request_body_shape import HttpRequestBodyShape


class DbHttpRequest(WithDescription):
    content_type: typing.Optional[str] = pydantic.Field(alias="contentType")
    type: HttpRequestBodyShape

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