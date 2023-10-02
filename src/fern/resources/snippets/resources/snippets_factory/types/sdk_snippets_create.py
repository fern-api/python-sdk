# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .go_sdk_snippets_create import GoSdkSnippetsCreate
from .java_sdk_snippets_create import JavaSdkSnippetsCreate
from .python_sdk_snippet_create import PythonSdkSnippetCreate
from .typescript_sdk_snippets_create import TypescriptSdkSnippetsCreate


class SdkSnippetsCreate_Typescript(TypescriptSdkSnippetsCreate):
    type: typing_extensions.Literal["typescript"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class SdkSnippetsCreate_Python(PythonSdkSnippetCreate):
    type: typing_extensions.Literal["python"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class SdkSnippetsCreate_Go(GoSdkSnippetsCreate):
    type: typing_extensions.Literal["go"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class SdkSnippetsCreate_Java(JavaSdkSnippetsCreate):
    type: typing_extensions.Literal["java"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


SdkSnippetsCreate = typing.Union[
    SdkSnippetsCreate_Typescript, SdkSnippetsCreate_Python, SdkSnippetsCreate_Go, SdkSnippetsCreate_Java
]
