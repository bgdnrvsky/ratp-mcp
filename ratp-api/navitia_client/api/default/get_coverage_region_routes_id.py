from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_routes_id_response_200 import GetCoverageRegionRoutesIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    start_page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    external_code: str | Unset = UNSET,
    headsign: str | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    odt_level: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    original_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_page"] = start_page

    params["count"] = count

    params["depth"] = depth

    json_forbidden_id: list[str] | Unset = UNSET
    if not isinstance(forbidden_id, Unset):
        json_forbidden_id = forbidden_id

    params["forbidden_id[]"] = json_forbidden_id

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    params["external_code"] = external_code

    params["headsign"] = headsign

    params["show_codes"] = show_codes

    params["odt_level"] = odt_level

    params["distance"] = distance

    params["since"] = since

    params["until"] = until

    params["disable_geojson"] = disable_geojson

    params["disable_disruption"] = disable_disruption

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags[]"] = json_tags

    params["original_id"] = original_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/routes/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionRoutesIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionRoutesIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionRoutesIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    external_code: str | Unset = UNSET,
    headsign: str | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    odt_level: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    original_id: str | Unset = UNSET,
) -> Response[GetCoverageRegionRoutesIdResponse200]:
    """
    Args:
        id (str):
        start_page (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        external_code (str | Unset):
        headsign (str | Unset):
        show_codes (bool | Unset):
        odt_level (str | Unset):
        distance (int | Unset):
        since (str | Unset):
        until (str | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):
        tags (list[str] | Unset):
        original_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionRoutesIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        start_page=start_page,
        count=count,
        depth=depth,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        external_code=external_code,
        headsign=headsign,
        show_codes=show_codes,
        odt_level=odt_level,
        distance=distance,
        since=since,
        until=until,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
        tags=tags,
        original_id=original_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    external_code: str | Unset = UNSET,
    headsign: str | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    odt_level: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    original_id: str | Unset = UNSET,
) -> GetCoverageRegionRoutesIdResponse200 | None:
    """
    Args:
        id (str):
        start_page (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        external_code (str | Unset):
        headsign (str | Unset):
        show_codes (bool | Unset):
        odt_level (str | Unset):
        distance (int | Unset):
        since (str | Unset):
        until (str | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):
        tags (list[str] | Unset):
        original_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionRoutesIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        start_page=start_page,
        count=count,
        depth=depth,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        external_code=external_code,
        headsign=headsign,
        show_codes=show_codes,
        odt_level=odt_level,
        distance=distance,
        since=since,
        until=until,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
        tags=tags,
        original_id=original_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    external_code: str | Unset = UNSET,
    headsign: str | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    odt_level: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    original_id: str | Unset = UNSET,
) -> Response[GetCoverageRegionRoutesIdResponse200]:
    """
    Args:
        id (str):
        start_page (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        external_code (str | Unset):
        headsign (str | Unset):
        show_codes (bool | Unset):
        odt_level (str | Unset):
        distance (int | Unset):
        since (str | Unset):
        until (str | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):
        tags (list[str] | Unset):
        original_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionRoutesIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        start_page=start_page,
        count=count,
        depth=depth,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        external_code=external_code,
        headsign=headsign,
        show_codes=show_codes,
        odt_level=odt_level,
        distance=distance,
        since=since,
        until=until,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
        tags=tags,
        original_id=original_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    external_code: str | Unset = UNSET,
    headsign: str | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    odt_level: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    original_id: str | Unset = UNSET,
) -> GetCoverageRegionRoutesIdResponse200 | None:
    """
    Args:
        id (str):
        start_page (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        external_code (str | Unset):
        headsign (str | Unset):
        show_codes (bool | Unset):
        odt_level (str | Unset):
        distance (int | Unset):
        since (str | Unset):
        until (str | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):
        tags (list[str] | Unset):
        original_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionRoutesIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start_page=start_page,
            count=count,
            depth=depth,
            forbidden_id=forbidden_id,
            forbidden_uris=forbidden_uris,
            external_code=external_code,
            headsign=headsign,
            show_codes=show_codes,
            odt_level=odt_level,
            distance=distance,
            since=since,
            until=until,
            disable_geojson=disable_geojson,
            disable_disruption=disable_disruption,
            tags=tags,
            original_id=original_id,
        )
    ).parsed
