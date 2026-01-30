from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_calendars_id_response_200 import GetCoverageRegionCalendarsIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["depth"] = depth

    params["count"] = count

    params["start_page"] = start_page

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_forbidden_id: list[str] | Unset = UNSET
    if not isinstance(forbidden_id, Unset):
        json_forbidden_id = forbidden_id

    params["forbidden_id[]"] = json_forbidden_id

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    params["distance"] = distance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendars/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionCalendarsIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionCalendarsIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionCalendarsIdResponse200]:
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
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
) -> Response[GetCoverageRegionCalendarsIdResponse200]:
    """
    Args:
        id (str):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionCalendarsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        depth=depth,
        count=count,
        start_page=start_page,
        start_date=start_date,
        end_date=end_date,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
) -> GetCoverageRegionCalendarsIdResponse200 | None:
    """
    Args:
        id (str):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionCalendarsIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        depth=depth,
        count=count,
        start_page=start_page,
        start_date=start_date,
        end_date=end_date,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
) -> Response[GetCoverageRegionCalendarsIdResponse200]:
    """
    Args:
        id (str):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionCalendarsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        depth=depth,
        count=count,
        start_page=start_page,
        start_date=start_date,
        end_date=end_date,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        distance=distance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    distance: int | Unset = UNSET,
) -> GetCoverageRegionCalendarsIdResponse200 | None:
    """
    Args:
        id (str):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        distance (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionCalendarsIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            depth=depth,
            count=count,
            start_page=start_page,
            start_date=start_date,
            end_date=end_date,
            forbidden_id=forbidden_id,
            forbidden_uris=forbidden_uris,
            distance=distance,
        )
    ).parsed
