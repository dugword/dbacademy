from dbacademy.clients.rest.common import ApiClient
from dbacademy.clients.rest.permissions.crud import PermissionsCrud

__all__ = ["Warehouses"]


class Warehouses(PermissionsCrud):
    valid_permissions = ["CAN_USE", "CAN_MANAGE"]

    def __init__(self, client: ApiClient):
        super().__init__(client, "2.0/permissions/sql/warehouses", "warehouses")
