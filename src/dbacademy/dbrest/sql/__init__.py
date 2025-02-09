from dbacademy.dbrest import DBAcademyRestClient
from dbacademy.clients.rest.common import ApiContainer


class SqlClient(ApiContainer):
    def __init__(self, client: DBAcademyRestClient):
        self.client = client      # Client API exposing other operations to this class

        from dbacademy.dbrest.sql.config import SqlConfigClient
        self.config = SqlConfigClient(self.client)

        from dbacademy.dbrest.sql.endpoints import SqlWarehousesClient
        self.warehouses = SqlWarehousesClient(self.client)
        self.endpoints = SqlWarehousesClient(self.client)  # Backwards Compatibility

        from dbacademy.dbrest.sql.queries import SqlQueriesClient
        self.queries = SqlQueriesClient(self.client)

        from dbacademy.dbrest.sql.statements import StatementsClient
        self.statements = StatementsClient(self.client)

        self.permissions = client.permissions.sql
