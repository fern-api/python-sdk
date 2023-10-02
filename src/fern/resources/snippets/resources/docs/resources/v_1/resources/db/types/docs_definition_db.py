# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .docs_definition_db_v_1 import DocsDefinitionDbV1
from .docs_definition_db_v_2 import DocsDefinitionDbV2


class DocsDefinitionDb_V1(DocsDefinitionDbV1):
    type: typing_extensions.Literal["v1"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DocsDefinitionDb_V2(DocsDefinitionDbV2):
    type: typing_extensions.Literal["v2"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


DocsDefinitionDb = typing.Union[DocsDefinitionDb_V1, DocsDefinitionDb_V2]
