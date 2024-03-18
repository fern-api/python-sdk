# This file was auto-generated by Fern from our API Definition.

from fern.client import AsyncFern, Fern

from fern import EndpointIdentifier, EndpointMethod, Sdk_Python

from .utilities import validate_response


async def test_get(client: Fern, async_client: AsyncFern) -> None:
    expected_response = [
        {
            "type": "python",
            "sdk": {"package": "vellum-ai", "version": "1.2.1"},
            "sync_client": 'import Vellum from vellum.client\n\nclient = Vellum(api_key="YOUR_API_KEY")\nclient.search(query="Find documents written in the last 5 days")\n',
            "async_client": 'import VellumAsync from vellum.client\n\nclient = VellumAsync(api_key="YOUR_API_KEY")\nawait client.search(query="Find documents written in the last 5 days")\n',
        },
        {
            "type": "typescript",
            "sdk": {"package": "vellum-ai", "version": "1.2.1"},
            "client": 'import { VellumClient } from "vellum-ai";\n\nconst vellum = VellumClient({\n  apiKey="YOUR_API_KEY"\n})\nvellum.search({\n  query: "Find documents written in the last 5 days"\n})\n',
        },
    ]
    response = client.snippets.get(endpoint=EndpointIdentifier(method=EndpointMethod.GET, path="/v1/search"))
    validate_response(response, expected_response)

    async_response = await async_client.snippets.get(
        endpoint=EndpointIdentifier(method=EndpointMethod.GET, path="/v1/search")
    )
    validate_response(async_response, expected_response)


async def test_load(client: Fern, async_client: AsyncFern) -> None:
    expected_response = {
        "next": 2,
        "snippets": {
            "/v1/search": {
                "GET": [
                    {
                        "type": "python",
                        "sdk": {"package": "vellum-ai", "version": "1.2.1"},
                        "sync_client": 'import Vellum from vellum.client\n\nclient = Vellum(api_key="YOUR_API_KEY")\nclient.search(query="Find documents written in the last 5 days")\n',
                        "async_client": 'import Vellum from vellum.client\n\nclient = Vellum(api_key="YOUR_API_KEY")\nclient.search(query="Find documents written in the last 5 days")\n',
                    },
                    {
                        "type": "typescript",
                        "sdk": {"package": "vellum-ai", "version": "1.2.1"},
                        "client": 'import { VellumClient } from "vellum-ai";\n\nconst vellum = VellumClient({\n  apiKey="YOUR_API_KEY"\n})\nvellum.search({\n  query: "Find documents written in the last 5 days"\n})\n',
                    },
                ]
            },
            "v1/document-indexes": {
                "POST": [
                    {
                        "type": "python",
                        "sdk": {"package": "vellum-ai", "version": "1.2.1"},
                        "sync_client": 'import Vellum from vellum.client\n\nclient = Vellum(api_key="YOUR_API_KEY")\nclient.document_indexes.create(name="meeting-reports", status="ACTIVE")\n',
                        "async_client": 'import VellumAsync from vellum.client\n\nclient = VellumAsync(api_key="YOUR_API_KEY")\nawait client.document_indexes.create(name="meeting-reports", status="ACTIVE")\n',
                    },
                    {
                        "type": "typescript",
                        "sdk": {"package": "vellum-ai", "version": "1.2.1"},
                        "client": 'import { VellumClient } from "vellum-ai";\n\nconst vellum = VellumClient({\n  apiKey="YOUR_API_KEY"\n})\nvellum.documentIndexes.create({\n  name: "meeting-reports",\n  status: "ACTIVE"\n})\n',
                    },
                ]
            },
        },
    }
    response = client.snippets.load(
        page=1,
        org_id="vellum",
        api_id="vellum-ai",
        sdks=[Sdk_Python(type="python", package="vellum-ai", version="1.2.1")],
    )
    validate_response(response, expected_response)

    async_response = await async_client.snippets.load(
        page=1,
        org_id="vellum",
        api_id="vellum-ai",
        sdks=[Sdk_Python(type="python", package="vellum-ai", version="1.2.1")],
    )
    validate_response(async_response, expected_response)
