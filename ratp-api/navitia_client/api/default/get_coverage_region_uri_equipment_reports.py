from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_uri_equipment_reports_response_200 import (
    GetCoverageRegionUriEquipmentReportsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uri: str,
    *,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["depth"] = depth

    params["count"] = count

    params["filter"] = filter_

    params["start_page"] = start_page

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{uri}/equipment_reports".format(
            uri=quote(str(uri), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionUriEquipmentReportsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionUriEquipmentReportsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionUriEquipmentReportsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
) -> Response[GetCoverageRegionUriEquipmentReportsResponse200]:
    """
    Args:
        uri (str):
        depth (int | Unset):
        count (int | Unset):
        filter_ (str | Unset):
        start_page (int | Unset):
        forbidden_uris (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriEquipmentReportsResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        depth=depth,
        count=count,
        filter_=filter_,
        start_page=start_page,
        forbidden_uris=forbidden_uris,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
) -> GetCoverageRegionUriEquipmentReportsResponse200 | None:
    """
    Args:
        uri (str):
        depth (int | Unset):
        count (int | Unset):
        filter_ (str | Unset):
        start_page (int | Unset):
        forbidden_uris (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriEquipmentReportsResponse200
    """

    return sync_detailed(
        uri=uri,
        client=client,
        depth=depth,
        count=count,
        filter_=filter_,
        start_page=start_page,
        forbidden_uris=forbidden_uris,
    ).parsed


async def asyncio_detailed(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
) -> Response[GetCoverageRegionUriEquipmentReportsResponse200]:
    """
    Args:
        uri (str):
        depth (int | Unset):
        count (int | Unset):
        filter_ (str | Unset):
        start_page (int | Unset):
        forbidden_uris (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriEquipmentReportsResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        depth=depth,
        count=count,
        filter_=filter_,
        start_page=start_page,
        forbidden_uris=forbidden_uris,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
) -> GetCoverageRegionUriEquipmentReportsResponse200 | None:
    """
    Args:
        uri (str):
        depth (int | Unset):
        count (int | Unset):
        filter_ (str | Unset):
        start_page (int | Unset):
        forbidden_uris (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriEquipmentReportsResponse200
    """

    return (
        await asyncio_detailed(
            uri=uri,
            client=client,
            depth=depth,
            count=count,
            filter_=filter_,
            start_page=start_page,
            forbidden_uris=forbidden_uris,
        )
    ).parsed
