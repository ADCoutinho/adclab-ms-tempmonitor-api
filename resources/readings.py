# resources/readings.py

from flask import Response, request
from database.models import SensorReadings
from flask_restful import Resource


class ReadingsApi(Resource):
    def post(self):
        body = request.get_json()
        reading = SensorReadings(**body).save()
        id = reading.id
        return {'id': str(id)}, 200


class ReadingApi(Resource):
    def get(self, id):
        reading = SensorReadings.objects.get(id=id).to_json()
        return Response(reading, mimetype="application/json", status=200)
