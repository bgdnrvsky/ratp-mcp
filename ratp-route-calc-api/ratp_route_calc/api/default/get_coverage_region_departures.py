from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_departures_response_200 import GetCoverageRegionDeparturesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    from_datetime: str | Unset = UNSET,
    until_datetime: str | Unset = UNSET,
    duration: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    max_date_times: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    calendar: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    items_per_schedule: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["from_datetime"] = from_datetime

    params["until_datetime"] = until_datetime

    params["duration"] = duration

    params["depth"] = depth

    params["count"] = count

    params["start_page"] = start_page

    params["max_date_times"] = max_date_times

    json_forbidden_id: list[str] | Unset = UNSET
    if not isinstance(forbidden_id, Unset):
        json_forbidden_id = forbidden_id

    params["forbidden_id[]"] = json_forbidden_id

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    params["calendar"] = calendar

    params["distance"] = distance

    params["show_codes"] = show_codes

    params["data_freshness"] = data_freshness

    params["items_per_schedule"] = items_per_schedule

    params["disable_geojson"] = disable_geojson

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/departures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionDeparturesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionDeparturesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionDeparturesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    from_datetime: str | Unset = UNSET,
    until_datetime: str | Unset = UNSET,
    duration: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    max_date_times: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    calendar: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    items_per_schedule: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
) -> Response[GetCoverageRegionDeparturesResponse200]:
    """Get departures for a given object

    Args:
        filter_ (str | Unset):
        from_datetime (str | Unset):
        until_datetime (str | Unset):
        duration (int | Unset):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        max_date_times (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        calendar (str | Unset):
        distance (int | Unset):
        show_codes (bool | Unset):
        data_freshness (str | Unset):
        items_per_schedule (int | Unset):
        disable_geojson (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionDeparturesResponse200]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        from_datetime=from_datetime,
        until_datetime=until_datetime,
        duration=duration,
        depth=depth,
        count=count,
        start_page=start_page,
        max_date_times=max_date_times,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        calendar=calendar,
        distance=distance,
        show_codes=show_codes,
        data_freshness=data_freshness,
        items_per_schedule=items_per_schedule,
        disable_geojson=disable_geojson,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    from_datetime: str | Unset = UNSET,
    until_datetime: str | Unset = UNSET,
    duration: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    max_date_times: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    calendar: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    items_per_schedule: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
) -> GetCoverageRegionDeparturesResponse200 | None:
    """Get departures for a given object

    Args:
        filter_ (str | Unset):
        from_datetime (str | Unset):
        until_datetime (str | Unset):
        duration (int | Unset):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        max_date_times (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        calendar (str | Unset):
        distance (int | Unset):
        show_codes (bool | Unset):
        data_freshness (str | Unset):
        items_per_schedule (int | Unset):
        disable_geojson (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionDeparturesResponse200
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        from_datetime=from_datetime,
        until_datetime=until_datetime,
        duration=duration,
        depth=depth,
        count=count,
        start_page=start_page,
        max_date_times=max_date_times,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        calendar=calendar,
        distance=distance,
        show_codes=show_codes,
        data_freshness=data_freshness,
        items_per_schedule=items_per_schedule,
        disable_geojson=disable_geojson,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    from_datetime: str | Unset = UNSET,
    until_datetime: str | Unset = UNSET,
    duration: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    max_date_times: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    calendar: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    items_per_schedule: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
) -> Response[GetCoverageRegionDeparturesResponse200]:
    """Get departures for a given object

    Args:
        filter_ (str | Unset):
        from_datetime (str | Unset):
        until_datetime (str | Unset):
        duration (int | Unset):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        max_date_times (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        calendar (str | Unset):
        distance (int | Unset):
        show_codes (bool | Unset):
        data_freshness (str | Unset):
        items_per_schedule (int | Unset):
        disable_geojson (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionDeparturesResponse200]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        from_datetime=from_datetime,
        until_datetime=until_datetime,
        duration=duration,
        depth=depth,
        count=count,
        start_page=start_page,
        max_date_times=max_date_times,
        forbidden_id=forbidden_id,
        forbidden_uris=forbidden_uris,
        calendar=calendar,
        distance=distance,
        show_codes=show_codes,
        data_freshness=data_freshness,
        items_per_schedule=items_per_schedule,
        disable_geojson=disable_geojson,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    from_datetime: str | Unset = UNSET,
    until_datetime: str | Unset = UNSET,
    duration: int | Unset = UNSET,
    depth: int | Unset = UNSET,
    count: int | Unset = UNSET,
    start_page: int | Unset = UNSET,
    max_date_times: int | Unset = UNSET,
    forbidden_id: list[str] | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    calendar: str | Unset = UNSET,
    distance: int | Unset = UNSET,
    show_codes: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    items_per_schedule: int | Unset = UNSET,
    disable_geojson: bool | Unset = UNSET,
) -> GetCoverageRegionDeparturesResponse200 | None:
    """Get departures for a given object

    Args:
        filter_ (str | Unset):
        from_datetime (str | Unset):
        until_datetime (str | Unset):
        duration (int | Unset):
        depth (int | Unset):
        count (int | Unset):
        start_page (int | Unset):
        max_date_times (int | Unset):
        forbidden_id (list[str] | Unset):
        forbidden_uris (list[str] | Unset):
        calendar (str | Unset):
        distance (int | Unset):
        show_codes (bool | Unset):
        data_freshness (str | Unset):
        items_per_schedule (int | Unset):
        disable_geojson (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionDeparturesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            from_datetime=from_datetime,
            until_datetime=until_datetime,
            duration=duration,
            depth=depth,
            count=count,
            start_page=start_page,
            max_date_times=max_date_times,
            forbidden_id=forbidden_id,
            forbidden_uris=forbidden_uris,
            calendar=calendar,
            distance=distance,
            show_codes=show_codes,
            data_freshness=data_freshness,
            items_per_schedule=items_per_schedule,
            disable_geojson=disable_geojson,
        )
    ).parsed
