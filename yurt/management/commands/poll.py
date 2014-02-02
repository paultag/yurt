from django.core.management.base import BaseCommand, CommandError
from yurt.nest import get_nest_wrapper
from yurt.models import (
    NestTemperatureReading,
    NestHumidityReading,
    NestTemperatureTarget,
    NestTemperatureTarget,
)


class Command(BaseCommand):
    args = '<none>'
    help = 'update the server'

    def handle(self):
        api = get_nest_wrapper()
        for house in api.get_structures():
            for device in house.get_sensors():
                when = device.get_timestamp()
                readings = device.get_current_readings()
                targets = device.get_target_readings()
                # OK. Let's store the data.

                NestTemperatureReading.create(
                    when=when,
                    measurement=readings['temperature']
                ).save()

                NestHumidityReading.create(
                    when=when,
                    measurement=readings['humidity']
                ).save()
