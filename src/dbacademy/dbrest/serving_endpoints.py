from dbacademy.dbrest import DBAcademyRestClient
from dbacademy.clients.rest.common import ApiContainer


class ServingEndpointsClient(ApiContainer):
    def __init__(self, client: DBAcademyRestClient):
        self.client = client
        self.base_url = f"{self.client.endpoint}/api/2.0/serving-endpoints"

    def list_endpoints(self) -> dict:
        response = self.client.api("GET", self.base_url)
        return response.get("endpoints", list())

    def get_by_name(self, name):
        return self.client.api("GET", f"{self.base_url}/{name}")

    def delete_by_name(self, name):
        self.client.api("DELETE", f"{self.base_url}/{name}")
        return None
