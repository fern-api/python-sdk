# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ............core.datetime_utils import serialize_datetime
from .endpoint_path_part import EndpointPathPart
from .path_parameter import PathParameter


class EndpointPath(pydantic.BaseModel):
    parts: typing.List[EndpointPathPart]
    path_parameters: typing.List[PathParameter] = pydantic.Field(alias="pathParameters")

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