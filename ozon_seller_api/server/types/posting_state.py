from enum import StrEnum


class PostingState(StrEnum):
    POSTING_ACCEPTANCE_IN_PROGRESS = "posting_acceptance_in_progress"
    POSTING_CREATED = "posting_created"
    POSTING_AWAITING_REGISTRATION = "posting_awaiting_registration"
    POSTING_TRANSFERRING_TO_DELIVERY = "posting_transferring_to_delivery"
    POSTING_IN_CARRIAGE = "posting_in_carriage"
    POSTING_NOT_IN_CARRIAGE = "posting_not_in_carriage"
    POSTING_IN_ARBITRATION = "posting_in_arbitration"
    POSTING_IN_CLIENT_ARBITRATION = "posting_in_client_arbitration"
    POSTING_ON_WAY_TO_CITY = "posting_on_way_to_city"
    POSTING_TRANSFERRED_TO_COURIER_SERVICE = "posting_transferred_to_courier_service"
    POSTING_IN_COURIER_SERVICE = "posting_in_courier_service"
    POSTING_ON_WAY_TO_PICKUP_POINT = "posting_on_way_to_pickup_point"
    POSTING_IN_PICKUP_POINT = "posting_in_pickup_point"
    POSTING_CONDITIONALLY_DELIVERED = "posting_conditionally_delivered"
    POSTING_DRIVER_PICK_UP = "posting_driver_pick_up"
    POSTING_DELIVERED = "posting_delivered"
    POSTING_RECEIVED = "posting_received"
    POSTING_CANCELED = "posting_canceled"
    POSTING_NOT_IN_SORT_CENTER = "posting_not_in_sort_center"
