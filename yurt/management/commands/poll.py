from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from yurt.nest import get_nest_wrapper
from yurt.models import (
    NestTemperatureReading,
    NestHumidityReading,
    NestTemperatureTarget,
    NestHumidityTarget,
)


def totes_insert(klass, *args, **kwargs):
    try:
        return klass.objects.create(*args, **kwargs).save()
    except IntegrityError:
        pass  # lamesauce.

class Command(BaseCommand):
    args = '<none>'
    help = 'update the server'

    def handle(self, **kwargs):
        api = get_nest_wrapper()
        for house in api.get_structures():
            for device in house.get_sensors():
                when = device.get_timestamp()
                readings = device.get_current_readings()
                targets = device.get_target_readings()
                # OK. Let's store the data.

                totes_insert(NestTemperatureReading, when=when,
                             measurement=readings['temperature'])

                totes_insert(NestHumidityReading, when=when,
                             measurement=readings['humidity'])

                totes_insert(NestTemperatureTarget,
                             when=when, **targets['temperature'])

                totes_insert(NestHumidityTarget,
                             when=when,
                             **targets['temperature'])
