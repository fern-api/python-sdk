# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.errors.unavailable_error import UnavailableError
from ..commons.errors.user_not_in_org_error import UserNotInOrgError
from ..commons.types.api_id import ApiId
from ..commons.types.endpoint_identifier import EndpointIdentifier
from ..commons.types.org_id import OrgId
from .errors.api_id_required_error import ApiIdRequiredError
from .errors.endpoint_not_found import EndpointNotFound
from .errors.invalid_page_error import InvalidPageError
from .errors.org_id_and_api_id_not_found import OrgIdAndApiIdNotFound
from .errors.org_id_not_found import OrgIdNotFound
from .errors.org_id_required_error import OrgIdRequiredError
from .errors.sdk_not_found import SdkNotFound
from .types.custom_snippet_payload import CustomSnippetPayload
from .types.sdk_request import SdkRequest
from .types.snippet import Snippet
from .types.snippets_page import SnippetsPage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SnippetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        org_id: typing.Optional[OrgId] = OMIT,
        api_id: typing.Optional[ApiId] = OMIT,
        sdks: typing.Optional[typing.Sequence[SdkRequest]] = OMIT,
        endpoint: EndpointIdentifier,
        example_identifier: typing.Optional[str] = OMIT,
        payload: typing.Optional[CustomSnippetPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Snippet]:
        """
        Get snippet by endpoint method and path

        Parameters:
            - org_id: typing.Optional[OrgId]. If the same API is defined across multiple organization,
                                              you must specify an organization ID.
            - api_id: typing.Optional[ApiId]. If you have more than one API, you must specify its ID.

            - sdks: typing.Optional[typing.Sequence[SdkRequest]]. The SDKs for which to load snippets. If unspecified,
                                                                  snippets for the latest published SDKs will be returned.
            - endpoint: EndpointIdentifier.

            - example_identifier: typing.Optional[str]. The identifier of the example to fetch the snippet for, this is ignored if a payload is passed in.

            - payload: typing.Optional[CustomSnippetPayload]. The JSON payload to be used as the input for the code snippet. This should just be thought of as the
                                                              request body you'd be sending to the endpoint as a cURL. If not specified then the default payload will be used.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import Fern

        from fern import EndpointIdentifier, EndpointMethod

        client = Fern(
            token="YOUR_TOKEN",
        )
        client.snippets.get(
            endpoint=EndpointIdentifier(
                method=EndpointMethod.GET,
                path="/v1/search",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"endpoint": endpoint}
        if org_id is not OMIT:
            _request["orgId"] = org_id
        if api_id is not OMIT:
            _request["apiId"] = api_id
        if sdks is not OMIT:
            _request["sdks"] = sdks
        if example_identifier is not OMIT:
            _request["exampleIdentifier"] = example_identifier
        if payload is not OMIT:
            _request["payload"] = payload
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "snippets"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(typing.List[Snippet], _response_json)  # type: ignore
        if "error" in _response_json:
            if _response_json["error"] == "UnauthorizedError":
                raise UnauthorizedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UserNotInOrgError":
                raise UserNotInOrgError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UnavailableError":
                raise UnavailableError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "ApiIdRequiredError":
                raise ApiIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdRequiredError":
                raise OrgIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdAndApiIdNotFound":
                raise OrgIdAndApiIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdNotFound":
                raise OrgIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "EndpointNotFound":
                raise EndpointNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "SDKNotFound":
                raise SdkNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def load(
        self,
        *,
        page: typing.Optional[int] = None,
        org_id: typing.Optional[OrgId] = OMIT,
        api_id: typing.Optional[ApiId] = OMIT,
        sdks: typing.Optional[typing.Sequence[SdkRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnippetsPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - org_id: typing.Optional[OrgId]. If the same API is defined across multiple organization,
                                              you must specify an organization ID.
            - api_id: typing.Optional[ApiId]. If you have more than one API, you must specify its ID.

            - sdks: typing.Optional[typing.Sequence[SdkRequest]]. The SDKs for which to load snippets. If unspecified,
                                                                  snippets for the latest published SDKs will be returned.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import Fern

        from fern import SdkRequest_Python

        client = Fern(
            token="YOUR_TOKEN",
        )
        client.snippets.load(
            page=1,
            org_id="vellum",
            api_id="vellum-ai",
            sdks=[
                SdkRequest_Python(
                    type="python",
                    package="vellum-ai",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if org_id is not OMIT:
            _request["orgId"] = org_id
        if api_id is not OMIT:
            _request["apiId"] = api_id
        if sdks is not OMIT:
            _request["sdks"] = sdks
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "snippets/load"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page": page,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(SnippetsPage, _response_json)  # type: ignore
        if "error" in _response_json:
            if _response_json["error"] == "UnauthorizedError":
                raise UnauthorizedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UserNotInOrgError":
                raise UserNotInOrgError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UnavailableError":
                raise UnavailableError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "InvalidPageError":
                raise InvalidPageError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "ApiIdRequiredError":
                raise ApiIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdRequiredError":
                raise OrgIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdAndApiIdNotFound":
                raise OrgIdAndApiIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdNotFound":
                raise OrgIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "SDKNotFound":
                raise SdkNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSnippetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        org_id: typing.Optional[OrgId] = OMIT,
        api_id: typing.Optional[ApiId] = OMIT,
        sdks: typing.Optional[typing.Sequence[SdkRequest]] = OMIT,
        endpoint: EndpointIdentifier,
        example_identifier: typing.Optional[str] = OMIT,
        payload: typing.Optional[CustomSnippetPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Snippet]:
        """
        Get snippet by endpoint method and path

        Parameters:
            - org_id: typing.Optional[OrgId]. If the same API is defined across multiple organization,
                                              you must specify an organization ID.
            - api_id: typing.Optional[ApiId]. If you have more than one API, you must specify its ID.

            - sdks: typing.Optional[typing.Sequence[SdkRequest]]. The SDKs for which to load snippets. If unspecified,
                                                                  snippets for the latest published SDKs will be returned.
            - endpoint: EndpointIdentifier.

            - example_identifier: typing.Optional[str]. The identifier of the example to fetch the snippet for, this is ignored if a payload is passed in.

            - payload: typing.Optional[CustomSnippetPayload]. The JSON payload to be used as the input for the code snippet. This should just be thought of as the
                                                              request body you'd be sending to the endpoint as a cURL. If not specified then the default payload will be used.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import AsyncFern

        from fern import EndpointIdentifier, EndpointMethod

        client = AsyncFern(
            token="YOUR_TOKEN",
        )
        await client.snippets.get(
            endpoint=EndpointIdentifier(
                method=EndpointMethod.GET,
                path="/v1/search",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"endpoint": endpoint}
        if org_id is not OMIT:
            _request["orgId"] = org_id
        if api_id is not OMIT:
            _request["apiId"] = api_id
        if sdks is not OMIT:
            _request["sdks"] = sdks
        if example_identifier is not OMIT:
            _request["exampleIdentifier"] = example_identifier
        if payload is not OMIT:
            _request["payload"] = payload
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "snippets"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(typing.List[Snippet], _response_json)  # type: ignore
        if "error" in _response_json:
            if _response_json["error"] == "UnauthorizedError":
                raise UnauthorizedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UserNotInOrgError":
                raise UserNotInOrgError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UnavailableError":
                raise UnavailableError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "ApiIdRequiredError":
                raise ApiIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdRequiredError":
                raise OrgIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdAndApiIdNotFound":
                raise OrgIdAndApiIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdNotFound":
                raise OrgIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "EndpointNotFound":
                raise EndpointNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "SDKNotFound":
                raise SdkNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def load(
        self,
        *,
        page: typing.Optional[int] = None,
        org_id: typing.Optional[OrgId] = OMIT,
        api_id: typing.Optional[ApiId] = OMIT,
        sdks: typing.Optional[typing.Sequence[SdkRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnippetsPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - org_id: typing.Optional[OrgId]. If the same API is defined across multiple organization,
                                              you must specify an organization ID.
            - api_id: typing.Optional[ApiId]. If you have more than one API, you must specify its ID.

            - sdks: typing.Optional[typing.Sequence[SdkRequest]]. The SDKs for which to load snippets. If unspecified,
                                                                  snippets for the latest published SDKs will be returned.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from fern.client import AsyncFern

        from fern import SdkRequest_Python

        client = AsyncFern(
            token="YOUR_TOKEN",
        )
        await client.snippets.load(
            page=1,
            org_id="vellum",
            api_id="vellum-ai",
            sdks=[
                SdkRequest_Python(
                    type="python",
                    package="vellum-ai",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if org_id is not OMIT:
            _request["orgId"] = org_id
        if api_id is not OMIT:
            _request["apiId"] = api_id
        if sdks is not OMIT:
            _request["sdks"] = sdks
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "snippets/load"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page": page,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(SnippetsPage, _response_json)  # type: ignore
        if "error" in _response_json:
            if _response_json["error"] == "UnauthorizedError":
                raise UnauthorizedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UserNotInOrgError":
                raise UserNotInOrgError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "UnavailableError":
                raise UnavailableError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "InvalidPageError":
                raise InvalidPageError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "ApiIdRequiredError":
                raise ApiIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdRequiredError":
                raise OrgIdRequiredError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdAndApiIdNotFound":
                raise OrgIdAndApiIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "OrgIdNotFound":
                raise OrgIdNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["error"] == "SDKNotFound":
                raise SdkNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
