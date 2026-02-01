from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_traffic_reports_response_200 import GetCoverageRegionTrafficReportsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    language: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["depth"] = depth

    params["count"] = count

    params["start_page"] = start_page

    json_forbidden_id: list[str] | Unset = UNSET
    if not isinstance(forbidden_id, Unset):
        json_forbidden_id = forbidden_id

    params["forbidden_id[]"] = json_forbidden_id

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    params["distance"] = distance

    params["disable_geojson"] = disable_geojson

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags[]"] = json_tags

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/traffic_reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionTrafficReportsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionTrafficReportsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionTrafficReportsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    language: str | Unset = UNSET,
) -> Response[GetCoverageRegionTrafficReportsResponse200]:
    """Get traffic reports

    Args:
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):
        disable_geojson (bool | Unset):
        tags (list[str] | Unset):
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionTrafficReportsResponse200]
    """

    kwargs = _get_kwargs(
        depth=depth,
        count=count,
        start_page=start_page,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
        disable_geojson=disable_geojson,
        tags=tags,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    language: str | Unset = UNSET,
) -> GetCoverageRegionTrafficReportsResponse200 | None:
    """Get traffic reports

    Args:
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):
        disable_geojson (bool | Unset):
        tags (list[str] | Unset):
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionTrafficReportsResponse200
    """

    return sync_detailed(
        client=client,
        depth=depth,
        count=count,
        start_page=start_page,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
        disable_geojson=disable_geojson,
        tags=tags,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    language: str | Unset = UNSET,
) -> Response[GetCoverageRegionTrafficReportsResponse200]:
    """Get traffic reports

    Args:
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):
        disable_geojson (bool | Unset):
        tags (list[str] | Unset):
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionTrafficReportsResponse200]
    """

    kwargs = _get_kwargs(
        depth=depth,
        count=count,
        start_page=start_page,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
        disable_geojson=disable_geojson,
        tags=tags,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    language: str | Unset = UNSET,
) -> GetCoverageRegionTrafficReportsResponse200 | None:
    """Get traffic reports

    Args:
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):
        disable_geojson (bool | Unset):
        tags (list[str] | Unset):
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionTrafficReportsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            depth=depth,
            count=count,
            start_page=start_page,
            forbidden_id=forbidden_id,
            forbidden_uris=forbidden_uris,
            distance=distance,
            disable_geojson=disable_geojson,
            tags=tags,
            language=language,
        )
    ).parsed
