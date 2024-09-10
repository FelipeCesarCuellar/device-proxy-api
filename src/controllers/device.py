import logging
from mappers.device import DeviceMapper

class DeviceController(object):
    def __init__(self, db_session):
        self.logger = logging.getLogger(__name__)
        self.db_session = db_session

    def create_device(self, device_source):
        device_model = DeviceMapper.toModel(device_source)
        self.db_session.add(device_model)
        self.db_session.commit()

        return DeviceMapper.toDTO(device_model)