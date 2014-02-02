import requests


def _create_models(info):
    structures = info['structure']
    devices = info['device']
    shared = info['shared']

    for structure_id, structure in structures.items():
        house = NestHouse(structure_id, structure)
        for device_id in house.data['devices']:
            device_id = device_id[len("device."):]

            device = devices[device_id]
            device.update(shared[device_id])

            house.add_sensor(NestSensor(device_id, device))
        yield house


class NestHouse(object):
    def __init__(self, id_, data):
        self.id = id_
        self.name = data['name']
        self.location = data['location']
        self.data = data
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def get_sensors(self):
        return self.sensors


class NestSensor(object):
    def __init__(self, id_, data):
        self.id = id_
        self.data = data
        self.sensors = []

    def get_current_readings(self):
        return {
            "humidity": self.data['current_humidity'],
            "temperature": self.data['current_temperature']
        }

    def get_target_readings(self):
        return {
            "temperature": self.data['target_temperature'],
            "humidity": self.data['target_humidity'],
        }


class NestAPI(object):
    _UAS = "Nest/1.1.0.10 CFNetwork/548.0.4"
    _LOGIN_URL = "https://home.nest.com/user/login"
    _STATUS_URL = "{base}/v2/mobile/user.{user_id}"

    def __init__(self, username, password):
        headers = {"user-agent": self._UAS,}
        payload = {
            "username": username,
            "password": password,
        }

        data = requests.post(
            self._LOGIN_URL,
            data=payload,
            headers=headers
        ).json()

        self.urls = data['urls']
        self.token = data['access_token']
        self.user_id = data['userid']

    def request(self, method, **kwargs):
        headers = {
            "user-agent": self._UAS,
            "Authorization":"Basic {0}".format(self.token),
            "X-nl-user-id": self.user_id,
            "X-nl-protocol-version": "1",
        }

        return requests.get(
            method.format(
                base=self.urls['transport_url'],
                user_id=self.user_id
            ),
            headers=headers,
            data=kwargs
        ).json()

    def status(self):
        return self.request(self._STATUS_URL)

    def get_structures(self):
        info = self.status()
        return _create_models(info)
