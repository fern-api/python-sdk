# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..........core.datetime_utils import serialize_datetime
from .colors_config import ColorsConfig
from .colors_config_v_2 import ColorsConfigV2
from .colors_config_v_3 import ColorsConfigV3
from .docs_typography_config import DocsTypographyConfig
from .file_id import FileId
from .height import Height
from .logo_v_2 import LogoV2
from .navbar_link import NavbarLink
from .navigation_config import NavigationConfig
from .url import Url


class DocsConfig(pydantic.BaseModel):
    title: typing.Optional[str]
    navigation: NavigationConfig
    logo: typing.Optional[FileId]
    logo_v_2: typing.Optional[LogoV2] = pydantic.Field(alias="logoV2")
    logo_height: typing.Optional[Height] = pydantic.Field(alias="logoHeight")
    logo_href: typing.Optional[Url] = pydantic.Field(alias="logoHref")
    favicon: typing.Optional[FileId]
    background_image: typing.Optional[FileId] = pydantic.Field(alias="backgroundImage")
    colors: typing.Optional[ColorsConfig]
    colors_v_2: typing.Optional[ColorsConfigV2] = pydantic.Field(alias="colorsV2")
    colors_v_3: ColorsConfigV3 = pydantic.Field(alias="colorsV3")
    navbar_links: typing.List[NavbarLink] = pydantic.Field(alias="navbarLinks")
    typography: typing.Optional[DocsTypographyConfig]

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
