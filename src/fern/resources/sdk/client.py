# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from .types.api_definition import ApiDefinition
from .types.generate_sdk_response import GenerateSdkResponse
from .types.sdk_generation_status import SdkGenerationStatus
from .types.sdk_language import SdkLanguage
from .types.sdk_publishing_configuration import SdkPublishingConfiguration

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SdkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate(
        self,
        *,
        api: ApiDefinition,
        language: SdkLanguage,
        publishing: SdkPublishingConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateSdkResponse:
        """
        Generate an SDK for your API definition in one of our supported languages.

        Parameters:
            - api: ApiDefinition. The API definition to use as input for SDK generation.

            - language: SdkLanguage. The target programming language for the generated SDK.

            - publishing: SdkPublishingConfiguration. Configuration options for publishing the generated SDK.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import Fern

        from fern import ApiDefinition_Openapi, SdkLanguage, SdkPublishingConfiguration

        client = Fern(
            token="YOUR_TOKEN",
        )
        client.sdk.generate(
            api=ApiDefinition_Openapi(type="openapi", value={"key": "value"}),
            language=SdkLanguage.TYPESCRIPT,
            publishing=SdkPublishingConfiguration(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sdk/generate"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"api": api, "language": language, "publishing": publishing})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"api": api, "language": language, "publishing": publishing}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GenerateSdkResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SdkGenerationStatus:
        """
        Get the status of an SDK generation job.

        Parameters:
            - job_id: str. The ID of the SDK generation job to check the status of

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import Fern

        client = Fern(
            token="YOUR_TOKEN",
        )
        client.sdk.get_status(
            job_id="jobId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sdk/status/{jsonable_encoder(job_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SdkGenerationStatus, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSdkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate(
        self,
        *,
        api: ApiDefinition,
        language: SdkLanguage,
        publishing: SdkPublishingConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateSdkResponse:
        """
        Generate an SDK for your API definition in one of our supported languages.

        Parameters:
            - api: ApiDefinition. The API definition to use as input for SDK generation.

            - language: SdkLanguage. The target programming language for the generated SDK.

            - publishing: SdkPublishingConfiguration. Configuration options for publishing the generated SDK.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import AsyncFern

        from fern import ApiDefinition_Openapi, SdkLanguage, SdkPublishingConfiguration

        client = AsyncFern(
            token="YOUR_TOKEN",
        )
        await client.sdk.generate(
            api=ApiDefinition_Openapi(type="openapi", value={"key": "value"}),
            language=SdkLanguage.TYPESCRIPT,
            publishing=SdkPublishingConfiguration(),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sdk/generate"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"api": api, "language": language, "publishing": publishing})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"api": api, "language": language, "publishing": publishing}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GenerateSdkResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SdkGenerationStatus:
        """
        Get the status of an SDK generation job.

        Parameters:
            - job_id: str. The ID of the SDK generation job to check the status of

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import AsyncFern

        client = AsyncFern(
            token="YOUR_TOKEN",
        )
        await client.sdk.get_status(
            job_id="jobId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sdk/status/{jsonable_encoder(job_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SdkGenerationStatus, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
