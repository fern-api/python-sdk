# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..........core.datetime_utils import serialize_datetime
from .docs_registration_id import DocsRegistrationId
from .file_path import FilePath
from .file_s_3_upload_url import FileS3UploadUrl


class StartDocsRegisterResponse(pydantic.BaseModel):
    docs_registration_id: DocsRegistrationId = pydantic.Field(alias="docsRegistrationId")
    upload_urls: typing.Dict[FilePath, FileS3UploadUrl] = pydantic.Field(alias="uploadUrls")

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