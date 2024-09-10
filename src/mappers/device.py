from uuid          import uuid4
from models.device import Device

class DeviceMapper():

    @staticmethod
    def toModel(device_source):
        my_model = Device()
        my_model.name = device_source['name']
        my_model.settings = device_source['settings']
        my_model.device_key = str(uuid4())

        if device_source.get('signature_key') is not None:
            my_model.signature_key = device_source['signature_key']
        else:
            my_model.signature_key = str(uuid4())

        return my_model

    @staticmethod
    def toDTO(device_model: Device):
        my_dto = dict()
        my_dto['name'] = device_model.name
        my_dto['device_key'] = device_model.device_key
        my_dto['settings'] = device_model.settings
        # my_dto['created_at'] = device_model.created_at

        # if device_model.deactivated_on is not None:
        #     my_dto['deactivated_on'] = device_model.deactivated_on

        return my_dto