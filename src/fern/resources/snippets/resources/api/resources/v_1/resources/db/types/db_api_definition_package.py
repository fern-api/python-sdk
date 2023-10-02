# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..........core.datetime_utils import serialize_datetime
from ...read.resources.type.types.type_id import TypeId
from ...read.resources.webhook.types.webhook_definition import WebhookDefinition
from ...read.types.subpackage_id import SubpackageId
from ..resources.endpoint.types.db_endpoint_definition import DbEndpointDefinition


class DbApiDefinitionPackage(pydantic.BaseModel):
    endpoints: typing.List[DbEndpointDefinition]
    webhooks: typing.Optional[typing.List[WebhookDefinition]]
    types: typing.List[TypeId]
    subpackages: typing.List[SubpackageId]
    points_to: typing.Optional[SubpackageId] = pydantic.Field(
        alias="pointsTo",
        description=(
            "if present, this package should be replaced with the provided subpackage\n" "in the docs navigation.\n"
        ),
    )

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
