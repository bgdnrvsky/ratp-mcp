"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .admin import Admin
from .amount import Amount
from .beta_endpoints import BetaEndpoints
from .calendar import Calendar
from .calendar_exception import CalendarException
from .calendar_period import CalendarPeriod
from .car_park import CarPark
from .cause import Cause
from .cell_lat_schema import CellLatSchema
from .cell_lon_schema import CellLonSchema
from .channel import Channel
from .channel_types_item import ChannelTypesItem
from .co2 import CO2
from .code import Code
from .comment import Comment
from .commercial_mode import CommercialMode
from .companie import Companie
from .context import Context
from .contributor import Contributor
from .coord import Coord
from .cost import Cost
from .coverage import Coverage
from .coverage_error import CoverageError
from .current_availability import CurrentAvailability
from .current_availability_status import CurrentAvailabilityStatus
from .dataset import Dataset
from .date_time_type import DateTimeType
from .disruption import Disruption
from .disruption_property import DisruptionProperty
from .disruption_status import DisruptionStatus
from .disruptions_response import DisruptionsResponse
from .distances import Distances
from .durations import Durations
from .effect import Effect
from .equipment_details import EquipmentDetails
from .equipment_details_embedded_type import EquipmentDetailsEmbeddedType
from .equipment_report import EquipmentReport
from .error import Error
from .exception import Exception_
from .fare import Fare
from .fare_zone import FareZone
from .feed_publisher import FeedPublisher
from .geo_status import GeoStatus
from .get_coverage_region_addresses_id_response_200 import GetCoverageRegionAddressesIdResponse200
from .get_coverage_region_arrivals_response_200 import GetCoverageRegionArrivalsResponse200
from .get_coverage_region_calendars_id_response_200 import GetCoverageRegionCalendarsIdResponse200
from .get_coverage_region_calendars_response_200 import GetCoverageRegionCalendarsResponse200
from .get_coverage_region_commercial_modes_id_response_200 import GetCoverageRegionCommercialModesIdResponse200
from .get_coverage_region_commercial_modes_response_200 import GetCoverageRegionCommercialModesResponse200
from .get_coverage_region_companies_id_response_200 import GetCoverageRegionCompaniesIdResponse200
from .get_coverage_region_companies_response_200 import GetCoverageRegionCompaniesResponse200
from .get_coverage_region_coord_id_response_200 import GetCoverageRegionCoordIdResponse200
from .get_coverage_region_coord_response_200 import GetCoverageRegionCoordResponse200
from .get_coverage_region_coords_id_response_200 import GetCoverageRegionCoordsIdResponse200
from .get_coverage_region_coords_response_200 import GetCoverageRegionCoordsResponse200
from .get_coverage_region_datasets_response_200 import GetCoverageRegionDatasetsResponse200
from .get_coverage_region_departures_response_200 import GetCoverageRegionDeparturesResponse200
from .get_coverage_region_disruptions_id_response_200 import GetCoverageRegionDisruptionsIdResponse200
from .get_coverage_region_equipment_reports_response_200 import GetCoverageRegionEquipmentReportsResponse200
from .get_coverage_region_geo_status_response_200 import GetCoverageRegionGeoStatusResponse200
from .get_coverage_region_heat_maps_response_200 import GetCoverageRegionHeatMapsResponse200
from .get_coverage_region_journey_pattern_points_id_response_200 import (
    GetCoverageRegionJourneyPatternPointsIdResponse200,
)
from .get_coverage_region_journey_pattern_points_response_200 import GetCoverageRegionJourneyPatternPointsResponse200
from .get_coverage_region_journey_patterns_id_response_200 import GetCoverageRegionJourneyPatternsIdResponse200
from .get_coverage_region_journey_patterns_response_200 import GetCoverageRegionJourneyPatternsResponse200
from .get_coverage_region_journeys_response_200 import GetCoverageRegionJourneysResponse200
from .get_coverage_region_line_groups_id_response_200 import GetCoverageRegionLineGroupsIdResponse200
from .get_coverage_region_line_groups_response_200 import GetCoverageRegionLineGroupsResponse200
from .get_coverage_region_lines_id_response_200 import GetCoverageRegionLinesIdResponse200
from .get_coverage_region_networks_id_response_200 import GetCoverageRegionNetworksIdResponse200
from .get_coverage_region_networks_response_200 import GetCoverageRegionNetworksResponse200
from .get_coverage_region_physical_modes_id_response_200 import GetCoverageRegionPhysicalModesIdResponse200
from .get_coverage_region_physical_modes_response_200 import GetCoverageRegionPhysicalModesResponse200
from .get_coverage_region_places_id_response_200 import GetCoverageRegionPlacesIdResponse200
from .get_coverage_region_places_nearby_response_200 import GetCoverageRegionPlacesNearbyResponse200
from .get_coverage_region_places_response_200 import GetCoverageRegionPlacesResponse200
from .get_coverage_region_poi_types_id_response_200 import GetCoverageRegionPoiTypesIdResponse200
from .get_coverage_region_poi_types_response_200 import GetCoverageRegionPoiTypesResponse200
from .get_coverage_region_pois_id_response_200 import GetCoverageRegionPoisIdResponse200
from .get_coverage_region_pois_response_200 import GetCoverageRegionPoisResponse200
from .get_coverage_region_pt_objects_response_200 import GetCoverageRegionPtObjectsResponse200
from .get_coverage_region_response_200 import GetCoverageRegionResponse200
from .get_coverage_region_routes_id_response_200 import GetCoverageRegionRoutesIdResponse200
from .get_coverage_region_routes_response_200 import GetCoverageRegionRoutesResponse200
from .get_coverage_region_stop_areas_id_response_200 import GetCoverageRegionStopAreasIdResponse200
from .get_coverage_region_stop_points_id_response_200 import GetCoverageRegionStopPointsIdResponse200
from .get_coverage_region_stop_points_response_200 import GetCoverageRegionStopPointsResponse200
from .get_coverage_region_traffic_reports_response_200 import GetCoverageRegionTrafficReportsResponse200
from .get_coverage_region_trips_id_response_200 import GetCoverageRegionTripsIdResponse200
from .get_coverage_region_trips_response_200 import GetCoverageRegionTripsResponse200
from .get_coverage_region_uri_addresses_id_response_200 import GetCoverageRegionUriAddressesIdResponse200
from .get_coverage_region_uri_addresses_response_200 import GetCoverageRegionUriAddressesResponse200
from .get_coverage_region_uri_arrivals_response_200 import GetCoverageRegionUriArrivalsResponse200
from .get_coverage_region_uri_calendars_response_200 import GetCoverageRegionUriCalendarsResponse200
from .get_coverage_region_uri_commercial_modes_id_response_200 import GetCoverageRegionUriCommercialModesIdResponse200
from .get_coverage_region_uri_commercial_modes_response_200 import GetCoverageRegionUriCommercialModesResponse200
from .get_coverage_region_uri_companies_id_response_200 import GetCoverageRegionUriCompaniesIdResponse200
from .get_coverage_region_uri_companies_response_200 import GetCoverageRegionUriCompaniesResponse200
from .get_coverage_region_uri_contributors_response_200 import GetCoverageRegionUriContributorsResponse200
from .get_coverage_region_uri_coord_id_response_200 import GetCoverageRegionUriCoordIdResponse200
from .get_coverage_region_uri_coord_response_200 import GetCoverageRegionUriCoordResponse200
from .get_coverage_region_uri_coords_id_response_200 import GetCoverageRegionUriCoordsIdResponse200
from .get_coverage_region_uri_coords_response_200 import GetCoverageRegionUriCoordsResponse200
from .get_coverage_region_uri_datasets_response_200 import GetCoverageRegionUriDatasetsResponse200
from .get_coverage_region_uri_departures_response_200 import GetCoverageRegionUriDeparturesResponse200
from .get_coverage_region_uri_disruptions_id_response_200 import GetCoverageRegionUriDisruptionsIdResponse200
from .get_coverage_region_uri_disruptions_response_200 import GetCoverageRegionUriDisruptionsResponse200
from .get_coverage_region_uri_equipment_reports_response_200 import GetCoverageRegionUriEquipmentReportsResponse200
from .get_coverage_region_uri_journey_pattern_points_id_response_200 import (
    GetCoverageRegionUriJourneyPatternPointsIdResponse200,
)
from .get_coverage_region_uri_journey_pattern_points_response_200 import (
    GetCoverageRegionUriJourneyPatternPointsResponse200,
)
from .get_coverage_region_uri_journey_patterns_id_response_200 import GetCoverageRegionUriJourneyPatternsIdResponse200
from .get_coverage_region_uri_journey_patterns_response_200 import GetCoverageRegionUriJourneyPatternsResponse200
from .get_coverage_region_uri_line_groups_id_response_200 import GetCoverageRegionUriLineGroupsIdResponse200
from .get_coverage_region_uri_line_groups_response_200 import GetCoverageRegionUriLineGroupsResponse200
from .get_coverage_region_uri_lines_id_response_200 import GetCoverageRegionUriLinesIdResponse200
from .get_coverage_region_uri_lines_response_200 import GetCoverageRegionUriLinesResponse200
from .get_coverage_region_uri_networks_id_response_200 import GetCoverageRegionUriNetworksIdResponse200
from .get_coverage_region_uri_networks_response_200 import GetCoverageRegionUriNetworksResponse200
from .get_coverage_region_uri_physical_modes_id_response_200 import GetCoverageRegionUriPhysicalModesIdResponse200
from .get_coverage_region_uri_physical_modes_response_200 import GetCoverageRegionUriPhysicalModesResponse200
from .get_coverage_region_uri_places_nearby_response_200 import GetCoverageRegionUriPlacesNearbyResponse200
from .get_coverage_region_uri_poi_types_id_response_200 import GetCoverageRegionUriPoiTypesIdResponse200
from .get_coverage_region_uri_poi_types_response_200 import GetCoverageRegionUriPoiTypesResponse200
from .get_coverage_region_uri_pois_id_response_200 import GetCoverageRegionUriPoisIdResponse200
from .get_coverage_region_uri_pois_response_200 import GetCoverageRegionUriPoisResponse200
from .get_coverage_region_uri_route_schedules_response_200 import GetCoverageRegionUriRouteSchedulesResponse200
from .get_coverage_region_uri_routes_id_response_200 import GetCoverageRegionUriRoutesIdResponse200
from .get_coverage_region_uri_routes_response_200 import GetCoverageRegionUriRoutesResponse200
from .get_coverage_region_uri_stop_areas_id_response_200 import GetCoverageRegionUriStopAreasIdResponse200
from .get_coverage_region_uri_stop_areas_response_200 import GetCoverageRegionUriStopAreasResponse200
from .get_coverage_region_uri_stop_points_id_response_200 import GetCoverageRegionUriStopPointsIdResponse200
from .get_coverage_region_uri_stop_points_response_200 import GetCoverageRegionUriStopPointsResponse200
from .get_coverage_region_uri_stop_schedules_response_200 import GetCoverageRegionUriStopSchedulesResponse200
from .get_coverage_region_uri_traffic_reports_response_200 import GetCoverageRegionUriTrafficReportsResponse200
from .get_coverage_region_uri_trips_id_response_200 import GetCoverageRegionUriTripsIdResponse200
from .get_coverage_region_uri_trips_response_200 import GetCoverageRegionUriTripsResponse200
from .get_coverage_region_uri_vehicle_journeys_id_response_200 import GetCoverageRegionUriVehicleJourneysIdResponse200
from .get_coverage_region_uri_vehicle_journeys_response_200 import GetCoverageRegionUriVehicleJourneysResponse200
from .get_coverage_region_vehicle_journeys_id_response_200 import GetCoverageRegionVehicleJourneysIdResponse200
from .get_coverage_region_vehicle_journeys_response_200 import GetCoverageRegionVehicleJourneysResponse200
from .graphical_isrochone import GraphicalIsrochone
from .graphical_isrochone_geojson import GraphicalIsrochoneGeojson
from .graphical_isrochone_geojson_type import GraphicalIsrochoneGeojsonType
from .header import Header
from .heat_map import HeatMap
from .heat_matrix_schema import HeatMatrixSchema
from .impacted import Impacted
from .impacted_section import ImpactedSection
from .impacted_stop import ImpactedStop
from .impacted_stop_stop_time_effect import ImpactedStopStopTimeEffect
from .individual_information import IndividualInformation
from .individual_information_gender import IndividualInformationGender
from .individual_rating import IndividualRating
from .journey import Journey
from .journey_debug import JourneyDebug
from .journey_pattern import JourneyPattern
from .journey_pattern_point import JourneyPatternPoint
from .line import Line
from .line_group import LineGroup
from .line_headers_schema import LineHeadersSchema
from .line_report import LineReport
from .lines_response import LinesResponse
from .lines_schema import LinesSchema
from .link import Link
from .link_schema import LinkSchema
from .message import Message
from .multi_line_string_schema import MultiLineStringSchema
from .network import Network
from .note import Note
from .note_category import NoteCategory
from .pagination import Pagination
from .passage import Passage
from .path import Path
from .period import Period
from .physical_mode import PhysicalMode
from .place import Place
from .place_embedded_type import PlaceEmbeddedType
from .place_nearby import PlaceNearby
from .place_nearby_embedded_type import PlaceNearbyEmbeddedType
from .poi import Poi
from .poi_properties import PoiProperties
from .poi_type import PoiType
from .property_ import Property
from .pt_object import PtObject
from .pt_object_embedded_type import PtObjectEmbeddedType
from .ridesharing_information import RidesharingInformation
from .route import Route
from .route_display_information import RouteDisplayInformation
from .route_is_frequence import RouteIsFrequence
from .route_schedule import RouteSchedule
from .row import Row
from .seats_description import SeatsDescription
from .section import Section
from .section_additional_informations_item import SectionAdditionalInformationsItem
from .section_data_freshness import SectionDataFreshness
from .section_geo_json_schema import SectionGeoJsonSchema
from .section_geo_json_schema_properties_item import SectionGeoJsonSchemaPropertiesItem
from .section_mode import SectionMode
from .section_transfer_type import SectionTransferType
from .section_type import SectionType
from .severity import Severity
from .severity_effect import SeverityEffect
from .stands import Stands
from .stands_status import StandsStatus
from .stop_area import StopArea
from .stop_area_equipments import StopAreaEquipments
from .stop_areas_response import StopAreasResponse
from .stop_date_time import StopDateTime
from .stop_date_time_additional_informations_item import StopDateTimeAdditionalInformationsItem
from .stop_date_time_data_freshness import StopDateTimeDataFreshness
from .stop_point import StopPoint
from .stop_point_equipments_item import StopPointEquipmentsItem
from .stop_schedule import StopSchedule
from .stop_time import StopTime
from .table import Table
from .ticket import Ticket
from .traffic_report import TrafficReport
from .trip import Trip
from .validity_pattern import ValidityPattern
from .vehicle_journey import VehicleJourney
from .vj_display_information import VJDisplayInformation
from .vj_display_information_equipments_item import VJDisplayInformationEquipmentsItem
from .week_pattern import WeekPattern

__all__ = (
    "Address",
    "Admin",
    "Amount",
    "BetaEndpoints",
    "Calendar",
    "CalendarException",
    "CalendarPeriod",
    "CarPark",
    "Cause",
    "CellLatSchema",
    "CellLonSchema",
    "Channel",
    "ChannelTypesItem",
    "CO2",
    "Code",
    "Comment",
    "CommercialMode",
    "Companie",
    "Context",
    "Contributor",
    "Coord",
    "Cost",
    "Coverage",
    "CoverageError",
    "CurrentAvailability",
    "CurrentAvailabilityStatus",
    "Dataset",
    "DateTimeType",
    "Disruption",
    "DisruptionProperty",
    "DisruptionsResponse",
    "DisruptionStatus",
    "Distances",
    "Durations",
    "Effect",
    "EquipmentDetails",
    "EquipmentDetailsEmbeddedType",
    "EquipmentReport",
    "Error",
    "Exception_",
    "Fare",
    "FareZone",
    "FeedPublisher",
    "GeoStatus",
    "GetCoverageRegionAddressesIdResponse200",
    "GetCoverageRegionArrivalsResponse200",
    "GetCoverageRegionCalendarsIdResponse200",
    "GetCoverageRegionCalendarsResponse200",
    "GetCoverageRegionCommercialModesIdResponse200",
    "GetCoverageRegionCommercialModesResponse200",
    "GetCoverageRegionCompaniesIdResponse200",
    "GetCoverageRegionCompaniesResponse200",
    "GetCoverageRegionCoordIdResponse200",
    "GetCoverageRegionCoordResponse200",
    "GetCoverageRegionCoordsIdResponse200",
    "GetCoverageRegionCoordsResponse200",
    "GetCoverageRegionDatasetsResponse200",
    "GetCoverageRegionDeparturesResponse200",
    "GetCoverageRegionDisruptionsIdResponse200",
    "GetCoverageRegionEquipmentReportsResponse200",
    "GetCoverageRegionGeoStatusResponse200",
    "GetCoverageRegionHeatMapsResponse200",
    "GetCoverageRegionJourneyPatternPointsIdResponse200",
    "GetCoverageRegionJourneyPatternPointsResponse200",
    "GetCoverageRegionJourneyPatternsIdResponse200",
    "GetCoverageRegionJourneyPatternsResponse200",
    "GetCoverageRegionJourneysResponse200",
    "GetCoverageRegionLineGroupsIdResponse200",
    "GetCoverageRegionLineGroupsResponse200",
    "GetCoverageRegionLinesIdResponse200",
    "GetCoverageRegionNetworksIdResponse200",
    "GetCoverageRegionNetworksResponse200",
    "GetCoverageRegionPhysicalModesIdResponse200",
    "GetCoverageRegionPhysicalModesResponse200",
    "GetCoverageRegionPlacesIdResponse200",
    "GetCoverageRegionPlacesNearbyResponse200",
    "GetCoverageRegionPlacesResponse200",
    "GetCoverageRegionPoisIdResponse200",
    "GetCoverageRegionPoisResponse200",
    "GetCoverageRegionPoiTypesIdResponse200",
    "GetCoverageRegionPoiTypesResponse200",
    "GetCoverageRegionPtObjectsResponse200",
    "GetCoverageRegionResponse200",
    "GetCoverageRegionRoutesIdResponse200",
    "GetCoverageRegionRoutesResponse200",
    "GetCoverageRegionStopAreasIdResponse200",
    "GetCoverageRegionStopPointsIdResponse200",
    "GetCoverageRegionStopPointsResponse200",
    "GetCoverageRegionTrafficReportsResponse200",
    "GetCoverageRegionTripsIdResponse200",
    "GetCoverageRegionTripsResponse200",
    "GetCoverageRegionUriAddressesIdResponse200",
    "GetCoverageRegionUriAddressesResponse200",
    "GetCoverageRegionUriArrivalsResponse200",
    "GetCoverageRegionUriCalendarsResponse200",
    "GetCoverageRegionUriCommercialModesIdResponse200",
    "GetCoverageRegionUriCommercialModesResponse200",
    "GetCoverageRegionUriCompaniesIdResponse200",
    "GetCoverageRegionUriCompaniesResponse200",
    "GetCoverageRegionUriContributorsResponse200",
    "GetCoverageRegionUriCoordIdResponse200",
    "GetCoverageRegionUriCoordResponse200",
    "GetCoverageRegionUriCoordsIdResponse200",
    "GetCoverageRegionUriCoordsResponse200",
    "GetCoverageRegionUriDatasetsResponse200",
    "GetCoverageRegionUriDeparturesResponse200",
    "GetCoverageRegionUriDisruptionsIdResponse200",
    "GetCoverageRegionUriDisruptionsResponse200",
    "GetCoverageRegionUriEquipmentReportsResponse200",
    "GetCoverageRegionUriJourneyPatternPointsIdResponse200",
    "GetCoverageRegionUriJourneyPatternPointsResponse200",
    "GetCoverageRegionUriJourneyPatternsIdResponse200",
    "GetCoverageRegionUriJourneyPatternsResponse200",
    "GetCoverageRegionUriLineGroupsIdResponse200",
    "GetCoverageRegionUriLineGroupsResponse200",
    "GetCoverageRegionUriLinesIdResponse200",
    "GetCoverageRegionUriLinesResponse200",
    "GetCoverageRegionUriNetworksIdResponse200",
    "GetCoverageRegionUriNetworksResponse200",
    "GetCoverageRegionUriPhysicalModesIdResponse200",
    "GetCoverageRegionUriPhysicalModesResponse200",
    "GetCoverageRegionUriPlacesNearbyResponse200",
    "GetCoverageRegionUriPoisIdResponse200",
    "GetCoverageRegionUriPoisResponse200",
    "GetCoverageRegionUriPoiTypesIdResponse200",
    "GetCoverageRegionUriPoiTypesResponse200",
    "GetCoverageRegionUriRouteSchedulesResponse200",
    "GetCoverageRegionUriRoutesIdResponse200",
    "GetCoverageRegionUriRoutesResponse200",
    "GetCoverageRegionUriStopAreasIdResponse200",
    "GetCoverageRegionUriStopAreasResponse200",
    "GetCoverageRegionUriStopPointsIdResponse200",
    "GetCoverageRegionUriStopPointsResponse200",
    "GetCoverageRegionUriStopSchedulesResponse200",
    "GetCoverageRegionUriTrafficReportsResponse200",
    "GetCoverageRegionUriTripsIdResponse200",
    "GetCoverageRegionUriTripsResponse200",
    "GetCoverageRegionUriVehicleJourneysIdResponse200",
    "GetCoverageRegionUriVehicleJourneysResponse200",
    "GetCoverageRegionVehicleJourneysIdResponse200",
    "GetCoverageRegionVehicleJourneysResponse200",
    "GraphicalIsrochone",
    "GraphicalIsrochoneGeojson",
    "GraphicalIsrochoneGeojsonType",
    "Header",
    "HeatMap",
    "HeatMatrixSchema",
    "Impacted",
    "ImpactedSection",
    "ImpactedStop",
    "ImpactedStopStopTimeEffect",
    "IndividualInformation",
    "IndividualInformationGender",
    "IndividualRating",
    "Journey",
    "JourneyDebug",
    "JourneyPattern",
    "JourneyPatternPoint",
    "Line",
    "LineGroup",
    "LineHeadersSchema",
    "LineReport",
    "LinesResponse",
    "LinesSchema",
    "Link",
    "LinkSchema",
    "Message",
    "MultiLineStringSchema",
    "Network",
    "Note",
    "NoteCategory",
    "Pagination",
    "Passage",
    "Path",
    "Period",
    "PhysicalMode",
    "Place",
    "PlaceEmbeddedType",
    "PlaceNearby",
    "PlaceNearbyEmbeddedType",
    "Poi",
    "PoiProperties",
    "PoiType",
    "Property",
    "PtObject",
    "PtObjectEmbeddedType",
    "RidesharingInformation",
    "Route",
    "RouteDisplayInformation",
    "RouteIsFrequence",
    "RouteSchedule",
    "Row",
    "SeatsDescription",
    "Section",
    "SectionAdditionalInformationsItem",
    "SectionDataFreshness",
    "SectionGeoJsonSchema",
    "SectionGeoJsonSchemaPropertiesItem",
    "SectionMode",
    "SectionTransferType",
    "SectionType",
    "Severity",
    "SeverityEffect",
    "Stands",
    "StandsStatus",
    "StopArea",
    "StopAreaEquipments",
    "StopAreasResponse",
    "StopDateTime",
    "StopDateTimeAdditionalInformationsItem",
    "StopDateTimeDataFreshness",
    "StopPoint",
    "StopPointEquipmentsItem",
    "StopSchedule",
    "StopTime",
    "Table",
    "Ticket",
    "TrafficReport",
    "Trip",
    "ValidityPattern",
    "VehicleJourney",
    "VJDisplayInformation",
    "VJDisplayInformationEquipmentsItem",
    "WeekPattern",
)
