from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_coverage_region_heat_maps_response_200 import GetCoverageRegionHeatMapsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    datetime_: str | Unset = UNSET,
    datetime_represents: str | Unset = UNSET,
    max_nb_transfers: int | Unset = UNSET,
    min_nb_transfers: int | Unset = UNSET,
    first_section_mode: list[str] | Unset = UNSET,
    last_section_mode: list[str] | Unset = UNSET,
    max_duration_to_pt: int | Unset = UNSET,
    max_walking_duration_to_pt: int | Unset = UNSET,
    max_bike_duration_to_pt: int | Unset = UNSET,
    max_bss_duration_to_pt: int | Unset = UNSET,
    max_car_duration_to_pt: int | Unset = UNSET,
    max_ridesharing_duration_to_pt: int | Unset = UNSET,
    walking_speed: float | Unset = UNSET,
    bike_speed: float | Unset = UNSET,
    bss_speed: float | Unset = UNSET,
    car_speed: float | Unset = UNSET,
    ridesharing_speed: float | Unset = UNSET,
    taxi_speed: float | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    allowed_id: list[str] | Unset = UNSET,
    disruption_active: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    max_duration: int | Unset = UNSET,
    wheelchair: bool | Unset = UNSET,
    traveler_type: str | Unset = UNSET,
    direct_path: str | Unset = UNSET,
    free_radius_from: int | Unset = UNSET,
    free_radius_to: int | Unset = UNSET,
    resolution: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["datetime"] = datetime_

    params["datetime_represents"] = datetime_represents

    params["max_nb_transfers"] = max_nb_transfers

    params["min_nb_transfers"] = min_nb_transfers

    json_first_section_mode: list[str] | Unset = UNSET
    if not isinstance(first_section_mode, Unset):
        json_first_section_mode = first_section_mode

    params["first_section_mode[]"] = json_first_section_mode

    json_last_section_mode: list[str] | Unset = UNSET
    if not isinstance(last_section_mode, Unset):
        json_last_section_mode = last_section_mode

    params["last_section_mode[]"] = json_last_section_mode

    params["max_duration_to_pt"] = max_duration_to_pt

    params["max_walking_duration_to_pt"] = max_walking_duration_to_pt

    params["max_bike_duration_to_pt"] = max_bike_duration_to_pt

    params["max_bss_duration_to_pt"] = max_bss_duration_to_pt

    params["max_car_duration_to_pt"] = max_car_duration_to_pt

    params["max_ridesharing_duration_to_pt"] = max_ridesharing_duration_to_pt

    params["walking_speed"] = walking_speed

    params["bike_speed"] = bike_speed

    params["bss_speed"] = bss_speed

    params["car_speed"] = car_speed

    params["ridesharing_speed"] = ridesharing_speed

    params["taxi_speed"] = taxi_speed

    json_forbidden_uris: list[str] | Unset = UNSET
    if not isinstance(forbidden_uris, Unset):
        json_forbidden_uris = forbidden_uris

    params["forbidden_uris[]"] = json_forbidden_uris

    json_allowed_id: list[str] | Unset = UNSET
    if not isinstance(allowed_id, Unset):
        json_allowed_id = allowed_id

    params["allowed_id[]"] = json_allowed_id

    params["disruption_active"] = disruption_active

    params["data_freshness"] = data_freshness

    params["max_duration"] = max_duration

    params["wheelchair"] = wheelchair

    params["traveler_type"] = traveler_type

    params["direct_path"] = direct_path

    params["free_radius_from"] = free_radius_from

    params["free_radius_to"] = free_radius_to

    params["resolution"] = resolution

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/heat_maps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCoverageRegionHeatMapsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoverageRegionHeatMapsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCoverageRegionHeatMapsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    datetime_: str | Unset = UNSET,
    datetime_represents: str | Unset = UNSET,
    max_nb_transfers: int | Unset = UNSET,
    min_nb_transfers: int | Unset = UNSET,
    first_section_mode: list[str] | Unset = UNSET,
    last_section_mode: list[str] | Unset = UNSET,
    max_duration_to_pt: int | Unset = UNSET,
    max_walking_duration_to_pt: int | Unset = UNSET,
    max_bike_duration_to_pt: int | Unset = UNSET,
    max_bss_duration_to_pt: int | Unset = UNSET,
    max_car_duration_to_pt: int | Unset = UNSET,
    max_ridesharing_duration_to_pt: int | Unset = UNSET,
    walking_speed: float | Unset = UNSET,
    bike_speed: float | Unset = UNSET,
    bss_speed: float | Unset = UNSET,
    car_speed: float | Unset = UNSET,
    ridesharing_speed: float | Unset = UNSET,
    taxi_speed: float | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    allowed_id: list[str] | Unset = UNSET,
    disruption_active: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    max_duration: int | Unset = UNSET,
    wheelchair: bool | Unset = UNSET,
    traveler_type: str | Unset = UNSET,
    direct_path: str | Unset = UNSET,
    free_radius_from: int | Unset = UNSET,
    free_radius_to: int | Unset = UNSET,
    resolution: int | Unset = UNSET,
) -> Response[GetCoverageRegionHeatMapsResponse200]:
    """
    Args:
        from_ (str | Unset):
        to (str | Unset):
        datetime_ (str | Unset):
        datetime_represents (str | Unset):
        max_nb_transfers (int | Unset):
        min_nb_transfers (int | Unset):
        first_section_mode (list[str] | Unset):
        last_section_mode (list[str] | Unset):
        max_duration_to_pt (int | Unset):
        max_walking_duration_to_pt (int | Unset):
        max_bike_duration_to_pt (int | Unset):
        max_bss_duration_to_pt (int | Unset):
        max_car_duration_to_pt (int | Unset):
        max_ridesharing_duration_to_pt (int | Unset):
        walking_speed (float | Unset):
        bike_speed (float | Unset):
        bss_speed (float | Unset):
        car_speed (float | Unset):
        ridesharing_speed (float | Unset):
        taxi_speed (float | Unset):
        forbidden_uris (list[str] | Unset):
        allowed_id (list[str] | Unset):
        disruption_active (bool | Unset):
        data_freshness (str | Unset):
        max_duration (int | Unset):
        wheelchair (bool | Unset):
        traveler_type (str | Unset):
        direct_path (str | Unset):
        free_radius_from (int | Unset):
        free_radius_to (int | Unset):
        resolution (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionHeatMapsResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        datetime_=datetime_,
        datetime_represents=datetime_represents,
        max_nb_transfers=max_nb_transfers,
        min_nb_transfers=min_nb_transfers,
        first_section_mode=first_section_mode,
        last_section_mode=last_section_mode,
        max_duration_to_pt=max_duration_to_pt,
        max_walking_duration_to_pt=max_walking_duration_to_pt,
        max_bike_duration_to_pt=max_bike_duration_to_pt,
        max_bss_duration_to_pt=max_bss_duration_to_pt,
        max_car_duration_to_pt=max_car_duration_to_pt,
        max_ridesharing_duration_to_pt=max_ridesharing_duration_to_pt,
        walking_speed=walking_speed,
        bike_speed=bike_speed,
        bss_speed=bss_speed,
        car_speed=car_speed,
        ridesharing_speed=ridesharing_speed,
        taxi_speed=taxi_speed,
        forbidden_uris=forbidden_uris,
        allowed_id=allowed_id,
        disruption_active=disruption_active,
        data_freshness=data_freshness,
        max_duration=max_duration,
        wheelchair=wheelchair,
        traveler_type=traveler_type,
        direct_path=direct_path,
        free_radius_from=free_radius_from,
        free_radius_to=free_radius_to,
        resolution=resolution,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    datetime_: str | Unset = UNSET,
    datetime_represents: str | Unset = UNSET,
    max_nb_transfers: int | Unset = UNSET,
    min_nb_transfers: int | Unset = UNSET,
    first_section_mode: list[str] | Unset = UNSET,
    last_section_mode: list[str] | Unset = UNSET,
    max_duration_to_pt: int | Unset = UNSET,
    max_walking_duration_to_pt: int | Unset = UNSET,
    max_bike_duration_to_pt: int | Unset = UNSET,
    max_bss_duration_to_pt: int | Unset = UNSET,
    max_car_duration_to_pt: int | Unset = UNSET,
    max_ridesharing_duration_to_pt: int | Unset = UNSET,
    walking_speed: float | Unset = UNSET,
    bike_speed: float | Unset = UNSET,
    bss_speed: float | Unset = UNSET,
    car_speed: float | Unset = UNSET,
    ridesharing_speed: float | Unset = UNSET,
    taxi_speed: float | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    allowed_id: list[str] | Unset = UNSET,
    disruption_active: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    max_duration: int | Unset = UNSET,
    wheelchair: bool | Unset = UNSET,
    traveler_type: str | Unset = UNSET,
    direct_path: str | Unset = UNSET,
    free_radius_from: int | Unset = UNSET,
    free_radius_to: int | Unset = UNSET,
    resolution: int | Unset = UNSET,
) -> GetCoverageRegionHeatMapsResponse200 | None:
    """
    Args:
        from_ (str | Unset):
        to (str | Unset):
        datetime_ (str | Unset):
        datetime_represents (str | Unset):
        max_nb_transfers (int | Unset):
        min_nb_transfers (int | Unset):
        first_section_mode (list[str] | Unset):
        last_section_mode (list[str] | Unset):
        max_duration_to_pt (int | Unset):
        max_walking_duration_to_pt (int | Unset):
        max_bike_duration_to_pt (int | Unset):
        max_bss_duration_to_pt (int | Unset):
        max_car_duration_to_pt (int | Unset):
        max_ridesharing_duration_to_pt (int | Unset):
        walking_speed (float | Unset):
        bike_speed (float | Unset):
        bss_speed (float | Unset):
        car_speed (float | Unset):
        ridesharing_speed (float | Unset):
        taxi_speed (float | Unset):
        forbidden_uris (list[str] | Unset):
        allowed_id (list[str] | Unset):
        disruption_active (bool | Unset):
        data_freshness (str | Unset):
        max_duration (int | Unset):
        wheelchair (bool | Unset):
        traveler_type (str | Unset):
        direct_path (str | Unset):
        free_radius_from (int | Unset):
        free_radius_to (int | Unset):
        resolution (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionHeatMapsResponse200
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        datetime_=datetime_,
        datetime_represents=datetime_represents,
        max_nb_transfers=max_nb_transfers,
        min_nb_transfers=min_nb_transfers,
        first_section_mode=first_section_mode,
        last_section_mode=last_section_mode,
        max_duration_to_pt=max_duration_to_pt,
        max_walking_duration_to_pt=max_walking_duration_to_pt,
        max_bike_duration_to_pt=max_bike_duration_to_pt,
        max_bss_duration_to_pt=max_bss_duration_to_pt,
        max_car_duration_to_pt=max_car_duration_to_pt,
        max_ridesharing_duration_to_pt=max_ridesharing_duration_to_pt,
        walking_speed=walking_speed,
        bike_speed=bike_speed,
        bss_speed=bss_speed,
        car_speed=car_speed,
        ridesharing_speed=ridesharing_speed,
        taxi_speed=taxi_speed,
        forbidden_uris=forbidden_uris,
        allowed_id=allowed_id,
        disruption_active=disruption_active,
        data_freshness=data_freshness,
        max_duration=max_duration,
        wheelchair=wheelchair,
        traveler_type=traveler_type,
        direct_path=direct_path,
        free_radius_from=free_radius_from,
        free_radius_to=free_radius_to,
        resolution=resolution,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    datetime_: str | Unset = UNSET,
    datetime_represents: str | Unset = UNSET,
    max_nb_transfers: int | Unset = UNSET,
    min_nb_transfers: int | Unset = UNSET,
    first_section_mode: list[str] | Unset = UNSET,
    last_section_mode: list[str] | Unset = UNSET,
    max_duration_to_pt: int | Unset = UNSET,
    max_walking_duration_to_pt: int | Unset = UNSET,
    max_bike_duration_to_pt: int | Unset = UNSET,
    max_bss_duration_to_pt: int | Unset = UNSET,
    max_car_duration_to_pt: int | Unset = UNSET,
    max_ridesharing_duration_to_pt: int | Unset = UNSET,
    walking_speed: float | Unset = UNSET,
    bike_speed: float | Unset = UNSET,
    bss_speed: float | Unset = UNSET,
    car_speed: float | Unset = UNSET,
    ridesharing_speed: float | Unset = UNSET,
    taxi_speed: float | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    allowed_id: list[str] | Unset = UNSET,
    disruption_active: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    max_duration: int | Unset = UNSET,
    wheelchair: bool | Unset = UNSET,
    traveler_type: str | Unset = UNSET,
    direct_path: str | Unset = UNSET,
    free_radius_from: int | Unset = UNSET,
    free_radius_to: int | Unset = UNSET,
    resolution: int | Unset = UNSET,
) -> Response[GetCoverageRegionHeatMapsResponse200]:
    """
    Args:
        from_ (str | Unset):
        to (str | Unset):
        datetime_ (str | Unset):
        datetime_represents (str | Unset):
        max_nb_transfers (int | Unset):
        min_nb_transfers (int | Unset):
        first_section_mode (list[str] | Unset):
        last_section_mode (list[str] | Unset):
        max_duration_to_pt (int | Unset):
        max_walking_duration_to_pt (int | Unset):
        max_bike_duration_to_pt (int | Unset):
        max_bss_duration_to_pt (int | Unset):
        max_car_duration_to_pt (int | Unset):
        max_ridesharing_duration_to_pt (int | Unset):
        walking_speed (float | Unset):
        bike_speed (float | Unset):
        bss_speed (float | Unset):
        car_speed (float | Unset):
        ridesharing_speed (float | Unset):
        taxi_speed (float | Unset):
        forbidden_uris (list[str] | Unset):
        allowed_id (list[str] | Unset):
        disruption_active (bool | Unset):
        data_freshness (str | Unset):
        max_duration (int | Unset):
        wheelchair (bool | Unset):
        traveler_type (str | Unset):
        direct_path (str | Unset):
        free_radius_from (int | Unset):
        free_radius_to (int | Unset):
        resolution (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoverageRegionHeatMapsResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        datetime_=datetime_,
        datetime_represents=datetime_represents,
        max_nb_transfers=max_nb_transfers,
        min_nb_transfers=min_nb_transfers,
        first_section_mode=first_section_mode,
        last_section_mode=last_section_mode,
        max_duration_to_pt=max_duration_to_pt,
        max_walking_duration_to_pt=max_walking_duration_to_pt,
        max_bike_duration_to_pt=max_bike_duration_to_pt,
        max_bss_duration_to_pt=max_bss_duration_to_pt,
        max_car_duration_to_pt=max_car_duration_to_pt,
        max_ridesharing_duration_to_pt=max_ridesharing_duration_to_pt,
        walking_speed=walking_speed,
        bike_speed=bike_speed,
        bss_speed=bss_speed,
        car_speed=car_speed,
        ridesharing_speed=ridesharing_speed,
        taxi_speed=taxi_speed,
        forbidden_uris=forbidden_uris,
        allowed_id=allowed_id,
        disruption_active=disruption_active,
        data_freshness=data_freshness,
        max_duration=max_duration,
        wheelchair=wheelchair,
        traveler_type=traveler_type,
        direct_path=direct_path,
        free_radius_from=free_radius_from,
        free_radius_to=free_radius_to,
        resolution=resolution,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    datetime_: str | Unset = UNSET,
    datetime_represents: str | Unset = UNSET,
    max_nb_transfers: int | Unset = UNSET,
    min_nb_transfers: int | Unset = UNSET,
    first_section_mode: list[str] | Unset = UNSET,
    last_section_mode: list[str] | Unset = UNSET,
    max_duration_to_pt: int | Unset = UNSET,
    max_walking_duration_to_pt: int | Unset = UNSET,
    max_bike_duration_to_pt: int | Unset = UNSET,
    max_bss_duration_to_pt: int | Unset = UNSET,
    max_car_duration_to_pt: int | Unset = UNSET,
    max_ridesharing_duration_to_pt: int | Unset = UNSET,
    walking_speed: float | Unset = UNSET,
    bike_speed: float | Unset = UNSET,
    bss_speed: float | Unset = UNSET,
    car_speed: float | Unset = UNSET,
    ridesharing_speed: float | Unset = UNSET,
    taxi_speed: float | Unset = UNSET,
    forbidden_uris: list[str] | Unset = UNSET,
    allowed_id: list[str] | Unset = UNSET,
    disruption_active: bool | Unset = UNSET,
    data_freshness: str | Unset = UNSET,
    max_duration: int | Unset = UNSET,
    wheelchair: bool | Unset = UNSET,
    traveler_type: str | Unset = UNSET,
    direct_path: str | Unset = UNSET,
    free_radius_from: int | Unset = UNSET,
    free_radius_to: int | Unset = UNSET,
    resolution: int | Unset = UNSET,
) -> GetCoverageRegionHeatMapsResponse200 | None:
    """
    Args:
        from_ (str | Unset):
        to (str | Unset):
        datetime_ (str | Unset):
        datetime_represents (str | Unset):
        max_nb_transfers (int | Unset):
        min_nb_transfers (int | Unset):
        first_section_mode (list[str] | Unset):
        last_section_mode (list[str] | Unset):
        max_duration_to_pt (int | Unset):
        max_walking_duration_to_pt (int | Unset):
        max_bike_duration_to_pt (int | Unset):
        max_bss_duration_to_pt (int | Unset):
        max_car_duration_to_pt (int | Unset):
        max_ridesharing_duration_to_pt (int | Unset):
        walking_speed (float | Unset):
        bike_speed (float | Unset):
        bss_speed (float | Unset):
        car_speed (float | Unset):
        ridesharing_speed (float | Unset):
        taxi_speed (float | Unset):
        forbidden_uris (list[str] | Unset):
        allowed_id (list[str] | Unset):
        disruption_active (bool | Unset):
        data_freshness (str | Unset):
        max_duration (int | Unset):
        wheelchair (bool | Unset):
        traveler_type (str | Unset):
        direct_path (str | Unset):
        free_radius_from (int | Unset):
        free_radius_to (int | Unset):
        resolution (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoverageRegionHeatMapsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            datetime_=datetime_,
            datetime_represents=datetime_represents,
            max_nb_transfers=max_nb_transfers,
            min_nb_transfers=min_nb_transfers,
            first_section_mode=first_section_mode,
            last_section_mode=last_section_mode,
            max_duration_to_pt=max_duration_to_pt,
            max_walking_duration_to_pt=max_walking_duration_to_pt,
            max_bike_duration_to_pt=max_bike_duration_to_pt,
            max_bss_duration_to_pt=max_bss_duration_to_pt,
            max_car_duration_to_pt=max_car_duration_to_pt,
            max_ridesharing_duration_to_pt=max_ridesharing_duration_to_pt,
            walking_speed=walking_speed,
            bike_speed=bike_speed,
            bss_speed=bss_speed,
            car_speed=car_speed,
            ridesharing_speed=ridesharing_speed,
            taxi_speed=taxi_speed,
            forbidden_uris=forbidden_uris,
            allowed_id=allowed_id,
            disruption_active=disruption_active,
            data_freshness=data_freshness,
            max_duration=max_duration,
            wheelchair=wheelchair,
            traveler_type=traveler_type,
            direct_path=direct_path,
            free_radius_from=free_radius_from,
            free_radius_to=free_radius_to,
            resolution=resolution,
        )
    ).parsed
