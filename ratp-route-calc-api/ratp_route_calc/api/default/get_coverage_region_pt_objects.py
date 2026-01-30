from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_pt_objects_response_200 import GetCoverageRegionPtObjectsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    type_: list[str] | Unset = UNSET,
    count: int | Unset = UNSET,
    admin_uri: list[str] | Unset = UNSET,
    depth: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type[]"] = json_type_

    params["count"] = count

    json_admin_uri: list[str] | Unset = UNSET
    if not isinstance(admin_uri, Unset):
        json_admin_uri = admin_uri

    params["admin_uri[]"] = json_admin_uri

    params["depth"] = depth

    params["disable_geojson"] = disable_geojson

    params["disable_disruption"] = disable_disruption

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pt_objects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionPtObjectsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionPtObjectsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionPtObjectsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    type_: list[str] | Unset = UNSET,
    count: int | Unset = UNSET,
    admin_uri: list[str] | Unset = UNSET,
    depth: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionPtObjectsResponse200]:
    """
    Args:
        q (str):
        type_ (list[str] | Unset):
        count (int | Unset):
        admin_uri (list[str] | Unset):
        depth (int | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionPtObjectsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        count=count,
        admin_uri=admin_uri,
        depth=depth,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    type_: list[str] | Unset = UNSET,
    count: int | Unset = UNSET,
    admin_uri: list[str] | Unset = UNSET,
    depth: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionPtObjectsResponse200 | None:
    """
    Args:
        q (str):
        type_ (list[str] | Unset):
        count (int | Unset):
        admin_uri (list[str] | Unset):
        depth (int | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionPtObjectsResponse200
    """

    return sync_detailed(
        client=client,
        q=q,
        type_=type_,
        count=count,
        admin_uri=admin_uri,
        depth=depth,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    type_: list[str] | Unset = UNSET,
    count: int | Unset = UNSET,
    admin_uri: list[str] | Unset = UNSET,
    depth: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> Response[GetCoverageRegionPtObjectsResponse200]:
    """
    Args:
        q (str):
        type_ (list[str] | Unset):
        count (int | Unset):
        admin_uri (list[str] | Unset):
        depth (int | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionPtObjectsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        count=count,
        admin_uri=admin_uri,
        depth=depth,
        disable_geojson=disable_geojson,
        disable_disruption=disable_disruption,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    type_: list[str] | Unset = UNSET,
    count: int | Unset = UNSET,
    admin_uri: list[str] | Unset = UNSET,
    depth: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
    disable_disruption: bool | Unset = UNSET,
) -> GetCoverageRegionPtObjectsResponse200 | None:
    """
    Args:
        q (str):
        type_ (list[str] | Unset):
        count (int | Unset):
        admin_uri (list[str] | Unset):
        depth (int | Unset):
        disable_geojson (bool | Unset):
        disable_disruption (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionPtObjectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            type_=type_,
            count=count,
            admin_uri=admin_uri,
            depth=depth,
            disable_geojson=disable_geojson,
            disable_disruption=disable_disruption,
        )
    ).parsed
