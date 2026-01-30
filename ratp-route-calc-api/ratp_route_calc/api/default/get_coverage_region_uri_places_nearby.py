from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_uri_places_nearby_response_200 import GetCoverageRegionUriPlacesNearbyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uri: str,
    *,
    type_: list[str] | Unset = UNSET,
    filter_: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type[]"] = json_type_

    params["filter"] = filter_

    params["distance"] = distance

    params["count"] = count

    params["depth"] = depth

    params["start_page"] = start_page

    params["bss_stands"] = bss_stands

    json_add_poi_infos: list[str] | Unset = UNSET
    if not isinstance(add_poi_infos, Unset):
        json_add_poi_infos = add_poi_infos

    params["add_poi_infos[]"] = json_add_poi_infos

    params["disable_geojson"] = disable_geojson

    params["disable_disruption"] = disable_disruption

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{uri}/places_nearby".format(
            uri=quote(str(uri), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionUriPlacesNearbyResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionUriPlacesNearbyResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionUriPlacesNearbyResponse200]:
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
    type_: list[str] | Unset = UNSET,
    filter_: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionUriPlacesNearbyResponse200]:
    """
    Args:
        uri (str):
        type_ (list[str] | Unset):
        filter_ (str | Unset):
        distance (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        start_page (int | Unset):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriPlacesNearbyResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        type_=type_,
        filter_=filter_,
        distance=distance,
        count=count,
        depth=depth,
        start_page=start_page,
        bss_stands=bss_stands,
        add_poi_infos=add_poi_infos,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    type_: list[str] | Unset = UNSET,
    filter_: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionUriPlacesNearbyResponse200 | None:
    """
    Args:
        uri (str):
        type_ (list[str] | Unset):
        filter_ (str | Unset):
        distance (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        start_page (int | Unset):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriPlacesNearbyResponse200
    """

    return sync_detailed(
        uri=uri,
        client=client,
        type_=type_,
        filter_=filter_,
        distance=distance,
        count=count,
        depth=depth,
        start_page=start_page,
        bss_stands=bss_stands,
        add_poi_infos=add_poi_infos,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    ).parsed


async def asyncio_detailed(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    type_: list[str] | Unset = UNSET,
    filter_: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionUriPlacesNearbyResponse200]:
    """
    Args:
        uri (str):
        type_ (list[str] | Unset):
        filter_ (str | Unset):
        distance (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        start_page (int | Unset):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionUriPlacesNearbyResponse200]
    """

    kwargs = _get_kwargs(
        uri=uri,
        type_=type_,
        filter_=filter_,
        distance=distance,
        count=count,
        depth=depth,
        start_page=start_page,
        bss_stands=bss_stands,
        add_poi_infos=add_poi_infos,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
    type_: list[str] | Unset = UNSET,
    filter_: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    count: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionUriPlacesNearbyResponse200 | None:
    """
    Args:
        uri (str):
        type_ (list[str] | Unset):
        filter_ (str | Unset):
        distance (int | Unset):
        count (int | Unset):
        depth (int | Unset):
        start_page (int | Unset):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionUriPlacesNearbyResponse200
    """

    return (
        await asyncio_detailed(
            uri=uri,
            client=client,
            type_=type_,
            filter_=filter_,
            distance=distance,
            count=count,
            depth=depth,
            start_page=start_page,
            bss_stands=bss_stands,
            add_poi_infos=add_poi_infos,
            disable_geojson=disable_geojson,
            disable_disruption=disable_disruption,
        )
    ).parsed
