from django.core.management.base import BaseCommand, CommandError
from yurt.nest import get_nest_wrapper
from yurt.models import NestTemperatureReading, NestHumidityReading


class Command(BaseCommand):
    args = '<none>'
    help = 'update the server'

    def handle(self):
        api = get_nest_wrapper()
        for house in api.get_structures():
            for device in house.get_sensors():
                print device
