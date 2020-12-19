# database/models.py

from .db import db
import datetime as dt


class SensorReadings(db.Document):
    client = db.StringField(require=True)
    sensor = db.IntField(required=True)
    reading_time = db.DateTimeField(default=dt.datetime.utcnow)
    temp = db.FloatField(required=True)
