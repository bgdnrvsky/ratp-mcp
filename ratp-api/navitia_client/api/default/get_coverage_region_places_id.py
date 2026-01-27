from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_places_id_response_200 import GetCoverageRegionPlacesIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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
        "url": "/places/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionPlacesIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionPlacesIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionPlacesIdResponse200]:
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
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionPlacesIdResponse200]:
    """
    Args:
        id (str):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionPlacesIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionPlacesIdResponse200 | None:
    """
    Args:
        id (str):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionPlacesIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        bss_stands=bss_stands,
        add_poi_infos=add_poi_infos,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionPlacesIdResponse200]:
    """
    Args:
        id (str):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionPlacesIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        bss_stands=bss_stands,
        add_poi_infos=add_poi_infos,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    bss_stands: bool | Unset = UNSET,
    add_poi_infos: list[str] | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionPlacesIdResponse200 | None:
    """
    Args:
        id (str):
        bss_stands (bool | Unset):
        add_poi_infos (list[str] | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionPlacesIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            bss_stands=bss_stands,
            add_poi_infos=add_poi_infos,
            disable_geojson=disable_geojson,
            disable_disruption=disable_disruption,
        )
    ).parsed
