# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..........core.datetime_utils import serialize_datetime
from .file_id import FileId


class FileS3UploadUrl(pydantic.BaseModel):
    upload_url: str = pydantic.Field(alias="uploadUrl")
    file_id: FileId = pydantic.Field(
        alias="fileId",
        description=("When reading docs we will return a map<FileId, URL> that you can use to look up the docs.\n"),
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
