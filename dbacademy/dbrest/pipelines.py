# Databricks notebook source
from dbacademy.dbrest import DBAcademyRestClient


class PipelinesClient:
    def __init__(self, client: DBAcademyRestClient, token: str, endpoint: str):
        self.client = client
        self.token = token
        self.endpoint = endpoint

        self.base_uri = f"{self.endpoint}/api/2.0/pipelines"

    def list(self):
        return self.client.execute_get_json(f"{self.base_uri}")

    # def list_events_by_id(self):
    #     return self.client.execute_get_json(f"{self.base_uri}/{pipeline_id}/events")

    # def list_events_by_id(self):
    #     return self.client.execute_get_json(f"{self.base_uri}/{pipeline_id}/events")

    def get_by_id(self, pipeline_id):
        return self.client.execute_get_json(f"{self.base_uri}/{pipeline_id}")

    # def get_updates_by_id(self, pipeline_id, update_id):
    #     return self.client.execute_get_json(f"{self.base_uri}/{pipeline_id}/updates/{update_id}")

    def delete_by_id(self, pipelines):
        return self.client.execute_delete_json(f"{self.base_uri}/{pipeline_id}")

    def existing_to_create(self, pipeline:dict):
        assert type(pipeline) == dict, f"Expected the \"pipeline\" parameter to be of type dict, found {type(pipeline)}"

        # for key in list(query.keys()):
        #     if key not in ["query", "name", "description", "schedule", "options"]:
        #         del query[key]

        # return query

    def create_from_dict(self, params:dict):
        return self.client.execute_post_json(f"{self.base_uri}", params)

    def create(self, name:str, storage:str, target:str, continuous:bool, development:bool, configuration:dict, libraries:list, clusters:list = None):
        
        if clusters == None: clusters = []
        assert type(clusters) == list, f"Expected clusters to be of type list, found {type(clusters)}"
        if len(clusters) == 0:
            clusters.append({
                "num_workers": 1
            })    

        assert type(libraries) == list, f"Expected libraries to be of type list, found {type(libraries)}"
        for library in libraries:
            notebook = library.get("notebook")
            assert notebook is not None, f"The library's notebook parameter must be specified."
            
            path = notebook.get("path")
            assert path is not None, f"The library's notebook's path parameter must be specified."
        
        params = dict()
        params["name"] = name
        params["storage"] = storage
        params["configuration"] = configuration
        params["clusters"] = clusters
        params["libraries"] = libraries
        params["target"] = target
        params["continuous"] = continuous
        params["development"] = development

        return self.create_from_dict(params)
