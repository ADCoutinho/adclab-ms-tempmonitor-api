# resources/routes.py

from .readings import ReadingsApi,ReadingApi

def initialize_routes(api):
    api.add_resource(ReadingsApi, '/api/v1/readings')
    api.add_resource(ReadingApi, '/api/v1/readings/<id>')