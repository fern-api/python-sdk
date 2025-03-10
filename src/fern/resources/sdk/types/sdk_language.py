# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SdkLanguage(str, enum.Enum):
    """
    The programming language to generate the SDK in
    """

    TYPESCRIPT = "typescript"
    PYTHON = "python"
    JAVA = "java"
    GO = "go"
    CSHARP = "csharp"
    RUBY = "ruby"
    PHP = "php"

    def visit(
        self,
        typescript: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        java: typing.Callable[[], T_Result],
        go: typing.Callable[[], T_Result],
        csharp: typing.Callable[[], T_Result],
        ruby: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SdkLanguage.TYPESCRIPT:
            return typescript()
        if self is SdkLanguage.PYTHON:
            return python()
        if self is SdkLanguage.JAVA:
            return java()
        if self is SdkLanguage.GO:
            return go()
        if self is SdkLanguage.CSHARP:
            return csharp()
        if self is SdkLanguage.RUBY:
            return ruby()
        if self is SdkLanguage.PHP:
            return php()
