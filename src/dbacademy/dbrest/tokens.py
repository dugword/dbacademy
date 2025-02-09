from dbacademy.dbrest import DBAcademyRestClient
from dbacademy.clients.rest.common import ApiContainer


class TokensClient(ApiContainer):
    def __init__(self, client: DBAcademyRestClient):
        self.client = client
        self.base_url = f"{self.client.endpoint}/api/2.0/token"

    def list(self):
        results = self.client.api("GET", f"{self.base_url}/list")
        return results["token_infos"]

    def create(self, comment: str, lifetime_seconds: int):
        params = {
            "comment": comment,
            "lifetime_seconds": lifetime_seconds
        }
        return self.client.api("POST", f"{self.base_url}/create", params)

    def revoke(self, token_id):
        params = {
            "token_id": token_id
        }
        return self.client.api("POST", f"{self.base_url}/delete", params)
