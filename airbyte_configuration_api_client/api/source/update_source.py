from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.source_read import SourceRead
from ...models.source_update import SourceUpdate
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SourceUpdate,
) -> Dict[str, Any]:
    url = "{}/v1/sources/update".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[None, SourceRead]]:
    if response.status_code == 200:
        response_200 = SourceRead.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    if response.status_code == 422:
        response_422 = None

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[None, SourceRead]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SourceUpdate,
) -> Response[Union[None, SourceRead]]:
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
    json_body: SourceUpdate,
) -> Optional[Union[None, SourceRead]]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SourceUpdate,
) -> Response[Union[None, SourceRead]]:
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
    json_body: SourceUpdate,
) -> Optional[Union[None, SourceRead]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
