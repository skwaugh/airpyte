from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.connection_id_request_body import ConnectionIdRequestBody
from ...models.job_info_read import JobInfoRead
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ConnectionIdRequestBody,
) -> Dict[str, Any]:
    url = "{}/v1/connections/reset".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[JobInfoRead, None]]:
    if response.status_code == 200:
        response_200 = JobInfoRead.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    if response.status_code == 422:
        response_422 = None

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[JobInfoRead, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ConnectionIdRequestBody,
) -> Response[Union[JobInfoRead, None]]:
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
    json_body: ConnectionIdRequestBody,
) -> Optional[Union[JobInfoRead, None]]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ConnectionIdRequestBody,
) -> Response[Union[JobInfoRead, None]]:
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
    json_body: ConnectionIdRequestBody,
) -> Optional[Union[JobInfoRead, None]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
