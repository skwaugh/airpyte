from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.source_definition_create import SourceDefinitionCreate
from ...models.source_definition_read import SourceDefinitionRead
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SourceDefinitionCreate,
) -> Dict[str, Any]:
    url = "{}/v1/source_definitions/create".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[None, SourceDefinitionRead]]:
    if response.status_code == 200:
        response_200 = SourceDefinitionRead.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = None

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[None, SourceDefinitionRead]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SourceDefinitionCreate,
) -> Response[Union[None, SourceDefinitionRead]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SourceDefinitionCreate,
) -> Optional[Union[None, SourceDefinitionRead]]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SourceDefinitionCreate,
) -> Response[Union[None, SourceDefinitionRead]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SourceDefinitionCreate,
) -> Optional[Union[None, SourceDefinitionRead]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
