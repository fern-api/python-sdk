# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .legacy_multi_algolia_index_info import LegacyMultiAlgoliaIndexInfo
from .single_algolia_index_info import SingleAlgoliaIndexInfo


class SearchInfo_LegacyMultiAlgoliaIndex(LegacyMultiAlgoliaIndexInfo):
    type: typing_extensions.Literal["legacyMultiAlgoliaIndex"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class SearchInfo_SingleAlgoliaIndex(pydantic.BaseModel):
    type: typing_extensions.Literal["singleAlgoliaIndex"]
    value: SingleAlgoliaIndexInfo

    class Config:
        frozen = True
        smart_union = True


SearchInfo = typing.Union[SearchInfo_LegacyMultiAlgoliaIndex, SearchInfo_SingleAlgoliaIndex]
