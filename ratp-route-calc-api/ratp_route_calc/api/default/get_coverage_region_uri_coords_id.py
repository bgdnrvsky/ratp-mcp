from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_uri_coords_id_response_200 import GetCoverageRegionUriCoordsIdResponse200
from ...types import Response


def _get_kwargs(
    uri: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{uri}/coords/{id}".format(
            uri=quote(str(uri), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionUriCoordsIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionUriCoordsIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionUriCoordsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uri: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCoverageRegionUriCoordsIdResponse200]:
    """
    Args:
        uri (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriCoordsIdResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uri: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCoverageRegionUriCoordsIdResponse200 | None:
    """
    Args:
        uri (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriCoordsIdResponse200
    """

    return sync_detailed(
        uri=uri,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uri: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCoverageRegionUriCoordsIdResponse200]:
    """
    Args:
        uri (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriCoordsIdResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uri: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCoverageRegionUriCoordsIdResponse200 | None:
    """
    Args:
        uri (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriCoordsIdResponse200
    """

    return (
        await asyncio_detailed(
            uri=uri,
            id=id,
            client=client,
        )
    ).parsed
